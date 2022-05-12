
from mall.models import Address
from mall.serializers import AddressSerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    id = query.get('id')
    user_id = query.get('userId')

    if id:
        params = {
            'pk': id,
            'inactive': False,
            'userId': user_id,
        }
        addresses = Address.objects.filter(**params).all()

        total = len(addresses)

    else:

        addresses = Address.objects.filter(inactive=False, userId=user_id).order_by('-isDefault', "-created")

        total = addresses.count()

    addressData = [AddressSerializer(address, fields=fields).data for address in addresses]

    return {
        "addresses": addressData,
        "total": total,
    }


def update(addressId, **kwargs):

    user_id = kwargs.get('userId')

    params = {
        'pk': addressId,
        'inactive': False,
        'userId': user_id,
    }
    address = Address.objects.filter(**params).first()

    if not address:
        raise ValidationError(_("The Address does not exist"))

    _addressAddtions(address, **kwargs)

    return address.id


def create(**kwargs):

    user_id = kwargs.get('userId')
    address = Address.objects.create(userId=user_id)

    _addressAddtions(address, **kwargs)

    return address.id


def delete(addressId,  **kwargs):
    user_id = kwargs.get('userId')

    params = {
        'pk': addressId,
        'inactive': False,
        'userId': user_id,
    }
    address = Address.objects.filter(**params).first()

    if not address:
        raise ValidationError(_("The Address does not exist"))

    address.inactive = True
    address.save()


def _addressAddtions(address, **kwargs):

    title = kwargs.get('title')
    receiver = kwargs.get('receiver')
    province = kwargs.get('province')
    city = kwargs.get('city')
    district = kwargs.get('district')
    place = kwargs.get('place')
    mobile = kwargs.get('mobile')
    tel = kwargs.get('tel')
    isDefault = kwargs.get('isDefault')
    user_id = kwargs.get('userId')

    if title:
        address.title = title
    if receiver:
        address.receiver = receiver
    if place:
        address.place = place
    if mobile:
        address.mobile = mobile
    if tel:
        address.tel = tel
    if province:
        address.province = province
    if city:
        address.city = city
    if district:
        address.district = district
    if isDefault:
        Address.objects.filter(userId=user_id, inactive=False).update(isDefault=False)
        address.isDefault = isDefault
    address.save()





