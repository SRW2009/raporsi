import time
from rest_framework import serializers
import jwt

from app.helper.response import SerializerHelper as HLog
from app.models import Admin, OauthAdmin
from raporsi.settings import SECRET_KEY


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=120, required=True)

    def login(self):
        activity = "Login Admin"
        email = self.data['email']
        try:
            a = Admin.objects.get(email=email)
        except Exception as e:
            HLog.create_log(email, activity, False, str(e))
            return {"message": "Login failed", "error": str(e)}

        password = jwt.decode(a.password, SECRET_KEY, algorithms=["HS256"])
        if self.data['password'] != password['password']:
            HLog.create_log(email, activity, False, "password not match")
            return {"message": "Login failed", "error": "password not match"}
        encoded_jwt = jwt.encode({"id": a.id, "email": a.email, "time": time.time()}, SECRET_KEY, algorithm="HS256")
        OauthAdmin.objects.create(admin_id=a.id, token=encoded_jwt)
        HLog.create_log(email, activity, True, "Login success")
        return {"message": "success", "data": {"id": a.id, "email": a.email, "token":encoded_jwt}}


class AdminSeed(serializers.Serializer):
    @staticmethod
    def seed():
        activity = "Seed Admin"
        try:
            a = Admin.objects.get(email="koala@panda.com")
            return {"message": "super admin already registered"}
        except Exception as e:
            print(e)
            HLog.create_log("koala@panda.com", activity, True, "SU successfully created")
            encoded_password = jwt.encode({"password": "koala_panda"}, SECRET_KEY, algorithm="HS256")
            Admin.objects.create(email="koala@panda.com", name='koala panda', password=encoded_password)
        return{"message": "super admin created"}
