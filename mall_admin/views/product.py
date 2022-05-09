
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall.apis import productApi
from mall.dataFormat import ProductFields
from toolset.utils import isDateFormat, str2bool
from toolset.viewUtils import viewResponse
from mall_admin.apis import couponApi, discountApi


def _validateParameter(request, operation):
    # 获取创建者 判断管理员权限

    # creatorId = _
    name = request.data.get("name")
    category = request.data.get("category")
    subCategory = request.data.get("subCategory")

    if name is None and operation == 'post':
        raise ValidationError(_("Title can't be empty."))

    # 上传oss

    params = {
        'name': name,
        'category': category,
        'subCategory': subCategory,
        'color': request.data.get("color"),
        'price': request.data.get("price"),
        'description': request.data.get("description"),
        'size': request.data.get("size"),
        'weight': request.data.get("weight"),
        'humanForm': request.data.get("humanForm"),
        'carForm': request.data.get("carForm"),
        'material': request.data.get("material"),
        'communicationMethod': request.data.get("communicationMethod"),
        'servo': request.data.get("servo"),
        'addOns': request.data.get("addOns"),
        'loudspeaker': request.data.get("loudspeaker"),
        'mic': request.data.get("mic"),
        'microchip': request.data.get("microchip"),
        'programmable': request.data.get("programmable"),
        'voiceControl': request.data.get("voiceControl"),
        'mobileControl': request.data.get("mobileControl"),
        'powerAdapter': request.data.get("powerAdapter"),
        'batteryCapacity': request.data.get("batteryCapacity"),
        'batteryType': request.data.get("batteryType"),
        'peripheralInterface': request.data.get("peripheralInterface"),
        'controlMethod': request.data.get("controlMethod"),
        # 'creatorId': creatorId,
    }

    return params


class Product(APIView):
    def put(self, request, prodcutId, format=None):

        params = _validateParameter(request, operation='put')

        prodcutId = productApi.update(prodcutId, **params)

        product = productApi.read(
            query={'id': prodcutId
                   },
            fields=ProductFields.brief)

        return viewResponse({
            "product": product["products"][0]
        })

    def delete(self, request, prodcutId, format=None):

        # 验证管理员身份

        productApi.delete(prodcutId)
        return viewResponse()


class ProductNew(APIView):
    def post(self, request, format=None):
        params = _validateParameter(request, operation='post')

        prodcutId = productApi.create(**params)
        product = productApi.read(
            query={'id': prodcutId
                   },
            fields=ProductFields.brief)

        return viewResponse({
            "product": product["products"][0]
        })