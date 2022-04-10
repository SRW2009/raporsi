from django.urls import path

from app.views.admin_view import AdminLoginView, AdminSeedView, ListAdmin, CreateAdminView, UpdateDeleteAdminView
from app.views.divisi_view import ListDivisiView, CreateDivisiView, UpdateDeleteDivisiView
from app.views.grade_view import CreateGradeView, ListGrade, UpdateDeleteGradeView
from app.views.relation_view import CreateRelationView, ListRelation, UpdateDeleteRelationView
from app.views.student_view import ListStudent, CreateStudentView, UpdateDeleteStudentView
from app.views.subject_view import ListSubject, CreateSubjectView, UpdateDeleteSubjectView
from app.views.teacher_view import ListTeacher, CreateTeacherView, UpdateDeleteTeacherView

urlpatterns = [
    path('login/', AdminLoginView.as_view()),
    path('seed/', AdminSeedView.as_view()),
    path('divisi/<int:pk>', UpdateDeleteDivisiView.as_view()),
    path('divisi/', CreateDivisiView.as_view()),
    path('divisi', ListDivisiView.as_view()),
    path('teacher/', CreateTeacherView.as_view()),
    path('teacher', ListTeacher.as_view()),
    path('teacher/<int:pk>', UpdateDeleteTeacherView.as_view()),
    path('admin', ListAdmin.as_view()),
    path('admin/', CreateAdminView.as_view()),
    path('admin/<int:pk>', UpdateDeleteAdminView.as_view()),
    path('student', ListStudent.as_view()),
    path('student/', CreateStudentView.as_view()),
    path('student/<int:pk>', UpdateDeleteStudentView.as_view()),
    path('mapel', ListSubject.as_view()),
    path('mapel/', CreateSubjectView.as_view()),
    path('mapel/<int:pk>', UpdateDeleteSubjectView.as_view()),
    path('relation/', CreateRelationView.as_view()),
    path('relation', ListRelation.as_view()),
    path('relation/<int:pk>', UpdateDeleteRelationView.as_view()),
    path('nilai/', CreateGradeView.as_view()),
    path('nilai', ListGrade.as_view()),
    path('nilai/<int:pk>', UpdateDeleteGradeView.as_view()),
]
