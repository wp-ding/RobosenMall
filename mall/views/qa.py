
from rest_framework.views import APIView
from mall.apis import qaApi
from mall.dataFormat import QAFields
from toolset.viewUtils import viewResponse


class QaFind(APIView):
    def get(self, request, format=None):

        start = int(request.GET.get("start", 0))
        count = int(request.GET.get("count", 24))

        qaList = qaApi.read(
            query={
                   'count': count,
                   'start': start
                   },
            fields=QAFields.brief)

        return viewResponse({
            "qas": qaList["qas"]
            })


