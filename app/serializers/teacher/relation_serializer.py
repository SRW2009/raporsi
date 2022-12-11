from rest_framework import serializers

from app.models import Student, Teacher, Relation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'nis']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']


class ListRelationSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()

    class Meta:
        model = Relation
        fields = ['id', 'teacher', 'student', 'name', 'is_active']

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
