from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE = ((1, "admin"), (2, "Staff"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female")]
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )

    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_pic = models.ImageField(null=True, blank=True)
    address = models.TextField()
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ", " + self.last_name


class SchoolYear(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return str(self.start_year) + " == " + str(self.end_year)


class Period(models.Model):
    PERIOD = [("1erep", "1ere p"), ("2emep", "2ème P"),("examen1", "Examen 1"),  ("3emep", "3ème P"), ("4emep", "4ème P"),("examen2", "Examen 2")]
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )
    period_name = models.CharField(max_length=50,default="1erep", choices=PERIOD)
    year_school = models.ForeignKey(SchoolYear, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.period_name)


class SchoolClass(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    class_name = models.CharField(max_length=25)
    class_num = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.class_name)

    def student_cls(self):
        sch_cls = SchoolClass.objects.all()
        stud = sch_cls.student_set()
        return stud.count()


class Admin(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )
    admin = models.OneToOneField(User, on_delete=models.CASCADE)


class Student(models.Model):
   
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    student_num = models.IntegerField(null=True, blank=False)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING,null=True, blank=False)

    def __str__(self):
        return self.admin.last_name + ", " + self.admin.first_name


class Staff(models.Model):
    ROLE = ((1, "Teacher"), (2, "Etude_Teacher"), (3, "Student"))
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.BooleanField(default=1)

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=120)
    max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, null=True, blank=False)
    #school_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} {self.max}"



class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    # file = models.FileField(upload_to='message/')

    def __str__(self):
        return f"{self.staff}  {self.admin}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.student.save()
