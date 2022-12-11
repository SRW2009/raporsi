from rest_framework import serializers

from app.models import Subject, Divisi


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'name', 'is_block']


class ListSubjectSerializer(serializers.ModelSerializer):
    divisi_detail = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'abbreviation', 'divisi_detail']


    @staticmethod
    def get_divisi_detail(divisi_instance):
        try:
            adm = Divisi.objects.get(id=divisi_instance.divisi_id)
            return DivisiSerializer(adm).data
        except Exception as e:
            print(e)
            return {"id": "", "name": ""}