from django.urls import path

from app.views.teacher.grade_view import ListGrade, UpdateDeleteGradeView, CreateGradeView
from app.views.teacher.subject_view import ListSubject
from app.views.teacher.teacher_view import TeacherLoginView
from app.views.teacher.setting_view import ListSetting
from app.views.teacher.relation_view import ListRelation

urlpatterns = [
    path('login/', TeacherLoginView.as_view()),
    path('nilai', ListGrade.as_view()),
    path('mapel', ListSubject.as_view()),
    path('nilai/<int:pk>', UpdateDeleteGradeView.as_view()),
    path('nilai/', CreateGradeView.as_view()),
    path('setting', ListSetting.as_view()),
    path('relation', ListRelation.as_view()),
]