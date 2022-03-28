from libs.models.general import COMPANY
from rest_framework import serializers


class COMPANYSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COMPANY
        fields = ['ID', 'NAME', 'AGE', 'ADDRESS','SALARY']

