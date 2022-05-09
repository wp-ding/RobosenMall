
from toolset.dataSerializer import DataSerializer
from mall.models import Product, ProductInfo
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT
from mall.dataFormat import ProductFields


class ProductSerializer(DataSerializer):
    def __init__(self, product, fields, parameters=None):
        if isinstance(product, int) or isinstance(product, str):
            product = Product.objects.get(pk=product)

        super(ProductSerializer, self).__init__(product, fields, parameters)

        self._product = product
        self._productInfo = ProductInfo.objects.get(productId=product.id)
        if parameters is None:
            parameters = {}

    def price(self, fields=None):
        if not self._product.price:
            return None
        return self._product.price / 100

    # def pictures(self, fields=None):
    #     # 拼接url
    #     return self._activity.coverImage

    def created(self, fields=None):
        return timezone.localtime(self._product.created).strftime(DATE_TIME_FORMAT)

    def creator(self, fields=None):
        # 查询创建者
        return self._product.creatorId

    def size(self, fields=None):
        if not self._productInfo.size:
            return None
        return self._productInfo.size

    def weight(self, fields=None):
        if not self._productInfo.weight:
            return None
        return self._productInfo.weight

    def humanForm(self, fields=None):
        if not self._productInfo.humanForm:
            return None
        return self._productInfo.humanForm

    def carForm(self, fields=None):
        if not self._productInfo.carForm:
            return None
        return self._productInfo.carForm

    def material(self, fields=None):
        if not self._productInfo.material:
            return None
        return self._productInfo.material

    def servo(self, fields=None):
        if not self._productInfo.servo:
            return None
        return self._productInfo.servo

    def communicationMethod(self, fields=None):
        if not self._productInfo.communicationMethod:
            return None
        return self._productInfo.communicationMethod

    def controlMethod(self, fields=None):
        if not self._productInfo.controlMethod:
            return None
        return self._productInfo.controlMethod

    def peripheralInterface(self, fields=None):
        if not self._productInfo.peripheralInterface:
            return None
        return self._productInfo.peripheralInterface

    def batteryType(self, fields=None):
        if not self._productInfo.batteryType:
            return None
        return self._productInfo.batteryType

    def batteryCapacity(self, fields=None):
        if not self._productInfo.batteryCapacity:
            return None
        return self._productInfo.batteryCapacity

    def powerAdapter(self, fields=None):
        if not self._productInfo.powerAdapter:
            return None
        return self._productInfo.powerAdapter

    def mobileControl(self, fields=None):
        if not self._productInfo.mobileControl:
            return None
        return self._productInfo.mobileControl

    def voiceControl(self, fields=None):
        if not self._productInfo.voiceControl:
            return None
        return self._productInfo.voiceControl

    def programmable(self, fields=None):
        if not self._productInfo.programmable:
            return None
        return self._productInfo.programmable

    def microchip(self, fields=None):
        if not self._productInfo.microchip:
            return None
        return self._productInfo.microchip

    def mic(self, fields=None):
        if not self._productInfo.mic:
            return None
        return self._productInfo.mic

    def loudspeaker(self, fields=None):
        if not self._productInfo.loudspeaker:
            return None
        return self._productInfo.loudspeaker

    def addOns(self, fields=None):
        if not self._productInfo.addOns:
            return None
        return self._productInfo.addOns