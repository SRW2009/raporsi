from rest_framework import serializers

from app.models import Student, Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class ListStudentSerializer(serializers.ModelSerializer):
    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id','nis', 'name', 'created_at','updated_at',
                  'deleted_at', 'created_by', 'updated_by', 'deleted_by']

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


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=50)
    nis = serializers.CharField(required=True, max_length=50)
    class Meta:
        model = Student
        fields = '__all__'