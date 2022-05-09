
from toolset.dataSerializer import DataSerializer
from mall.models import Coupon, DiscountProduct
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT


class CouponSerializer(DataSerializer):
    def __init__(self, coupon, fields, parameters=None):
        if isinstance(coupon, int) or isinstance(coupon, str):
            coupon = Coupon.objects.get(pk=coupon)

        super(CouponSerializer, self).__init__(coupon, fields, parameters)

        self._coupon = coupon
        if parameters is None:
            parameters = {}

    def amount(self, fields=None):
        return self._coupon.amount / 100

    def threshold(self, fields=None):
        return self._coupon.threshold / 100

    def created(self, fields=None):
        return timezone.localtime(self._coupon.created).strftime(DATE_TIME_FORMAT)

    def creator(self, fields=None):
        # 查询创建者
        return self._coupon.creatorId


