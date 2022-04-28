
from mall.models import Activity
from mall.serializers import ActivitySerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    id = query.get('id')
    if id:
        params = {
            'pk': id,
            'inactive': False,
        }
        activity_list = Activity.objects.filter(**params).all()

        total = len(activity_list)
    else:
        start = query.get('start', 0)
        count = query.get('count', 24)
        activity_list = Activity.objects.filter(inactive=False).order_by("-start", "-end")

        total = activity_list.count()
        activity_list = activity_list[start:start + count]

    activityData = [ActivitySerializer(activity, fields=fields).data for activity in activity_list]

    return {
        "activities": activityData,
        "total": total,
    }


def update(activityId, **kwargs):

    title = kwargs.get('title')
    content = kwargs.get('content')
    coverImage = kwargs.get('coverImage')
    start = kwargs.get('start')
    end = kwargs.get('end')
    status = kwargs.get('status')
    discount = kwargs.get('discount')
    coupon = kwargs.get('coupon')

    activity = Activity.objects.filter(pk=activityId).first()
    if not activity:
        raise ValidationError(_("The activity does not exist"))

    if title and title != activity.title:
        activity.title = title

    if content and content != activity.content:
        activity.content = content

    if coverImage and coverImage != activity.coverImage:
        activity.coverImage = coverImage

    if start and start != activity.start:
        activity.start = start

    if end and end != activity.end:
        activity.start = end

    if discount and discount != activity.discount:
        activity.discount = discount

    if coupon and coupon != activity.coupon:
        activity.coupon = coupon

    activity.status = status
    activity.save()

    return activity.id


def create(**kwargs):
    title = kwargs.get('title')
    discount = kwargs.get('discount')
    coupon = kwargs.get('coupon')
    content = kwargs.get('content')
    coverImage = kwargs.get('coverImage')
    start = kwargs.get('start')
    end = kwargs.get('end')
    creatorId = kwargs.get('creatorId')

    activity = Activity.objects.create(title=title.strip(), creatorId=creatorId)

    if discount:
        activity.discount = discount

    if coupon:
        activity.coupon = coupon

    if content:
        activity.content = content

    if coverImage:
        activity.coverImage = coverImage

    if start:
        activity.start = start

    if end:
        activity.end = end

    activity.save()

    return activity.id


def delete(activityId,  **kwargs):

    activity = Activity.objects.filter(pk=activityId).first()
    if not activity:
        raise ValidationError(_("The activity does not exist"))

    activity.inactive = True
    activity.save()