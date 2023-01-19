from django.db import models
from app_admin.models import *
import uuid

# Create your models here.


class Participation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    #name = models.CharField(max_length=120)
    staff = models.ManyToManyField(Staff)
    course = models.ManyToManyField(Course)
    period = models.ManyToManyField(Period)
    school_class = models.ManyToManyField(SchoolClass)
    #school_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_staff(self):
        return self.staff.all()#.order_by('id').values_list('admin','role')

    def get_school_class(self):
        return self.school_class.all().values_list('class_name')

    def get_student_class(self):
        return self.school_class.all().values_list('student')

    def get_course(self):
        return self.course.all().values_list('name')

    def get_course_cotation(self):
        return self.course.all().values_list('cotation')

    def get_period(self):
        return self.period.all().order_by('id').values_list('period_name')

    # def __str__(self):
    #     return self.staff+" " +self.course


# cote
class Cotation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    period = models.ForeignKey(Period, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'self.note'


class Comportement(models.Model):
    

    CONDUITE_TYPE = [("impoli", "Impoli"), ("poli", "Poli")]
    DECITION_TYPE = [("passe", "Passe"), ("echouer", "Echouer")]
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    period = models.ForeignKey(Period, on_delete=models.DO_NOTHING)
    conduite = models.CharField(max_length=30, choices=CONDUITE_TYPE)
    decision = models.CharField(max_length=30, choices=DECITION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)