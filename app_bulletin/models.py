from django.db import models
from app_staff.models import Cotation, Comportement
from app_admin.models import SchoolClass

# Create your models here.

# bulletin is a rapport for student

class Bulletin(models.Model):
    cote = models.ForeignKey(Cotation, on_delete=models.DO_NOTHING)
    comportement = models.ForeignKey(Comportement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


