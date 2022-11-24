from rest_framework import serializers

from app.models import Admin, Setting


class ListSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = ['id', 'variable', 'value']
