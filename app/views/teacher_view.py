from rest_framework import generics
from app.models import Teacher
from app.serializers.teacher_serializer import TeacherSerializer, AllTeacherSerializer
from middleware.authentication import AdminAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class TeacherView(generics.CreateAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        admin_id = self.request.auth['id']
        serializer.create(admin_id)


class GetAllTeacher(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email','name','id']
    authentication_classes = [AdminAuthentication]
    queryset = Teacher.objects.all()
    serializer_class = AllTeacherSerializer