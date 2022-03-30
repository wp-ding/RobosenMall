
from mall.models import Activity
from mall.serializers import ActivitySerializer


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    id = query.get('id')
    if id:
        params = {
            'pk': id,
            # 'inactive': False,
        }
        activity = Activity.objects.get(**params)

        activity_list = [activity] if activity else []
        total = len(activity_list)
    else:
        activity_list = []

    activityData = [ActivitySerializer(activity, fields=fields).data for activity in activity_list]

    return {
        "activities": activityData
    }




def update(activityId, **kwargs):
    pass


def create(**kwargs):
    title = kwargs.get('title')
    activity = Activity.objects.create(title=title)
    return activity.id


def delete(activityId,  **kwargs):
    pass