from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True, unique=True)
    password = models.CharField(max_length=360, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey("self", related_name='admin_admin_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey("self", related_name='admin_admin_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey("self", related_name='admin_admin_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)


class Divisi(models.Model):
    name = models.CharField(max_length=30)
    is_block = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_divisi_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_divisi_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_divisi_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s=" % self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(max_length=360, blank=True, null=True)
    divisi = models.ForeignKey(Divisi, blank=True, null=True, on_delete=models.SET_NULL)
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_teacher_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_teacher_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_teacher_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)


class Subject(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    divisi = models.ForeignKey(Divisi, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_subject_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_subject_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_subject_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s - %s" % (self.name, self.divisi.name)


class Student(models.Model):
    nis = models.CharField(max_length=20, blank=True, null=True, unique=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_student_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_student_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_student_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s - %s" % (self.nis, self.name)


class Relation(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_relation_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_relation_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_relation_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s - %s" % self.student.name, self.teacher.name


class Grade(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    semester = models.CharField(max_length=60, blank=True, null=True)
    year = models.CharField(max_length=60, blank=True, null=True)
    is_observation = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Teacher, related_name='teacher_grade_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Teacher, related_name='teacher_grade_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Teacher, related_name='teacher_grade_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    created_by_admin = models.ForeignKey(Admin, related_name='admin_grade_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by_admin = models.ForeignKey(Admin, related_name='admin_grade_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by_admin = models.ForeignKey(Admin, related_name='admin_grade_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    npb = JSONField()
    nhb = JSONField()
    nk = JSONField()

    def __str__(self):
        return "%s - %s" % (self.student.name, self.semester)


class OauthAdmin(models.Model):
    admin = models.ForeignKey(Admin, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=360, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.admin.name, self.token)


class OauthTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=360, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.teacher.name, self.token)


class Log(models.Model):
    case = JSONField()
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Setting(models.Model):
    variable = models.CharField(max_length=80)
    value = JSONField()
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Admin, related_name='admin_setting_created_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Admin, related_name='admin_setting_updated_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(Admin, related_name='admin_setting_deleted_at', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "%s : %s" % (self.variable, self.value)
