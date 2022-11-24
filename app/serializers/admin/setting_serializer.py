from rest_framework import serializers

from app.models import Admin, Setting


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class ListSettingSerializer(serializers.ModelSerializer):
    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    class Meta:
        model = Setting
        fields = ['id', 'variable', 'value', 
                  'created_at', 'updated_at', 'deleted_at', 
                  'created_by', 'updated_by', 'deleted_by']

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


class SettingSerializer(serializers.ModelSerializer):
    variable = serializers.CharField(max_length=80, required=True)
    value = serializers.JSONField()
    class Meta:
        model = Setting
        fields = '__all__'