from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from app.serializers.admin_serializer import AdminLoginSerializer, AdminSeed


class AdminLoginView(APIView):

    @staticmethod
    def post(self):
        serializer = AdminLoginSerializer(data=self.data)
        if serializer.is_valid():
            res = serializer.login()
            if "error" in str(res):
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminSeedView(APIView):
    @staticmethod
    def post(self):
        serializer = AdminSeed
        res = serializer.seed()
        return Response(res, status=status.HTTP_201_CREATED)
