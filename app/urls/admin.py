from django.urls import path

from app.views.admin import AdminLoginView, AdminSeedView
from app.views.divisi import DivisiView

urlpatterns = [
    path('login/', AdminLoginView.as_view()),
    path('seed/', AdminSeedView.as_view()),
    path('divisi/', DivisiView.as_view()),
    path('divisi/<int:id>', DivisiView.as_view()),
]
