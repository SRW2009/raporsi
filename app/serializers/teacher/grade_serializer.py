from rest_framework import serializers

from app.models import Grade, Student, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'nis']


class ListGradeSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ['id', 'student','semester','year', 'is_observation', 'npb','nhb','nk']

    @staticmethod
    def get_student(student_instance):
        try:
            adm = Student.objects.get(id=student_instance.student_id)
            return StudentSerializer(adm).data
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