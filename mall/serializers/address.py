
from toolset.dataSerializer import DataSerializer
from mall.models import Address
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT
from mall.serializers import AreaSerializer


class AddressSerializer(DataSerializer):
    def __init__(self, address, fields, parameters=None):
        if isinstance(address, int) or isinstance(address, str):
            address = Address.objects.get(pk=address)

        super(AddressSerializer, self).__init__(address, fields, parameters)

        self._address = address
        if parameters is None:
            parameters = {}

    def title(self, fields=None):
        return self._address.title

    def receiver(self, fields=None):
        return self._address.receiver

    def province(self, fields=None):
        if not self._address.province:
            return None
        result = AreaSerializer(self._address.province, fields={"parent": True}).data
        return result['parent']["name"]

    def city(self, fields=None):
        if not self._address.city:
            return None
        result = AreaSerializer(self._address.city, fields={"parent": True}).data
        return result['parent']["name"]

    def district(self, fields=None):
        if not self._address.district:
            return None
        result = AreaSerializer(self._address.district, fields={"parent": True}).data
        return result['parent']["name"]

    def created(self, fields=None):
        return timezone.localtime(self._address.created).strftime(DATE_TIME_FORMAT)

    def user(self, fields=None):
        # 查询创建者
        return self._address.userId


