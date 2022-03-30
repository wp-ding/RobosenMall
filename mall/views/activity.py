
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from mall.apis import activityApi
from mall.dataFormat import ActivityFields
from rest_framework.response import Response


class ActivityFind(APIView):
    def get(self, request, format=None):
        pass


class Activity(APIView):
    def put(self, request, activityId, format=None):
        pass

    def delete(self, request, activityId, format=None):
        pass


class ActivityNew(APIView):
    def post(self, request, format=None):
        title = request.data.get("title")

        if title is None:
            raise ValidationError(_("Title error."))

        params = {
            'title': title
        }
        activityId = activityApi.create(**params)
        activity = activityApi.read(
            query={'id': activityId
                   },
            fields=ActivityFields.brief)

        return Response({
            "activity": activity["activities"][0]
        })