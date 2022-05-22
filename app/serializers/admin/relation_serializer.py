from rest_framework import serializers

from app.models import Admin, Student, Teacher, Relation


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','nis']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']


class ListRelationSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    class Meta:
        model = Relation
        fields = ['id', 'teacher', 'student','name', 'is_active', 'created_at', 'updated_at',
                  'deleted_at', 'created_by', 'updated_by', 'deleted_by']

    @staticmethod
    def get_teacher(teacher_instance):
        try:
            adm = Teacher.objects.get(id=teacher_instance.teacher_id)
            return TeacherSerializer(adm).data
        except Exception as e:
            print(e)
            return {"id": "", "name": ""}

    @staticmethod
    def get_student(student_instance):
        try:
            adm = Student.objects.get(id=student_instance.student_id)
            return StudentSerializer(adm).data
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


class RelationSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(required=True)
    teacher_id = serializers.IntegerField(required=True)
    is_active = serializers.BooleanField(required=True)
    name = serializers.CharField(max_length=60, required=True)

    class Meta:
        model = Relation
        fields = '__all__'
