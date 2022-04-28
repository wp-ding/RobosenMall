
from mall.models import Coupon
from mall_admin.serializers import CouponSerializer
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
        coupons = Coupon.objects.filter(**params).all()

        total = len(coupons)
    elif title:
        coupons = Coupon.objects.filter(title__contains=title, closed=False).all()

        total = len(coupons)
    elif product:
        coupons = Coupon.objects.filter(product=product, closed=False).all()
        total = len(coupons)

    else:
        start = query.get('start', 0)
        count = query.get('count', 24)
        coupons = Coupon.objects.filter(closed=False).order_by("-created")

        total = coupons.count()
        coupons = coupons[start:start + count]

    couponData = [CouponSerializer(coupon, fields=fields).data for coupon in coupons]

    return {
        "coupons": couponData,
        "total": total,
    }


def update(couponId, **kwargs):

    title = kwargs.get('title')
    amount = kwargs.get('amount')
    threshold = kwargs.get('threshold')
    limit = kwargs.get('limit')
    product = kwargs.get('product')
    expiration = kwargs.get('expiration')
    auto = kwargs.get('auto')

    coupon = Coupon.objects.filter(code=couponId).first()
    if not coupon:
        raise ValidationError(_("The Coupon does not exist"))

    if title and title != coupon.title:
        coupon.title = title.strip()

    if amount:
        coupon.amount = float(amount) / 100

    if threshold:
        coupon.threshold = float(threshold) / 100

    if auto:
        coupon.auto = auto

    if expiration and expiration != coupon.expiration:
        coupon.expiration = expiration

    if limit and limit != coupon.limit:
        coupon.limit = int(limit)

    if product and product != coupon.product:
        coupon.product = product

    coupon.save()

    return coupon.code


def create(**kwargs):
    title = kwargs.get('title')
    amount = kwargs.get('amount')
    threshold = kwargs.get('threshold')
    limit = kwargs.get('limit')
    product = kwargs.get('product')
    expiration = kwargs.get('expiration')
    auto = kwargs.get('auto')
    creatorId = kwargs.get('creatorId')

    code = generateCode()
    tried = 0
    while Coupon.objects.filter(code=code).exists() and tried < 5:
        code = generateCode()
        tried += 1

    coupon = Coupon.objects.create(code=code, creatorId=creatorId)

    if title:
        coupon.title = title.strip()

    if amount:
        coupon.amount = float(amount) / 100

    if threshold:
        coupon.threshold = float(threshold) / 100

    if auto:
        coupon.auto = auto

    if expiration:
        coupon.expiration = expiration

    if limit:
        coupon.limit = int(limit)

    if product:
        coupon.product = product

    coupon.save()

    return coupon.code


def delete(couponId, **kwargs):
    coupon = Coupon.objects.filter(code=couponId).all()
    if not coupon:
        raise ValidationError(_("The Coupon does not exist"))

    coupon.update(closed=True)