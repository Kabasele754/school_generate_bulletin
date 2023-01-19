from django.db import models
from app_staff.models import Cotation, Comportement
from app_admin.models import SchoolClass, Student, Admin
import uuid

# Create your models here.

# bulletin is a rapport for student

class Bulletin(models.Model):
    CONDUITE_TYPE = [("impoli", "Impoli"), ("poli", "Poli")]
    DECITION_TYPE = [("passe", "Passe"), ("echouer", "Echouer")]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    conduite = models.CharField(max_length=30, choices=CONDUITE_TYPE)
    decision = models.CharField(max_length=30, choices=DECITION_TYPE)
    
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
     
   


