from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.views.generic import TemplateView, DetailView, View, CreateView
from django.contrib import messages
from django.urls import reverse
from app_admin.models import *
from .models import *
from .forms import *


# Create your views here.

class DashbordardView(TemplateView):
    template_name = "school_staf/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context

class StaffCourseView(View):
    template_name = "school_staf/gestion_cote/course.html"

    def get(self, request):
        context = {}
        #course_one = get_object_or_404(Course, pk=pk)
        staff_one = Staff.objects.get(admin=request.user)
        staff_course = staff_one.course_set.all()
        # print("Staff", staff_one)
        # print("Staff", staff_course)
        context['staff_course'] = staff_course
        return render(request, self.template_name,context)

def detail_course(request, course_id):
    context = {}
    staff_one = Staff.objects.get(admin=request.user)
    staff_course = staff_one.course_set.get(id=course_id)
    # get one class by staff course
    class_one = SchoolClass.objects.get(id=staff_course.school_class.id)

    # get all student by class
    student_by_class = class_one.student_set.all()
    # get cote by student
    cote_student = []
    stud_ok= []
    for stud in student_by_class:
        stud_ok.append(Student.objects.get(admin=stud.admin))

        #cote_student.append(Cotation.objects.filter(student=stud_ok))

        print('Ou sont les eleve par classe', cote_student)
    for s in stud_ok:
        cote_student.append(staff_course.cotation_set.filter(student=s))
        print("for note", cote_student)
    # cote_sutentd_final = []
    #
    # for c_s in cote_student:
    #     cote_sutentd_final.append(c_s)


    print("Voir eleve par note", cote_student)
    print("Voir tous les etudiants", student_by_class)
    print("Stp je peux voir la classe", class_one)
    # get all period
    periods = Period.objects.all()
    form = CotationForm(request.POST)
    context['form'] = form
    context['staff_one'] = staff_one
    context['staff_course'] = staff_course
    context['student_by_class'] = student_by_class
    context['periods'] = periods
    context['cote_student'] = cote_student
    if request.method == 'POST':
        if form.is_valid():

            note = form.cleaned_data.get('note')
            get_period = form.cleaned_data.get('period')
            get_student = form.cleaned_data.get('student')

            print("je peux voir l'id eleve", get_student)
            print("je peux voir l'id perion", get_period)

            # get object
            #get_p = Period.objects.get(id=get_period)
            #get_s = Student.objects.get(admin=get_student)


            cote = Cotation()
                # .objects.create(
                # note = note,
                # staff = staff_one,
                # student=get_s,
                # course=staff_course,
                # period = get_p
                #     )
            cote.note = note
            cote.staff = staff_one
            cote.student = get_student
            cote.course = staff_course
            cote.period = get_period
            cote.save()
            messages.success(request, f"Ccote add succefuly")


        else:
            messages.error(request, "Invalid Form Submitted ")
    #         return render(request, "hod_template/edit_session_template.html", context)




    return render(request, "school_staf/gestion_cote/cote.html", context)

