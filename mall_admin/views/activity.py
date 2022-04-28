
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall.apis import activityApi
from mall.dataFormat import ActivityFields
from toolset.utils import isDateFormat, str2bool
from toolset.viewUtils import viewResponse
from mall_admin.apis import couponApi, discountApi


def _validateParameter(request, operation):
    # 获取创建者 判断管理员权限

    # creatorId = _
    title = request.data.get("title")
    content = request.data.get("content")
    coverImage = request.data.get("cover_url")  # 上传oss
    datetime = request.data.get("datetime")
    coupon = request.data.get("coupon")
    discount = request.data.get("discount")

    if title is None and operation == 'post':
        raise ValidationError(_("Title can't be empty."))

    if datetime is None and operation == 'post':
        raise ValidationError(_("Datetime can't be empty."))

    start, end = tuple(datetime.split("|")) if datetime else None, None
    if (start is None or end is None) and operation == 'post':
        raise ValidationError(_("Datetime must include start and end dates."))

    if coupon:
        coupons = couponApi.read(query={"code": coupon}, fields={"id": True})["coupons"]
        if not coupons:
            raise ValidationError(_("The coupon does not exist."))
        coupon = coupons[0]['id']


    if discount:
        discounts = discountApi.read(query={"code": discount}, fields={"id": True})["discounts"]
        if not discounts:
            raise ValidationError(_("The discount does not exist."))
        discount = discounts[0]['id']

    # 上传oss

    params = {
        'title': title,
        'content': content,
        'coupon': coupon,
        'discount': discount,
        'coverImage': coverImage,
        'start': isDateFormat(start),
        'end': isDateFormat(end),
        # 'creatorId': creatorId,
    }

    if operation == 'put':
        params['status'] = str2bool(request.data.get("status"))

    return params


class Activity(APIView):
    def put(self, request, activityId, format=None):

        params = _validateParameter(request, operation='put')

        activityId = activityApi.update(activityId, **params)

        activity = activityApi.read(
            query={'id': activityId
                   },
            fields=ActivityFields.brief)

        return viewResponse({
            "activity": activity["activities"][0]
        })

    def delete(self, request, activityId, format=None):

        # 验证管理员身份

        activityApi.delete(activityId)
        return viewResponse()


class ActivityNew(APIView):
    def post(self, request, format=None):
        params = _validateParameter(request, operation='post')

        activityId = activityApi.create(**params)
        activity = activityApi.read(
            query={'id': activityId
                   },
            fields=ActivityFields.brief)

        return viewResponse({
            "activity": activity["activities"][0]
        })