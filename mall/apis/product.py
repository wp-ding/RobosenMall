
from mall.models import Product, ProductInfo, ProductPicture
from mall.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    id = query.get('id')
    subCategory = query.get('subCategory')
    category = query.get('category')
    public = query.get('public', True)

    isAdmin = False  # 管理员

    if id:
        params = {
            'pk': id,
            'inactive': False,
        }
        if subCategory:
            params["subCategory"] = subCategory
        products = Product.objects.filter(**params).all()

        total = len(products)
    elif category:
        params = {
            'category': int(category),
            'inactive': False,
        }
        products = Product.objects.filter(**params).order_by("-created")

        total = products.count()
    elif public:
        # 管理员可用
        params = {
            'public': public,
            'inactive': False,
        }
        products = Product.objects.filter(**params).order_by("-created")

        total = products.count()
    else:
        start = query.get('start', 0)
        count = query.get('count', 24)
        products = Product.objects.filter(inactive=False).order_by("-created")

        total = products.count()
        products = products[start:start + count]

    if not isAdmin:
        products = products.filter(public=True)

    productData = [ProductSerializer(product, fields=fields).data for product in products]

    return {
        "products": productData,
        "total": total,
    }


def update(productId, **kwargs):
    name = kwargs.get('name')

    product = Product.objects.filter(pk=productId).first()

    if not product:
        raise ValidationError(_("The Product does not exist"))

    if name:
        product.name = name.strip()

    _productAddtions(product, **kwargs)

    return product.id


def create(**kwargs):
    name = kwargs.get('name')

    product = Product.objects.create(name=name)

    _productAddtions(product, **kwargs)

    return product.id


def delete(productId,  **kwargs):

    product = Product.objects.filter(pk=productId).first()
    if not product:
        raise ValidationError(_("The Product does not exist"))

    product.update(inactive=True)


def _productAddtions(product, **kwargs):

    category = kwargs.get('category')
    subCategory = kwargs.get('subCategory')
    color = kwargs.get('color')
    price = kwargs.get('price')
    description = kwargs.get('description')
    size = kwargs.get('size')
    weight = kwargs.get('weight')
    humanForm = kwargs.get('humanForm')
    carForm = kwargs.get('carForm')
    material = kwargs.get('material')
    servo = kwargs.get('servo')
    communicationMethod = kwargs.get('communicationMethod')
    controlMethod = kwargs.get('controlMethod')
    peripheralInterface = kwargs.get('peripheralInterface')
    batteryType = kwargs.get('batteryType')
    batteryCapacity = kwargs.get('batteryCapacity')
    powerAdapter = kwargs.get('powerAdapter')
    mobileControl = kwargs.get('mobileControl')
    voiceControl = kwargs.get('voiceControl')
    programmable = kwargs.get('programmable')
    microchip = kwargs.get('microchip')
    mic = kwargs.get('mic')
    loudspeaker = kwargs.get('loudspeaker')
    addOns = kwargs.get('addOns')
    pictures = kwargs.get('pictures')
    index = kwargs.get('index')
    creatorId = kwargs.get('creatorId')
    public = kwargs.get('public')

    if category:
        product.category = category
    if subCategory:
        product.subCategory = subCategory
    if color:
        product.color = color
    if price:
        product.price = float(price) * 100
    if description:
        product.description = description
    if creatorId:
        product.creatorId = creatorId
    if public:
        product.public = public

    product.save()

    productInfo, _ = ProductInfo.objects.update_or_create(productId=product.id).first()

    if size:
        productInfo.size = size
    if weight:
        productInfo.weight = weight
    if humanForm:
        productInfo.humanForm = humanForm
    if carForm:
        productInfo.carForm = carForm
    if material:
        productInfo.material = material
    if servo:
        productInfo.servo = servo
    if communicationMethod:
        productInfo.communicationMethod = communicationMethod
    if controlMethod:
        productInfo.controlMethod = controlMethod
    if peripheralInterface:
        productInfo.peripheralInterface = peripheralInterface
    if batteryType:
        productInfo.batteryType = batteryType
    if batteryCapacity:
        productInfo.batteryCapacity = batteryCapacity
    if powerAdapter:
        productInfo.powerAdapter = powerAdapter
    if mobileControl:
        productInfo.mobileControl = mobileControl
    if voiceControl:
        productInfo.voiceControl = voiceControl
    if programmable:
        productInfo.programmable = programmable
    if microchip:
        productInfo.microchip = microchip
    if mic:
        productInfo.mic = mic
    if loudspeaker:
        productInfo.loudspeaker = loudspeaker
    if addOns:
        productInfo.addOns = addOns
    productInfo.save()

    if pictures:
        productPicture = ProductPicture.objects.filter(productId=product.id).order_by("index").all()
        if not productPicture:
            raise ValidationError(_("The ProductPicture does not exist"))
        if index:
            currentPicture = productPicture.filter(index=index)
            currentPicture.picture = pictures
            currentPicture.save()
        else:
            productPicture.delete()
            i = 0
            while i < len(pictures):
                currentPicture = pictures[i]
                productPicture.picture = currentPicture
                productPicture.index = i
                productPicture.save()

                i += 1




