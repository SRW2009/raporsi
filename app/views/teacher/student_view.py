from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from app.models import Student
from app.serializers.teacher.student_serializer import ListStudentSerializer
from middleware.authentication import TeacherAuthentication


class ListStudent(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nis','name','id']
    authentication_classes = [TeacherAuthentication]
    queryset = Student.objects.filter(deleted_at__isnull=True)
    serializer_class = ListStudentSerializer
