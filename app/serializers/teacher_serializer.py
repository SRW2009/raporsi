import jwt
from django.utils import timezone

from rest_framework import exceptions
from app.helper.response import SerializerHelper as HLog
from rest_framework import serializers
from django.db import transaction
from app.models import Admin, Divisi, Teacher
from raporsi.settings import SECRET_KEY


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'name']


class AllTeacherSerializer(serializers.ModelSerializer):
    divisi_detail = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'is_leader', 'divisi_detail']

    @staticmethod
    def get_divisi_detail(divisi_instance):
        try:
            adm = Divisi.objects.get(id=divisi_instance.divisi_id)
            return AdminSerializer(adm).data
        except Exception as e:
            print(e)
            return {"id": "", "name": ""}


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=50)
    password = serializers.CharField(max_length=30, required=True)
    is_leader = serializers.BooleanField(required=True)
    divisi_id = serializers.IntegerField(required=True)

    def create(self, admin_id):
        activity = 'Create Teacher'
        try:
            Divisi.objects.get(id=self.data['divisi_id'])
            with transaction.atomic():
                t = Teacher.objects.create(name=self.data['name'], email=self.data['email'],
                                           is_leader=self.data['is_leader'], divisi_id=self.data['divisi_id'])
                t.created_by_id = admin_id
                encoded_jwt = jwt.encode({"password": self.data['password']}, SECRET_KEY, algorithm="HS256")
                t.password = encoded_jwt
                t.save()
        except Exception as e:
            pass
            HLog.create_log(admin_id, activity, False, str(e))
            raise exceptions.APIException(str(e))
        pass
        HLog.create_log(admin_id, activity, True, "Teacher successfully created")
    #
    # def update(self, teacher_id, admin_id):
    #     activity = 'Update Teacher'
    #     try:
    #         t = Teacher.objects.get(id=teacher_id, deleted_at__isnull=True)
    #         Divisi.objects.get(id=self.data['divisi_id'])
    #         with transaction.atomic():
    #             t.name = self.data['name']
    #             t.email = self.data['email']
    #             if self.data['password'] != t.password:
    #                 t.password = jwt.encode({"password": self.data['password']}, SECRET_KEY, algorithm="HS256")
    #             t.is_leader = self.data['is_leader']
    #             t.divisi_id = self.data['divisi_id']
    #             t.updated_at = timezone.now()
    #             t.updated_by_id = admin_id
    #             t.save()
    #     except Exception as e:
    #         pass
    #         HLog.create_log(admin_id, activity, False, str(e))
    #         return {"error": str(e)}
    #     pass
    #     HLog.create_log(admin_id, activity, True, "Teacher updated successfully")
    #     return{"message": "Teacher updated successfully"}
    #
    # @staticmethod
    # def delete(teacher_id, admin_id):
    #     activity = 'Delete Teacher'
    #     try:
    #         t = Teacher.objects.get(id=teacher_id, deleted_at__isnull=True)
    #         with transaction.atomic():
    #             t.deleted_at = timezone.now()
    #             t.deleted_by_id = admin_id
    #             t.save()
    #     except Exception as e:
    #         pass
    #         HLog.create_log(admin_id, activity, False, str(e))
    #         return {"error": str(e)}
    #     pass
    #     HLog.create_log(admin_id, activity, True, "Teacher deleted successfully")
    #     return{"message": "Teacher deleted successfully"}
