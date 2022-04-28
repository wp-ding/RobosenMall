
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall.apis import activityApi
from mall.dataFormat import ActivityFields
from toolset.utils import isDateFormat, str2bool
from toolset.viewUtils import viewResponse


class ActivityFind(APIView):
    def get(self, request, format=None):
        q = request.GET.get("q")

        start = int(request.GET.get("start", 0))
        count = int(request.GET.get("count", 24))

        activity = activityApi.read(
            query={'q': q,
                   'count': count,
                   'start': start
                   },
            fields=ActivityFields.brief)

        return viewResponse({
            "activity": activity["activities"]
            })
