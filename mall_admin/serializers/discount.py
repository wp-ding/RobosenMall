
from toolset.dataSerializer import DataSerializer
from mall.models import Discount, DiscountProduct
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT


class DiscountSerializer(DataSerializer):
    def __init__(self, discount, fields, parameters=None):
        if isinstance(discount, int) or isinstance(discount, str):
            discount = Discount.objects.get(pk=discount)

        super(DiscountSerializer, self).__init__(discount, fields, parameters)

        self._discount = discount
        if parameters is None:
            parameters = {}

    def amount(self, fields=None):
        return self._discount.amount * 100 if self._discount.type == 1 else self._discount.amount

    def threshold(self, fields=None):
        return self._discount.threshold * 100

    def created(self, fields=None):
        return timezone.localtime(self._discount.created).strftime(DATE_TIME_FORMAT)

    def creator(self, fields=None):
        # 查询创建者
        return self._discount.creatorId


