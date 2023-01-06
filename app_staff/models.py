from django.db import models
from app_admin.models import *


# Create your models here.

class Participation(models.Model):
    name = models.CharField(max_length=120)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    period = models.ForeignKey(Period, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# cote

class Cotation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    period = models.ForeignKey(Period, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

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

