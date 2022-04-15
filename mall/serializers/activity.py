
from toolset.dataSerializer import DataSerializer
from mall.models import Activity
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT


class ActivitySerializer(DataSerializer):
    def __init__(self, activity, fields, parameters=None):
        if isinstance(activity, int) or isinstance(activity, str):
            activity = Activity.objects.get(pk=activity)

        super(ActivitySerializer, self).__init__(activity, fields, parameters)

        self._activity = activity
        if parameters is None:
            parameters = {}

    def title(self, fields=None):
        return self._activity.title

    def content(self, fields=None):
        return self._activity.content

    def coverImage(self, fields=None):
        # 拼接url
        return self._activity.coverImage

    def start(self, fields=None):
        return timezone.localtime(self._activity.start).strftime(DATE_TIME_FORMAT)

    def end(self, fields=None):
        return timezone.localtime(self._activity.end).strftime(DATE_TIME_FORMAT)

    def created(self, fields=None):
        return timezone.localtime(self._activity.created).strftime(DATE_TIME_FORMAT)

    def status(self, fields=None):
        return self._activity.status

    def inactive(self, fields=None):
        return self._activity.inactive

    def creator(self, fields=None):
        # 查询创建者
        return self._activity.creatorId


