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
        return f'({self.note})==> {self.course.name} {self.course.max}'
    
    
    # ajout 20-01-2023
    def get_cour_max10(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=1)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=1)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=1)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    def get_cour_max50(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=1)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    def get_cour_max100(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=1)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    
    # cotation 2 eme periode
    
    def get_cour_max10_p2(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=2)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20_p2(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=2)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40_p2(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=2)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max50_p2(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=2)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max100_p2(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=2)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    
    # cotation 3 eme periode examen 
    
    def get_cour_max10_p3(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=3)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20_p3(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=3)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40_p3(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=3)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max50_p3(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=3)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max100_p3(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=3)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    
    # cotation total periode 1
     
    def get_cour_max10_total_1(id_etudiant):
        list_total = []
        
        for co_object in Cotation.get_cour_max10(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max10_p2(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max10_p3(id_etudiant):
            list_total.append(co_object.note)
        return sum(list_total)
    
    def get_cour_max20_total_1(id_etudiant):
        list_total = []
        
        for co_object in Cotation.get_cour_max20(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max20_p2(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max20_p3(id_etudiant):
            list_total.append(co_object.note)
        return sum(list_total)
        
    
    def get_cour_max40_total_1(id_etudiant):
        dico={}
        list_total = []
        
        for co_object in Cotation.get_cour_max40(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max40_p2(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max40_p3(id_etudiant):
            list_total.append(co_object.note)
        
        return sum(list_total)
    
    # cotation 4 eme periode deuxieme semestre
    
    def get_cour_max10_p4(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=4)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20_p4(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=4)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40_p4(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=4)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max50_p4(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=4)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max100_p4(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=4)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    
    # cotation 5 eme periode deuxieme semestre
    
    def get_cour_max10_p5(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=5)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20_p5(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=5)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40_p5(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=5)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max50_p5(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=5)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max100_p5(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=5)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    
    # cotation 6 eme periode deuxieme semestre
    
    def get_cour_max10_p6(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=6)
        for ob in objet_cotation:
            if(ob.course.max==10):
                dico[ob]=ob.period
        return dico
        
    def get_cour_max20_p6(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=6)
        for ob in objet_cotation:
            if(ob.course.max==20):
                dico[ob]=ob.period
        return dico
    
    def get_cour_max40_p6(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=6)
        for ob in objet_cotation:
            if(ob.course.max==40):
                dico[ob]=ob.period
        return dico
    def get_cour_max50_p6(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=6)
        for ob in objet_cotation:
            if(ob.course.max==50):
                dico[ob]=ob.period
        return dico
    def get_cour_max100_p6(id_etudiant):
        dico={}
        
        objet_cotation=Cotation.objects.filter(student=id_etudiant,period=6)
        for ob in objet_cotation:
            if(ob.course.max==100):
                dico[ob]=ob.period
        return dico
    # partie total 2 semetre
    
    def get_cour_max10_total_2(id_etudiant):
        dico={}
        list_total = []
        
        for co_object in Cotation.get_cour_max10_p4(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max10_p5(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max10_p6(id_etudiant):
            list_total.append(co_object.note)
        
        return sum(list_total)
    
    def get_cour_max20_total_2(id_etudiant):
        dico={}
        list_total = []
        
        for co_object in Cotation.get_cour_max20_p4(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max20_p5(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max20_p6(id_etudiant):
            list_total.append(co_object.note)
        
        return sum(list_total)
    
    def get_cour_max40_total_2(id_etudiant):
        dico={}
        list_total = []
        
        for co_object in Cotation.get_cour_max40_p4(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max40_p5(id_etudiant):
            list_total.append(co_object.note)
        for co_object in Cotation.get_cour_max40_p6(id_etudiant):
            list_total.append(co_object.note)
        
        return sum(list_total)
    
    
    # fin ajout 


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