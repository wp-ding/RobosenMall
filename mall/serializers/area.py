
from toolset.dataSerializer import DataSerializer
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT
from mall.models import Area


class AreaSerializer(DataSerializer):
    def __init__(self, area, fields, parameters=None):
        if isinstance(area, int) or isinstance(area, str):
            area = Area.objects.get(pk=area)

        super(AreaSerializer, self).__init__(area, fields, parameters)

        self._area = area
        if parameters is None:
            parameters = {}

    def id(self, fields=None):
        if not self._area:
            return None
        return self._area.id

    def name(self, fields=None):
        if not self._area:
            return None
        return self._area.name

    def parent(self, fields=None):
        if not self._area:
            return None
        parent = Area.objects.get(pk=self._area.parent_id)
        return {"id": parent.id, "name": parent.name}



