
from toolset.dataSerializer import DataSerializer
from mall.models import Activity


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
