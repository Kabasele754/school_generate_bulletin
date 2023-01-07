import json
import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.messages.views import SuccessMessageMixin # get the in add edit
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from .forms import *
from .models import *
from app_public.models import *
from app_staff.models import *
from app_staff.forms import *

from django.views.generic import TemplateView, DetailView, View, CreateView
# impoertation send mail
from django.conf import settings
from django.core.mail import send_mail
import datetime


# Create your views here.

class DashbordardView(TemplateView):
    template_name = "school_admin/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context


#add School year function

class SchoolYearView(View):
    model = SchoolYear
    success_msg = 'Category created.'
    form_class = SchoolYearForm
    template_name = "school_admin/gestion_school/school.html"

    def get(self, request, *args, **kwargs):
        context = {}
        form_school = self.form_class
        all_year = SchoolYear.objects.all()
        context['form'] = form_school
        context['all_year'] = all_year
        return render(request, self.template_name , context)

    # create a post for show one and to make a comment
    def post(self, request):
        school_form = self.form_class(request.POST)
        context = {'form': school_form, 'page_title': 'Ajouter Categorie'}
        if request.method == 'POST':
            if school_form.is_valid():
                start_year = school_form.cleaned_data.get('start_year')
                end_year = school_form.cleaned_data.get('end_year')
                try:
                    obj_school = SchoolYear.objects.create(
                         start_year=start_year,
                        end_year=end_year
                        )
                    if obj_school == "":
                        messages.error(request, "Ne peut etre ajouté: ")
                    else:
                        obj_school.save()
                    messages.success(request, f"Vous avez ajouté category  avec succé")
                    return redirect(reverse('year'))
                except Exception as e:
                    messages.error(request, f" ne peut etre ajouté : " + str(e))
            else:
                form = SchoolClassForm()
                messages.error(request, "Ne peut etre ajouté: ")
                context['form'] = form
        return render(request, self.template_name, context)

def edit_school_year(request, sch_year_id):
    sch_year_id = int(sch_year_id)
    try:
        sch_year = SchoolYear.objects.get(id = sch_year_id)

    except SchoolYear.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('book')
    form = SchoolYearForm(request.POST or None, instance=sch_year)
    context = {
        'form': form,
        'sch_year': sch_year,
        'page_title': 'Edit School year'
    }
    if request.method == 'POST':
        if form.is_valid():
            start_year = form.cleaned_data.get('start_year')
            end_year = form.cleaned_data.get('end_year')
            # school_class = form.cleaned_data.get('school_class')
            # staff = form.cleaned_data.get('staff')
            try:
                school = SchoolYear.objects.get(id=sch_year_id)
                school.start_year = start_year
                school.end_year = end_year
                # course.school_class = school_class
                # course.staff = staff
                school.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'school_admin/gestion_school/edit_school.html', context)
# add period function
class PeriodView(View):
    model = Period
    success_msg = 'Category created.'
    form_class = PeriodForm
    template_name = "school_admin/gestion_school/period.html"

    def get(self, request, *args, **kwargs):
        context = {}
        form_period = self.form_class
        all_period = self.model.objects.all()
        context['form'] = form_period
        context['all_period'] = all_period
        return render(request, self.template_name , context)

    # create a post for show one and to make a comment
    def post(self, request):
        period_form = self.form_class(request.POST)
        context = {'form': period_form, 'page_title': 'Ajouter Categorie'}
        if request.method == 'POST':
            if period_form.is_valid():
                period_name = period_form.cleaned_data.get('period_name')
                period_num = period_form.cleaned_data.get('period_num')
                year_school = period_form.cleaned_data.get('year_school')
                try:
                    obj_period = Period.objects.create(
                         period_name=period_name,
                        period_num=period_num,
                        year_school=year_school

                        )
                    if obj_period == "":
                        messages.error(request, "Ne peut etre ajouté: ")
                    else:
                        obj_period.save()
                    messages.success(request, f"Vous avez ajouté period  avec succé")
                    return redirect(reverse('period'))
                except Exception as e:
                    messages.error(request, f" ne peut etre ajouté : " + str(e))
            else:
                form = PeriodForm()
                messages.error(request, "Ne peut etre ajouté: ")
                context['form'] = form
        return render(request, self.template_name, context)
# update category
def edit_period(request, periode_id):

    periode_id = int(periode_id)
    try:
        period_one = Period.objects.get(id=periode_id)

    except Period.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('period')
    period_form = PeriodForm(request.POST or None, instance=period_one)
    context = {
        'form': period_form,
        'period_one': period_one,
        'page_title': 'Edit Course'
    }
    if request.method == 'POST':
        if period_form.is_valid():
            period_name = period_form.cleaned_data.get('period_name')
            period_num = period_form.cleaned_data.get('period_num')
            year_school = period_form.cleaned_data.get('year_school')
            try:
                period = Period.objects.get(id=period_one)
                period.period_name = period_name
                period.period_num = period_num
                period.year_school = year_school
                period.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'school_admin/gestion_school/edit_period.html', context)

# end period
# Begin gestion student

class StudentView(View):
    model = Student
    template_name = "school_admin/gestion_student/student.html"
    form_class = StudentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        students = Student.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'studs': students })

    def post(self, request):
        form = StudentForm(request.POST or None, request.FILES or None)
        context = {'form': form, 'page_title': 'Add Student'}
        if request.method == 'POST':
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                address = form.cleaned_data.get('address')
                email = form.cleaned_data.get('email')
                gender = form.cleaned_data.get('gender')
                password = form.cleaned_data.get('password')
                school_class = form.cleaned_data.get('school_class')
                student_num = form.cleaned_data.get('student_num')
                passport = request.FILES.get('profile_pic')
                fs = FileSystemStorage()
                # filename = fs.save(passport.name, passport)
                # passport_url = fs.url(filename)
                try:
                    user = User.objects.create_user(
                        email=email, password=password, user_type=3, first_name=first_name, last_name=last_name,
                        profile_pic=passport)
                    user.gender = gender
                    user.address = address
                    user.student.school_class = school_class
                    user.student.student_num = student_num
                    user.save()

                    messages.success(request, "Successfully Added")
                    return redirect(reverse('student'))

                except Exception as e:
                    messages.error(request, "Could Not Add " + str(e))
            else:
                messages.error(request, "Please fulfil all requirements")

        return render(request, self.template_name, context)

def edit_student(request, student_id):
    student_id = int(student_id)
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('student')
    form = StudentForm(request.POST or None, instance=student)
    #cour_student = []

    #for sud in student:
    cour_student = student.school_class.course_set.all()
    cote_student = student.cotation_set.all()

    print("svp can I see course student", cour_student)
    print("svp can I see cotation student", cote_student)
    context = {
        'form': form,
        'student': student,
        'page_title': 'Edit Student'
    }
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password') or None
            school_class = form.cleaned_data.get('school_class')
            student_num = form.cleaned_data.get('student_num')
            passport = request.FILES.get('profile_pic') or None
            try:
                user = User.objects.get(id=student.admin.id)
                if passport != None:
                    fs = FileSystemStorage()
                    filename = fs.save(passport.name, passport)
                    passport_url = fs.url(filename)
                    user.profile_pic = passport_url
                user.username = username
                user.email = email
                if password != None:
                    user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                student.school_class = school_class
                student.student_num = student_num
                user.save()
                student.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_student', args=[student_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "school_admin/gestion_student/edit_student.html", context)


# detail student
def detail_student(request, student_id):
    student_id = int(student_id)
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('student')
    form = StudentForm(request.POST or None, instance=student)
    # cour_student = []

    # for sud in student:
    cour_student = student.school_class.course_set.all()
    cote_student = student.cotation_set.all()

    print("svp can I see course student", cour_student)
    print("svp can I see cotation student", cote_student)
    context = {
        'form': form,
        'student': student,
        'cote_student': cote_student
    }

    return render(request, "school_admin/gestion_student/cote_bulletin_student.html", context)

# generate
def generate_bulletin(request):
    context = {}
    # course class
    all_class = SchoolClass.objects.all()

    all_student_by_class = all_class.student_set.all()

    course_cl = all_student_by_class.course_set.all()

    # student course
    context['course_cl'] = course_cl
    return render(request, "school_admin/gestion_class/generate_bulletin.html", context)

class CotationStudentView(View):
    model = Cotation
    template_name = "school_admin/gestion_student/cote_student.html"
    form_class = ComportementForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        cotes = self.model.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'cotes': cotes })

    def post(self, request):
        form = ComportementForm(request.POST or None, request.FILES or None)
        context = {'form': form, 'page_title': 'Add Comportement'}
        if request.method == 'POST':
            period = request.POST['period']
            student = request.POST['student']
            conduite = request.POST['conduite']
            decision = request.POST['decision']
            print("See PK Student", student)

            # get object id student and period
            get_period = Period.objects.get(id=period)
            get_student = Student.objects.get(id=student)

            # get_p = Period.objects.get(id=get_period)
            # get_s = Student.objects.get(id=get_student)

            try:
                comportement = Comportement()
                comportement.student=get_student
                comportement.period=get_period
                comportement.conduite=conduite
                comportement.decision=decision

                comportement.save()

                messages.success(request, "Successfully Added")
                return redirect(reverse('student'))

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

        return render(request, self.template_name, context)


def cote_student(request, template_name = "school_admin/gestion_student/cote_student.html"):
    context = {}

    cotes = Cotation.objects.all()
    context['cotes'] = cotes

    context['page_title'] = 'Add Comportement'
    if request.method == 'POST':
        period = request.POST['period']
        student = request.POST['student']
        conduite = request.POST['conduite']
        decision = request.POST['decision']
        print("See PK Student", student)
        print("See PK period", period)

        # get object id student and period
        get_period = Period.objects.get(id=period)
        get_student = Student.objects.get(id=student)

        # get_p = Period.objects.get(id=get_period)
        # get_s = Student.objects.get(id=get_student)

        try:
            comportement = Comportement()
            comportement.student=get_student
            comportement.period=get_period
            comportement.conduite=conduite
            comportement.decision=decision

            comportement.save()

            messages.success(request, "Successfully Added")
            return redirect(reverse('student'))

        except Exception as e:
            messages.error(request, "Could Not Add " + str(e))
    else:
        messages.error(request, "Please fulfil all requirements")

    return render(request, template_name, context)

# End gestion student

# Begin gestion staf
# Function Add and select Staff

class StaffView(View):
    model = Staff
    template_name = "school_admin/gestion_staff/staff.html"
    form_class = StaffForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        staff = Staff.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'staff': staff })

    def post(self, request):
        form = StaffForm(request.POST or None, request.FILES or None)
        context = {'form': form, 'page_title': 'Add Staff'}
        if request.method == 'POST':
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                address = form.cleaned_data.get('address')
                email = form.cleaned_data.get('email')
                gender = form.cleaned_data.get('gender')
                password = form.cleaned_data.get('password')
                #course = form.cleaned_data.get('course')
                passport = request.FILES.get('profile_pic')
                fs = FileSystemStorage()
                # filename = fs.save(passport.name, passport)
                # passport_url = fs.url(filename)
                try:
                    user = User.objects.create_user(
                        email=email, password=password, user_type=2, first_name=first_name, last_name=last_name,
                        profile_pic=passport)
                    user.gender = gender
                    user.address = address
                    #user.staff.course = course
                    user.save()
                    messages.success(request, "Successfully Added")
                    return redirect(reverse('staff'))

                except Exception as e:
                    messages.error(request, "Could Not Add " + str(e))
            else:
                messages.error(request, "Please fulfil all requirements")

        return render(request, self.template_name, context)


def edit_staff(request, staff_id):
    staff_id = int(staff_id)
    try:
        staff = Staff.objects.get(id=staff_id)
    except Staff.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('staff')
    form = StaffForm(request.POST or None, instance=staff)
    context = {
        'form': form,
        'staff_id': staff,

    }
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password') or None
            course = form.cleaned_data.get('course')
            passport = request.FILES.get('profile_pic') or None
            try:
                user = User.objects.get(id=staff.admin.id)
                user.username = username
                user.email = email
                if password != None:
                    user.set_password(password)
                if passport != None:
                    fs = FileSystemStorage()
                    filename = fs.save(passport.name, passport)
                    passport_url = fs.url(filename)
                    user.profile_pic = passport_url
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                staff.course = course
                user.save()
                staff.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_staff', args=[staff_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please fil form properly")
    else:
        user = User.objects.get(id=staff_id)
        staff = Staff.objects.get(id=user.id)
        return render(request, "school_admin/gestion_staff/edit_staff.html", context)

class AffecterCoursView(CreateView):
    model = Participation
    form_class = ParticipationForm
    template_name = 'school_admin/gestion_staff/staff_course.html'
    success_url = reverse_lazy('affecter')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participation = self.model.objects.all()
        context['participate'] = participation
        print("Voir les participation",participation )
        return context


class AffecterCoursUpdateView(UpdateView):
    # specify the model you want to use
    model = Participation
    form_class = ParticipationForm
    template_name = 'school_admin/gestion_staff/edit_affecter.html'
    success_url = reverse_lazy('affecter')




class AffecterfCoursView(View):
    model = Staff
    template_name = "school_admin/gestion_staff/staff_course.html"
    form_class = ParticipationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        cours = Course.objects.all()
        staff = Staff.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'cours': cours,'staff':staff})

    def post(self, request):
        book_form = self.form_class(request.POST or None, request.FILES or None)
        context = {'form': book_form}
        if request.method == 'POST':

            if book_form.is_valid():

                name = book_form.cleaned_data.get('name')
                school_class = book_form.cleaned_data.get('school_class')

                # try:
                course = Course.objects.create(
                    name=name,school_class=school_class
                )

                course.save()
                messages.success(request, f"Cours add succefuly")
                return redirect(reverse('book'))
                # except Exception as e:
                #     messages.error(request, "Could Not Add: " + str(e))
            else:
                form = CourseForm()
                context['form'] = form
                messages.error(request, "Could Not Add: ")

        return render(request, self.template_name, context)

# end gestion staf

# Begin gestion class
class ClassView(View):
    model = Staff
    template_name = "school_admin/gestion_class/index_class.html"
    form_class = SchoolClassForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        school_class = SchoolClass.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'school_class': school_class,})

    def post(self, request):
        class_form = SchoolClassForm(request.POST or None, request.FILES or None)
        context = {'form': class_form}
        if request.method == 'POST':
            if class_form.is_valid():

                class_name = class_form.cleaned_data.get('class_name')
                class_num = class_form.cleaned_data.get('class_num')

                # try:
                school_class = SchoolClass.objects.create(
                    class_name=class_name,class_num=class_num
                )

                school_class.save()
                print("Voir resultat Officer ")
                messages.success(request, f"Class add succefuly")
                return redirect(reverse('school_class'))
                # except Exception as e:
                #     messages.error(request, "Could Not Add: " + str(e))
            else:
                form = SchoolClassForm()
                context['form'] = form
                messages.error(request, "Could Not Add: ")

        return render(request, self.template_name, context)

def edit_class(request, class_id):
    class_id = int(class_id)
    try:
        school_class = SchoolClass.objects.get(id=class_id)
    except SchoolClass.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('school_class')
    school_class_student = school_class.student_set.all().count()
    #school_class_course = school_class.course_set.all().count()
    form = SchoolClassForm(request.POST or None, instance=school_class)
    context = {
        'form': form,
        'school_class': school_class,
        'school_class_student': school_class_student,
        'school_class_course': "school_class_course"
    }
    if request.method == 'POST':
        if form.is_valid():
            class_name = form.cleaned_data.get('class_name')
            class_num = form.cleaned_data.get('class_num')
            try:
                course = SchoolClass.objects.get(id=class_id)
                course.class_name = class_name
                course.class_num = class_num
                course.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'school_admin/gestion_class/edit_class.html', context)

# End gestion Class

# Begin gestion Book
class CourseView(View):
    model = Staff
    template_name = "school_admin/gestion_book/course.html"
    form_class = CourseForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        cours = Course.objects.all()
        # url site https://restcountries.com/
        #data_country = requests.get("https://restcountries.com/v3.1/all").json()

        return render(request, self.template_name, {'form': form, 'cours': cours,})

    def post(self, request):
        book_form = CourseForm(request.POST or None, request.FILES or None)
        context = {'form': book_form}
        if request.method == 'POST':
            if book_form.is_valid():

                name = book_form.cleaned_data.get('name')
                #school_class = book_form.cleaned_data.get('school_class')
                #staff = book_form.cleaned_data.get('staff')

                # try:
                course = Course.objects.create(
                    name=name,
                )
                # school_class = school_class,
                # staff = staff

                course.save()
                messages.success(request, f"Cours add succefuly")
                return redirect(reverse('book'))
                # except Exception as e:
                #     messages.error(request, "Could Not Add: " + str(e))
            else:
                form = CourseForm()
                context['form'] = form
                messages.error(request, "Could Not Add: ")

        return render(request, self.template_name, context)

# function update
def edit_course(request, course_id):
    course_id = int(course_id)
    try:
        course = Course.objects.get(id = course_id)

    except Course.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('book')
    form = CourseForm(request.POST or None, instance=course)
    context = {
        'form': form,
        'course': course,
        'page_title': 'Edit Course'
    }
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            # school_class = form.cleaned_data.get('school_class')
            # staff = form.cleaned_data.get('staff')
            try:
                course = Course.objects.get(id=course_id)
                course.name = name
                # course.school_class = school_class
                # course.staff = staff
                course.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'school_admin/gestion_book/edit_course.html', context)

# End gestion book


# Begin gestion inbox mail
class InboxView(TemplateView):
    template_name = "school_admin/mailbox/mailbox.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context
# End gestion Inbox mail

# Begin gestion compose mail
class ComposeView(TemplateView):
    template_name = "school_admin/mailbox/compose.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context
# End gestion compose mail

# Begin gestion compose mail
class BulletinView(TemplateView):
    template_name = "school_admin/bulletin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context
# End gestion compose mail

def admin_home(request):
    total_staff = Staff.objects.all().count()
    total_students = Student.objects.all().count()
    total_course = Course.objects.all().count()


    context = {
        'page_title': "Administrative Dashboard",
        'total_students': total_students,
        'total_staff': total_staff,
        'total_course': total_course,


    }
    return render(request, 'school_admin/dashboard.html', context)

# function add staff
def add_staff(request):
    form = StaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
            #course = form.cleaned_data.get('course')
            passport = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            # filename = fs.save(passport.name, passport)
            # passport_url = fs.url(filename)
            try:
                user = User.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name, profile_pic=passport)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('staff'))

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'school_admin/gestion_staff/staff.html', context)

# add student
def add_student(request):
    form = StaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
            course = form.cleaned_data.get('course')
            passport = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            # filename = fs.save(passport.name, passport)
            # passport_url = fs.url(filename)
            try:
                user = User.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name, profile_pic=passport)
                user.gender = gender
                user.staff.school_class = course
                user.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('staff'))

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'school_admin/gestion_staff/staff.html', context)

# add profile admin
def admin_view_profile(request):
    admin = get_object_or_404(Admin, admin=request.user)

    # try:
    #     #admin = Admin.objects.get(admin=request.user)
    #     admin = get_object_or_404(Admin, admin=request.user)
    # except Admin.TypeError:
    #     messages.error(request, "Operational Error")
    #     return redirect('admin_home')

    form = AdminForm(request.POST or None, request.FILES or None,
                     instance=admin)
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
                custom_user = admin.admin
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
                return redirect(reverse('admin_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occured While Updating Profile " + str(e))
    return render(request, "school_admin/profile.html", context)

# add category blog
class AddCategoryView(View):
    model = Category
    success_msg = 'Category created.'
    form_class = CategoryForm
    template_name = "school_admin/gestion_event/category.html"

    def get(self, request, *args, **kwargs):
        context = {}
        form_category = self.form_class
        categories = Category.objects.all()
        context['form'] = form_category
        context['categories'] = categories
        return render(request, self.template_name , context)

    # create a post for show one and to make a comment
    def post(self, request):
        category_form = self.form_class(request.POST)
        context = {'form': category_form, 'page_title': 'Ajouter Categorie'}
        if request.method == 'POST':
            if category_form.is_valid():
                name = category_form.cleaned_data.get('name')
                try:
                    obj_category = Category.objects.create(
                         name=name,
                        )
                    if obj_category == "":
                        messages.error(request, "Ne peut etre ajouté: ")
                    else:
                        obj_category.save()
                    messages.success(request, f"Vous avez ajouté category {name}  avec succé")
                    return redirect(reverse('add_category'))
                except Exception as e:
                    messages.error(request, f"{name} ne peut etre ajouté : " + str(e))
            else:
                form = CategoryForm()
                messages.error(request, "Ne peut etre ajouté: ")
                context['form'] = form
        return render(request, self.template_name, context)

# update category
def edit_category(request, cate_id):

    cate_id = int(cate_id)
    try:
        cate_one = Category.objects.get(id=cate_id)

    except Category.DoesNotExist:
        messages.error(request, "Key Not Exist")
        return redirect('add_category')
    form = CategoryForm(request.POST or None, instance=cate_one)
    context = {
        'form': form,
        'category': cate_one,
        'page_title': 'Edit Course'
    }
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            try:
                category = Category.objects.get(id=cate_one)
                category.name = name
                category.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'school_admin/gestion_event/edit_category.html', context)

# list end add blog
class AllBlogs(TemplateView):
    template_name = 'school_admin/gestion_event/category.html'

    def get_context_data(self, **kwargs):
        context = super(AllBlogs, self).get_context_data(**kwargs)
        context['blogs'] = ArticleBlog.objects.filter().order_by('-created')
        context['categories'] = Category.objects.all()

        return context

# Add blog  function
class AddBlogView(View):
    model = ArticleBlog
    form_class = ArticleForm
    template_name = "school_admin/gestion_event/event.html"
    success_msg = 'blog created.'

    def get(self, request, *args, **kwargs):
        context = {}
        all_blogs = ArticleBlog.objects.all()
        context['form'] = self.form_class
        context['all_blogs'] = all_blogs
        return render(request, self.template_name, context)

    # create a post for show one and to make a comment
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == "POST":
            form = ArticleForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                description = form.cleaned_data['description']
                status = form.cleaned_data['status']
                category = form.cleaned_data['category']
                try:
                    blogpost = form.save(commit=False)
                    blogpost.title = title
                    blogpost.description = description
                    blogpost.image = image
                    blogpost.status = status
                    blogpost.category = category
                    blogpost.admin = Admin.objects.get(admin=request.user)
                    blogpost.save()
                    obj = form.instance
                    alert = True
                    messages.success(request, "Successfully Added")
                    return redirect(reverse('add_blog'))
                except Exception as e:
                    messages.error(request, f"ne peut etre ajouté : " + str(e))

                #return render(request, "inscription/gestion_blog/add_blog.html", {'obj': obj, 'alert': alert})
            else:
                form = ArticleForm()
                messages.error(request, "Could Not Add: ")
                context['form'] = form
        return render(request, self.template_name, context=context)

# function update blog article
def update_article(request, article_id):
    article_id = int(article_id)
    context = {}
    try:
        article_one = ArticleBlog.objects.get(id = article_id)
    except ArticleBlog.DoesNotExist:
        return redirect('add_blog')

    article_form = ArticleForm(request.POST or None, instance = article_one)
    context['article_one'] = article_one
    context['form'] = article_form
    if article_form.is_valid():
        try:
            article_form.save()
            messages.success(request, "Successfully Updated")
            #return redirect('add_blog')

        except:
            messages.error(request, "Could Not Update")
    else:
        messages.error(request, "Could Not Update")
    return render(request, 'school_admin/gestion_event/edit_event.html', context)

# function delete blog
def delete_blog(request, blog_id):
    blog_id = int(blog_id)
    try:
        blog_one = ArticleBlog.objects.get(id= blog_id)
    except ArticleBlog.DoesNotExist:
        return redirect('list_blog')
    blog_one.delete()
    return redirect('list_blog')

# Send message

def create_mail_view(request, *args, **kwargs):
    """This function view is help to send a mail"""
    context = {}
    statf = Staff.objects.all()

    all_message = Message.objects.all()
    context['messages'] = all_message
    context['message_count'] = all_message.count()
    context['statf'] = statf
    if request.method == "POST":
        email = request.POST.get('email')
        client_id = request.POST.get('client_id')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        email_from = settings.EMAIL_HOST_USER
        # recipient_list = [user.email, ]

        template = 'manager_op/send.html'
        context = {'date': datetime.datetime.today().date,
                   'email': email,
                   }
        receivers = [email, ]
        print(" Voir", email)

        send_mail(
            subject,
            content,
            email_from,
            [email, ],
            fail_silently=False
        )

        admin_id = Admin.objects.get(admin=request.user)
        print("ou est manager stp", admin_id)
        all_staff = Staff.objects.all()
        for c in all_staff:

            # nous comparons si l'addresse email get recuperer sur l'input hmtl
            # si cet egal a l'email de la table client
            if c.admin.email == email:
                msg = Message()
                msg.client = c  # cet object client
                msg.manager = admin_id # get_user(request)
                msg.subject = subject
                msg.content = content
                # msg = Message.objects.create(client=email,manager =get_user(request), subject=subject, content=content)

                msg.save()
                messages.success(request, ('Your message have sent succefuly!'))
                break
        # if has_send:
        #     message = "you send succefuly"
        #     context['msg'] = message
        # else:
        #     message = "you don't send message "
        #     context['msg'] = message

    # return render(request, 'manager_op/index.html', context )
    return render(request, 'school_admin/mailbox/compose.html', context)

