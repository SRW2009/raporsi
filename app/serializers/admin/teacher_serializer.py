import jwt
from rest_framework import serializers
from app.models import Admin, Divisi, Teacher
from raporsi.settings import SECRET_KEY


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'name', 'is_block']


class ListTeacherSerializer(serializers.ModelSerializer):
    divisi_detail = serializers.SerializerMethodField()
    divisi_block_detail = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'password', 'is_leader', 'divisi_detail', 'divisi_block_detail', 'created_at','updated_at',
                  'deleted_at', 'created_by', 'updated_by', 'deleted_by']

    @staticmethod
    def get_password(teacher_instance):
        try:
            password = jwt.decode(teacher_instance.password, SECRET_KEY, algorithms=["HS256"])
            return password['password']
        except Exception as e:
            return str(e)

    @staticmethod
    def get_divisi_detail(divisi_instance):
        try:
            div = Divisi.objects.get(id=divisi_instance.divisi_id)
            return DivisiSerializer(div).data
        except Exception as e:
            print(e)
            return {"id": "", "name": ""}

    @staticmethod
    def get_divisi_block_detail(divisi_block_instance):
        try:
            if (divisi_block_instance.divisi_block_id == None): return None
            div = Divisi.objects.get(id=divisi_block_instance.divisi_block_id)
            return DivisiSerializer(div).data
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


class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=50)
    password = serializers.CharField(max_length=360, required=True)
    is_leader = serializers.BooleanField(required=True)
    divisi_id = serializers.IntegerField(required=True)
    divisi_block_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = Teacher
        fields = '__all__'