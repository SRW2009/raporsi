from django.urls import path

from app.views.admin_view import AdminLoginView, AdminSeedView
from app.views.divisi_view import ListDivisiView, CreateDivisiView, UpdateDeleteDivisiView

urlpatterns = [
    path('login/', AdminLoginView.as_view()),
    path('seed/', AdminSeedView.as_view()),
    path('divisi/<int:pk>', UpdateDeleteDivisiView.as_view()),
    path('divisi/', CreateDivisiView.as_view()),
    path('divisi', ListDivisiView.as_view()),
    # path('teacher/', TeacherView.as_view()),
    # path('teacher', GetAllTeacher.as_view()),
]
