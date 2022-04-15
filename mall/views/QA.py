
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
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


class Qa(APIView):
    def put(self, request, qaId, format=None):

        question = request.data.get("question")
        answer = request.data.get("answer")

        params = {
            "question": question,
            "answer": answer,
        }

        qaId = qaApi.update(qaId, **params)

        qa = qaApi.read(
            query={'id': qaId
                   },
            fields=QAFields.brief)

        return viewResponse({
            "qa": qa["qas"][0]
        })

    def delete(self, request, qaId, format=None):

        # 验证管理员身份

        qaApi.delete(qaId)
        return viewResponse()


class QaNew(APIView):
    def post(self, request, format=None):
        # 管理员获取

        question = request.data.get("question")
        answer = request.data.get("answer")

        if question is None:
            raise ValidationError(_("Question can't be empty"))

        params = {
            "question": question,
            "answer": answer,
            # "creatorId": answer,
        }
        qaId = qaApi.create(**params)
        qa = qaApi.read(
            query={'id': qaId
                   },
            fields=QAFields.brief)

        return viewResponse({
            "qa": qa["qas"][0]
        })