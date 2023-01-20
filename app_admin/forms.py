from django import forms
from django.forms.widgets import DateInput, TextInput

from .models import *
from app_public.models import *
from app_staff.models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
        'password': forms.PasswordInput(),
    }
    profile_pic = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if User.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).admin.email.lower()
            if dbEmail != formEmail:  # There has been changes
                if User.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError("The given email is already registered")

        return formEmail

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender',  'password','profile_pic', 'address' ]


class StudentForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields + \
            ['student_num', 'school_class']


class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Admin
        fields = CustomUserForm.Meta.fields


class StaffForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields


class CourseForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Course
        fields = ['name',]


class ParticipationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ParticipationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Participation
        fields = ['staff','course','period','school_class']

    staff = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    course = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-label'})
    )
    period = forms.ModelMultipleChoiceField(
        queryset=Period.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    school_class = forms.ModelMultipleChoiceField(
        queryset=SchoolClass.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class SchoolClassForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(SchoolClassForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SchoolClass
        fields = ['class_name','class_num']



class SchoolYearForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(SchoolYearForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SchoolYear
        fields = '__all__'
        widgets = {
            'start_year': DateInput(attrs={'type': 'date','class':'form-control datetimepicker-input'},format="%dT-%m-%Y"),
            'end_year': DateInput(attrs={'type': 'date','class':'form-control'},format="%dT-%m-%Y"),
        }

class PeriodForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(PeriodForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Period
        fields = '__all__'
        # widgets = {
        #     'start_year': DateInput(attrs={'type': 'date','class':'form-control datetimepicker-input'},format="%dT-%m-%Y"),
        #     'end_year': DateInput(attrs={'type': 'date','class':'form-control'},format="%dT-%m-%Y"),
        # }


class StudentEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields 


class StaffEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StaffEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields





class CategoryForm(FormSettings):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title categorie'}),
        }


class ArticleForm(FormSettings):
    class Meta:
        model = ArticleBlog
        #fields = '__all__'
        fields = ['title','image','status','category','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Copy the title with no space and a hyphen in between'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
        }


class ContactForm(forms.ModelForm):
    # number = PhoneNumberField(region="CA")
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'subject', 'message')

        # widgets = {
        #     'phone': PhoneNumberPrefixWidget(),
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')


class SystemConfigForm(FormSettings):
    class Meta:
        model = SystemConfig
        fields = ['logo_name','logo_image']
        widgets = {
            'logo_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            
        }
