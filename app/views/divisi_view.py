from django.utils import timezone
from rest_framework import status, mixins
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Divisi
from app.serializers.divisi_serializer import ListDivisiSerializer, DivisiSerializer
from middleware.authentication import AdminAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class CreateDivisiView(generics.CreateAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = DivisiSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by_id'] = request.auth['id']
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"Divisi created successfully"}, status=status.HTTP_201_CREATED, headers=headers)


class ListDivisiView(generics.ListAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = ListDivisiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    queryset = Divisi.objects.filter(deleted_at__isnull=True)


class UpdateDeleteDivisiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [AdminAuthentication]
    serializer_class = DivisiSerializer
    queryset = Divisi.objects.filter(deleted_at__isnull=True)
    http_method_names = ['put', 'delete']

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['updated_by_id'] = request.auth['id']
        serializer.validated_data['updated_at'] = timezone.now()
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response({"message": "Divisi updated successfully"}, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_by_id = request.auth['id']
        instance.deleted_at = timezone.now()
        self.perform_destroy(instance)
        return Response({"message": "Divisi deleted successfully"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.save()
