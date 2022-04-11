from rest_framework import serializers

from app.models import Student


class ListStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','nis', 'name']
