
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall_admin.apis import discountApi
from mall_admin.dataFormat import DiscountFields
from toolset.viewUtils import viewResponse
from toolset.utils import str2bool, isDateFormat
from mall.apis import productApi


class DiscountFind(APIView):
    def get(self, request, format=None):

        code = request.GET.get("code")
        title = request.GET.get("title")
        product = request.GET.get("product")

        start = int(request.GET.get("start", 0))
        count = int(request.GET.get("count", 24))

        discountList = discountApi.read(
            query={
                   'code': code,
                   'title': title,
                   'product': product,
                   'count': count,
                   'start': start
                   },
            fields=DiscountFields.brief)

        return viewResponse({
            "discounts": discountList["discounts"],
            "total": discountList["total"]
        })


def _validateParameter(request, operation):
    # 获取创建者 判断管理员权限

    # creatorId = _
    title = request.data.get("title")
    amount = request.data.get("amount")
    threshold = request.data.get("threshold")
    type = request.data.get("type")
    expiration = request.data.get("expiration")
    auto = request.data.get("auto")
    limit = request.data.get("limit")
    product = request.data.get("product")

    if title is None and operation == 'post':
        raise ValidationError(_("Title can't be empty."))

    if amount is None and operation == 'post':
        raise ValidationError(_("Amount can't be empty."))

    if product:
        products = productApi.read(query={'id': product}, fields={"id": True})
        productIds = [product["id"] for product in products['products']]
        missProduct = list(set(product) - set(productIds))
        if missProduct:
            raise ValidationError(_("Some product does not exist"))

    params = {
        'title': title,
        'amount': amount,
        'threshold': threshold,
        'type': type,
        'limit': limit,
        'product': product,
        'expiration': isDateFormat(expiration, format='date'),
        'auto': str2bool(auto),
        # 'creatorId': creatorId,
    }

    return params


class Discount(APIView):
    def put(self, request, discountId, format=None):

        params = _validateParameter(request, operation='put')

        discountId = discountApi.update(discountId, **params)

        activity = discountApi.read(
            query={'id': discountId
                   },
            fields=DiscountFields.brief)

        return viewResponse({
            "discount": activity["discounts"][0]
        })

    def delete(self, request, discountId, format=None):

        # 验证管理员身份

        discountApi.delete(discountId)
        return viewResponse()


class DiscountNew(APIView):
    def post(self, request, format=None):
        params = _validateParameter(request, operation='post')

        discountId = discountApi.create(**params)
        activity = discountApi.read(
            query={'id': discountId
                   },
            fields=DiscountFields.brief)

        return viewResponse({
            "discount": activity["discounts"][0]
        })