from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers.teacher.teacher_serializer import TeacherLoginSerializer
from rest_framework import status


class TeacherLoginView(APIView):

    @staticmethod
    def post(self):
        serializer = TeacherLoginSerializer(data=self.data)
        if serializer.is_valid():
            res = serializer.login()
            if "error" in str(res):
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)