from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers.divisi import DivisiSerializer
from middleware.authentication import AdminAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class DivisiView(APIView):
    authentication_classes = [AdminAuthentication]
    filter_backends = [DjangoFilterBackend]
    @staticmethod
    def post(request):
        serializer = DivisiSerializer(data=request.data)
        if serializer.is_valid():
            admin_id = request.auth['id']
            res = serializer.create(admin_id)
            if "error" in str(res):
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, id):
        serializer = DivisiSerializer(data=request.data)
        if serializer.is_valid():
            print(id)
            admin_id = request.auth['id']
            res = serializer.update(id, admin_id)
            if "error" in str(res):
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, id):
        serializer = DivisiSerializer
        admin_id = request.auth['id']
        res = serializer.delete(id, admin_id)
        if "error" in str(res):
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request):
        admin_id = request.auth['id']
        serializer = DivisiSerializer
        try:
            id = request.query_params['id']
        except:
            id = ""
        try:
            name = request.query_params['name']
        except:
            name=""
        res = serializer.get(admin_id,id,name)
        if "error" in str(res):
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res, status=status.HTTP_200_OK)

    # @staticmethod
    # def filter(request):
    #     admin_id = request.auth['id']
    #     id = request.query_params['id']
    #     name = request.query_params['name']
    #     serializer = DivisiSerializer
    #     res = serializer.filter(admin_id, id, name)
    #     if "error" in str(res):
    #         return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     return Response(res, status=status.HTTP_200_OK)