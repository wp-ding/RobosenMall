from libs.models.general_model import COMPANY
from rest_framework import serializers


class COMPANYSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COMPANY
        fields = ['ID', 'NAME', 'AGE', 'ADDRESS','SALARY']

