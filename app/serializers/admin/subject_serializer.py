from rest_framework import serializers

from app.models import Admin, Divisi, Subject


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'name', 'is_block']


class ListSubjectSerializer(serializers.ModelSerializer):
    divisi_detail = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = ['id', 'name', 'abbreviation', 'divisi_detail', 'created_at','updated_at',
                  'deleted_at', 'created_by', 'updated_by', 'deleted_by']


    @staticmethod
    def get_divisi_detail(divisi_instance):
        try:
            adm = Divisi.objects.get(id=divisi_instance.divisi_id)
            return DivisiSerializer(adm).data
        except Exception as e:
            print(e)
            return {"id": "", "name": ""}

    @staticmethod
    def get_updated_by(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.updated_by_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_created_by(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.created_by_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_deleted_by(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.deleted_by_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}


class SubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=50)
    abbreviation = serializers.CharField(required=False, allow_null=True)
    divisi_id = serializers.IntegerField(required=True)

    class Meta:
        model = Subject
        fields = '__all__'