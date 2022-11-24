from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from app.models import Setting
from app.serializers.teacher.setting_serializer import ListSettingSerializer
from middleware.authentication import TeacherAuthentication

class ListSetting(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','variable']
    authentication_classes = [TeacherAuthentication]
    queryset = Setting.objects.filter(deleted_at__isnull=True)
    serializer_class = ListSettingSerializer

