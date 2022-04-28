
from mall.models import QA
from mall.serializers import QASerializer
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _


def read(**kwargs):
    query = kwargs.get('query')
    fields = kwargs.get('fields')
    id = query.get('id')
    if id:
        params = {
            'pk': id,
            'inactive': False,
        }
        qas = QA.objects.filter(**params).all()

        total = len(qas)
    else:
        start = query.get('start', 0)
        count = query.get('count', 24)
        qas = QA.objects.filter(inactive=False).order_by("-created")

        total = qas.count()
        qas = qas[start:start + count]

    qaData = [QASerializer(qa, fields=fields).data for qa in qas]

    return {
        "qas": qaData,
        "total": total,
    }


def update(qaId, **kwargs):

    question = kwargs.get('question')
    answer = kwargs.get('answer')

    qa = QA.objects.filter(pk=qaId).first()
    if not qa:
        raise ValidationError(_("The qa does not exist"))

    if question and question != qa.question:
        qa.question = question

    if answer and answer != qa.answer:
        qa.answer = answer

    qa.save()

    return qa.id


def create(**kwargs):
    question = kwargs.get('question')
    answer = kwargs.get('answer')
    creatorId = kwargs.get('creatorId')

    params = {
        "question": question,
        "answer": answer,
        "creatorId": creatorId,
    }

    qa = QA.objects.create(**params)
    return qa.id


def delete(qaId,  **kwargs):

    qa = QA.objects.filter(pk=qaId).all()
    if not qa:
        raise ValidationError(_("The qa does not exist"))

    qa.update(inactive=True)