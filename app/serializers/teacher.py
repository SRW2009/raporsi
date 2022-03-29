import jwt

from app.helper.response import SerializerHelper as HLog
from rest_framework import serializers

from app.models import Admin, Divisi, Teacher
from raporsi.settings import SECRET_KEY


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id','name']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id','name']


class AllTeacherSerializer(serializers.Serializer):
    divisi_detail = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'password', 'is_leader', 'divisi_detail']

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
    password = serializers.CharField(required=True, max_length=30)
    is_leader = serializers.BooleanField(required=True)
    divisi = serializers.IntegerField(required=True)

    def create(self, validated_data):
        t = Teacher.objects.create(**validated_data)
        encoded_jwt = jwt.encode({"password": t.password}, SECRET_KEY, algorithm="HS256")
        t.password = encoded_jwt
        t.save()


