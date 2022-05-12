
from rest_framework.views import APIView
from mall.apis import areaApi, addressApi
from mall.dataFormat import AreaFields, AddressFields
from toolset.viewUtils import viewResponse
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _
from toolset.utils import str2bool, validPhone


class AreaFind(APIView):
    def post(self, request, format=None):

        area_id = request.data.get("area_id")

        areaList = areaApi.read(
            query={
                   'area_id': area_id,
                   },
            fields=AreaFields.brief)

        return viewResponse({
            "areas": areaList["areas"],
        })


def _validateParameter(request, operation):

    userId = 1
    title = request.data.get("title")
    receiver = request.data.get("receiver")
    province = request.data.get("province")
    city = request.data.get("city")
    district = request.data.get("district")
    place = request.data.get("place")
    mobile = request.data.get("mobile")
    tel = request.data.get("tel")
    isDefault = request.data.get("isDefault")

    if receiver is None and operation == 'post':
        raise ValidationError(_("Receiver can't be empty."))
    if mobile:
        if not validPhone(mobile):
            raise ValidationError(_("Phone format error."))

    params = {
        'title': title,
        'receiver': receiver,
        'province': province,
        'city': city,
        'district': district,
        'place': place,
        'mobile': mobile,
        'tel': tel,
        'isDefault': str2bool(isDefault),
        'userId': userId,
    }

    return params


class Address(APIView):
    def put(self, request, addressId, format=None):

        params = _validateParameter(request, operation='put')

        addressId = addressApi.update(addressId, **params)

        address = addressApi.read(
            query={'id': addressId,
                   "userId": params['userId']
                   },
            fields=AddressFields.brief)

        return viewResponse({
            "address": address["addresses"][0]
        })

    def delete(self, request, addressId, format=None):
        userId = 1
        params = {
            "userId": userId
        }

        addressApi.delete(addressId,  **params)
        return viewResponse()


class AddressNew(APIView):
    def post(self, request, format=None):
        params = _validateParameter(request, operation='post')

        addressId = addressApi.create(**params)
        address = addressApi.read(
            query={'id': addressId,
                   "userId": params['userId']
                   },
            fields=AddressFields.brief)

        return viewResponse({
            "address": address["addresses"][0]
        })


class AddressFind(APIView):
    def get(self, request, format=None):

        # 获取本人id
        userId = 1
        id = request.GET.get("addressId")

        address = addressApi.read(
            query={
                   'userId': userId,
                   'id': id,
                   },
            fields=AddressFields.brief)

        return viewResponse({
            "address": address["addresses"]
        })
