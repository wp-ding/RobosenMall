
from toolset.dataSerializer import DataSerializer
from mall.models import QA
from django.utils import timezone
from toolset.utils import DATE_TIME_FORMAT


class QASerializer(DataSerializer):
    def __init__(self, qa, fields, parameters=None):
        if isinstance(qa, int) or isinstance(qa, str):
            qa = QA.objects.get(pk=qa)

        super(QASerializer, self).__init__(qa, fields, parameters)

        self._qa = qa
        if parameters is None:
            parameters = {}

    def question(self, fields=None):
        return self._qa.question

    def answer(self, fields=None):
        return self._qa.answer

    def created(self, fields=None):
        return timezone.localtime(self._qa.created).strftime(DATE_TIME_FORMAT)

    def inactive(self, fields=None):
        return self._qa.inactive

    def creator(self, fields=None):
        # 查询创建者
        return self._qa.creatorId


