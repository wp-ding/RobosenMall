
from mall.models import Discount, DiscountProduct
from mall_admin.serializers import DiscountSerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _
from toolset.utils import generateCode


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    code = query.get('code')
    title = query.get('title')
    product = query.get('product')
    if code:
        params = {
            'code': code,
            'closed': False,
        }
        discounts = Discount.objects.filter(**params).all()

        total = len(discounts)
    elif title:
        discounts = Discount.objects.filter(title__contains=title, closed=False).all()

        total = len(discounts)
    elif product:
        products = DiscountProduct.objects.filter(product__in=product).all()
        discountIds = [product.discount for product in products]
        discounts = Discount.objects.filter(pk__in=discountIds, closed=False).all().order_by("-created")

        total = len(discounts)

    else:
        start = query.get('start', 0)
        count = query.get('count', 24)
        discounts = Discount.objects.filter(closed=False).order_by("-created")

        total = discounts.count()
        discounts = discounts[start:start + count]

    discountData = [DiscountSerializer(discount, fields=fields).data for discount in discounts]

    return {
        "discounts": discountData,
        "total": total,
    }


def update(discountId, **kwargs):

    title = kwargs.get('title')
    amount = kwargs.get('amount')
    threshold = kwargs.get('threshold')
    type = kwargs.get('type')
    limit = kwargs.get('limit')
    product = kwargs.get('product')
    expiration = kwargs.get('expiration')
    auto = kwargs.get('auto')

    discount = Discount.objects.filter(code=discountId).first()
    if not discount:
        raise ValidationError(_("The Discount does not exist"))
    if type and not amount:
        raise ValidationError(_("Change type must upload amount"))

    if title and title != discount.title:
        discount.title = title.strip()

    if type:
        discount.type = int(type)
    if amount:
        discount.amount = float(amount) / 100 if type == 1 else float(amount)

    if threshold:
        discount.threshold = float(threshold) / 100

    if auto:
        discount.auto = auto

    if expiration and expiration != discount.expiration:
        discount.expiration = expiration

    if limit and limit != discount.limit:
        discount.type = int(type)

    if product:
        oldProductObj = DiscountProduct.objects.filter(discount=discount.code).all()
        oldProductIds = [productobj.product for productobj in oldProductObj]
        if oldProductIds != product:
            DiscountProduct.objects.filter(discount=discount.code).delete()
        discountPro = [
            DiscountProduct(discount=discount.id, product=i)
            for i in product
        ]
        DiscountProduct.objects.bulk_create(discountPro)

    discount.save()

    return discount.code


def create(**kwargs):

    title = kwargs.get('title')
    amount = kwargs.get('amount')
    threshold = kwargs.get('threshold')
    type = kwargs.get('type')
    limit = kwargs.get('limit')
    product = kwargs.get('product')
    expiration = kwargs.get('expiration')
    auto = kwargs.get('auto')
    creatorId = kwargs.get('creatorId')

    code = generateCode()
    tried = 0
    while Discount.objects.filter(code=code).exists() and tried < 5:
        code = generateCode()
        tried += 1

    discount = Discount.objects.create(code=code, creatorId=creatorId)

    if title:
        discount.title = title.strip()

    if type:
        discount.type = int(type)

    if amount:
        discount.amount = float(amount) / 100 if type == 1 else float(amount)

    if threshold:
        discount.threshold = float(threshold) / 100

    if auto:
        discount.auto = auto

    if expiration:
        discount.expiration = expiration

    if limit:
        discount.limit = int(limit)

    discount.save()

    if product:
        discountPro = [
            DiscountProduct(discount=discount.id, product=i)
            for i in product
        ]
        DiscountProduct.objects.bulk_create(discountPro)

    return discount.code


def delete(discountId,  **kwargs):

    discount = Discount.objects.filter(code=discountId).all()
    if not discount:
        raise ValidationError(_("The Discount does not exist"))

    discount.update(closed=True)