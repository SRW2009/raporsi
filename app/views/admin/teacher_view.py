import jwt
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from app.models import Teacher, Divisi
from app.serializers.admin.teacher_serializer import TeacherSerializer, ListTeacherSerializer
from middleware.authentication import AdminAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from raporsi.settings import SECRET_KEY


class CreateTeacherView(generics.CreateAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by_id'] = request.auth['id']
        serializer.validated_data['password'] = jwt.encode({"password": serializer.validated_data['password']}, SECRET_KEY, algorithm="HS256")
        try:
            Divisi.objects.get(id=serializer.validated_data['divisi_id'], deleted_at__isnull=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"message":"Teacher created successfully"}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ListTeacher(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email','name','id']
    authentication_classes = [AdminAuthentication]
    queryset = Teacher.objects.filter(deleted_at__isnull=True)
    serializer_class = ListTeacherSerializer


class UpdateDeleteTeacherView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.filter(deleted_at__isnull=True)
    http_method_names = ['put', 'delete']

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['updated_by_id'] = request.auth['id']
        serializer.validated_data['updated_at'] = timezone.now()
        serializer.validated_data['password'] = jwt.encode({"password": serializer.validated_data['password']},
                                                           SECRET_KEY, algorithm="HS256")
        try:
            Divisi.objects.get(id=serializer.validated_data['divisi_id'], deleted_at__isnull=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            print("koala")
            return Response({"message": "Teacher updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_by_id = request.auth['id']
        instance.deleted_at = timezone.now()
        self.perform_destroy(instance)
        return Response({"message": "Teacher deleted successfully"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.save()
