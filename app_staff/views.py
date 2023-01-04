from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.core.files.storage import FileSystemStorage

from django.views.generic import TemplateView, DetailView, View, CreateView
from django.contrib import messages
from django.urls import reverse
from app_admin.models import *
from app_admin.forms import *
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
    course_id = int(course_id)
    context = {}
    staff_one = Staff.objects.get(admin=request.user)
    try:
        # get one class by staff course
        staff_course = staff_one.course_set.get(id=course_id)

    except Course.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('staff_all_course')

    # get all class for staff
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
        note = request.POST['note']
        get_period = request.POST['period']
        get_student = request.POST['student']
        print("Ou est l'eleve???", get_student)

        # print("je peux voir l'id eleve", get_student)
        # print("je peux voir l'id perion", get_period)

        # get object by id
        get_p = Period.objects.get(id=get_period)
        get_s = Student.objects.get(id=get_student)
        # affect this value
        cote = Cotation()
        cote.note = note
        cote.staff = staff_one
        cote.student = get_s
        cote.course = staff_course
        cote.period = get_p
        # save cote
        cote.save()
        messages.success(request, f"Ccote add succefuly")

    else:
        messages.error(request, "Invalid Form Submitted ")

    return render(request, "school_staf/gestion_cote/cote.html", context)

# add profile admin
def staff_view_profile(request):
    staff = get_object_or_404(Staff, admin=request.user)
    form = StaffForm(request.POST or None, request.FILES or None,
                     instance=staff)
    context = {'form': form,
               'page_title': 'View/Edit Profile'
               }
    if request.method == 'POST':
        try:
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                address = form.cleaned_data.get('address')
                password = form.cleaned_data.get('password') or None
                passport = request.FILES.get('profile_pic') or None
                custom_user = staff.admin
                if password != None:
                    custom_user.set_password(password)
                if passport != None:
                    fs = FileSystemStorage()
                    filename = fs.save(passport.name, passport)
                    passport_url = fs.url(filename)
                    custom_user.profile_pic = passport_url
                custom_user.first_name = first_name
                custom_user.last_name = last_name
                custom_user.address = address
                custom_user.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('profile_staff'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occured While Updating Profile " + str(e))
    return render(request, "school_staf/profile.html", context)

