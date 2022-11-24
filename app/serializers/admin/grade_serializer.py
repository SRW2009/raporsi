from rest_framework import serializers

from app.models import Admin, Student, Teacher, Grade


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'nis']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']


class ListGradeSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    updated_by_admin = serializers.SerializerMethodField()
    created_by_admin = serializers.SerializerMethodField()
    deleted_by_admin = serializers.SerializerMethodField()

    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ['id', 'student','semester','year', 'is_observation', 'npb','nhb','nk', 'created_at', 'updated_at',
                  'deleted_at', 'created_by_admin', 'updated_by_admin', 'deleted_by_admin',
                  'created_by', 'updated_by', 'deleted_by']

    @staticmethod
    def get_student(student_instance):
        try:
            adm = Student.objects.get(id=student_instance.student_id)
            return StudentSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_updated_by_admin(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.updated_by_admin_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_created_by_admin(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.created_by_admin_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_deleted_by_admin(admin_instance):
        try:
            adm = Admin.objects.get(id=admin_instance.deleted_by_admin_id)
            return AdminSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_updated_by(teacher_instance):
        try:
            adm = Teacher.objects.get(id=teacher_instance.updated_by_id)
            return TeacherSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_created_by(teacher_instance):
        try:
            adm = Teacher.objects.get(id=teacher_instance.created_by_id)
            return TeacherSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}

    @staticmethod
    def get_deleted_by(teacher_instance):
        try:
            adm = Teacher.objects.get(id=teacher_instance.deleted_by_id)
            return TeacherSerializer(adm).data
        except Exception as e:
            return {"id": "", "name": ""}


class GradeSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(required=True)
    year = serializers.CharField(max_length=60, required=True)
    semester = serializers.CharField(max_length=60, required=True)
    is_observation = serializers.BooleanField(required=True)
    npb = serializers.JSONField()
    nhb = serializers.JSONField()
    nk = serializers.JSONField()
    class Meta:
        model = Grade
        fields = '__all__'