from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from app.models import Subject
from app.serializers.teacher.subject_serializer import ListSubjectSerializer
from middleware.authentication import TeacherAuthentication


class ListSubject(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','id']
    authentication_classes = [TeacherAuthentication]
    queryset = Subject.objects.filter(deleted_at__isnull=True)
    serializer_class = ListSubjectSerializer
