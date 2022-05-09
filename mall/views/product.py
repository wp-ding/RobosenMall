
from rest_framework.views import APIView
from mall.apis import productApi
from mall.dataFormat import ProductFields
from toolset.viewUtils import viewResponse


class ProductFind(APIView):
    def get(self, request, format=None):

        q = request.GET.get("q")
        category = request.GET.get("category")
        subCategory = request.GET.get("subCategory")

        start = int(request.GET.get("start", 0))
        count = int(request.GET.get("count", 24))

        product = productApi.read(
            query={'q': q,
                   'category': category,
                   'subCategory': subCategory,
                   'count': count,
                   'start': start
                   },
            fields=ProductFields.brief)

        return viewResponse({
            "product": product["products"],
            "total": product["total"]
            })
