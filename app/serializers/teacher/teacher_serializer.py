import jwt
from rest_framework import serializers

from app.models import Teacher, OauthTeacher
from raporsi.settings import SECRET_KEY
import time


class TeacherLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=120, required=True)

    def login(self):
        activity = "Login Teacher"
        email = self.data['email']
        try:
            a = Teacher.objects.get(email=email)
        except Exception as e:
            return {"message": "Login failed", "error": str(e)}

        password = jwt.decode(a.password, SECRET_KEY, algorithms=["HS256"])
        if self.data['password'] != password['password']:
            return {"message": "Login failed", "error": "password not match"}
        encoded_jwt = jwt.encode({"id": a.id, "email": a.email, "time": time.time()}, SECRET_KEY, algorithm="HS256")
        OauthTeacher.objects.create(teacher_id=a.id, token=encoded_jwt)
        return {"message": "success", "data": {"id": a.id, "email": a.email, "token":encoded_jwt}}