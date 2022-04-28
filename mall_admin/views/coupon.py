
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall_admin.apis import couponApi
from mall_admin.dataFormat import CouponFields
from toolset.viewUtils import viewResponse
from toolset.utils import str2bool, isDateFormat
from mall.apis import prodcutApi


class CouponFind(APIView):
    def get(self, request, format=None):

        code = request.GET.get("code")
        title = request.GET.get("title")
        product = request.GET.get("product")

        start = int(request.GET.get("start", 0))
        count = int(request.GET.get("count", 24))

        couponList = couponApi.read(
            query={
                   'code': code,
                   'title': title,
                   'product': product,
                   'count': count,
                   'start': start
                   },
            fields=CouponFields.brief)

        return viewResponse({
            "coupons": couponList["coupons"],
            "total": couponList["total"]
        })


def _validateParameter(request, operation):
    # 获取创建者 判断管理员权限

    # creatorId = _
    title = request.data.get("title")
    amount = request.data.get("amount")
    threshold = request.data.get("threshold")
    expiration = request.data.get("expiration")
    auto = request.data.get("auto")
    limit = request.data.get("limit")
    product = request.data.get("product")

    if title is None and operation == 'post':
        raise ValidationError(_("Title can't be empty."))

    if amount is None and operation == 'post':
        raise ValidationError(_("Amount can't be empty."))

    if product:
        products = prodcutApi.read(query={'id': product}, fields={"id": True})['products']
        if products:
            raise ValidationError(_("The product does not exist"))

    params = {
        'title': title,
        'amount': amount,
        'threshold': threshold,
        'limit': limit,
        'product': product,
        'expiration': isDateFormat(expiration, format='date'),
        'auto': str2bool(auto),
        # 'creatorId': creatorId,
    }

    return params


class Coupon(APIView):
    def put(self, request, couponId, format=None):

        params = _validateParameter(request, operation='put')

        couponId = couponApi.update(couponId, **params)

        activity = couponApi.read(
            query={'id': couponId
                   },
            fields=CouponFields.brief)

        return viewResponse({
            "coupon": activity["coupons"][0]
        })

    def delete(self, request, couponId, format=None):

        # 验证管理员身份

        couponApi.delete(couponId)
        return viewResponse()


class CouponNew(APIView):
    def post(self, request, format=None):
        params = _validateParameter(request, operation='post')

        couponId = couponApi.create(**params)
        activity = couponApi.read(
            query={'id': couponId
                   },
            fields=CouponFields.brief)

        return viewResponse({
            "coupon": activity["coupons"][0]
        })