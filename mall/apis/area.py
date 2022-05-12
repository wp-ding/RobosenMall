
from mall.models import Area
from mall.serializers import AreaSerializer
from django.core import cache


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    area_id = query.get('area_id')

    cacheClient = cache.caches["redis"]
    if not area_id:

        pro_list = cacheClient.get("proList")
        if pro_list:
            areaData = eval(pro_list)
        else:
            pro_list = Area.objects.filter(level_id=1).all()
            areaData = [AreaSerializer(pro, fields=fields).data for pro in pro_list]
            cacheClient.set("proList", str(areaData), 3600 * 24)
    else:
        areaData = cacheClient.get(area_id)
        if not areaData:
            city_list = Area.objects.filter(parent_id=area_id).all()
            areaData = [AreaSerializer(city, fields=fields).data for city in city_list]
            cacheClient.set(area_id, str(areaData), 3600 * 24)

    return {
        "areas": areaData,
    }

