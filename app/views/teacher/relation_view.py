from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from app.models import Relation
from app.serializers.teacher.relation_serializer import ListRelationSerializer
from middleware.authentication import TeacherAuthentication


class ListRelation(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','id','teacher_id']
    authentication_classes = [TeacherAuthentication]
    queryset = Relation.objects.filter(deleted_at__isnull=True)
    serializer_class = ListRelationSerializer
