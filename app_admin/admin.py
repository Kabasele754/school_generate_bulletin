from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(SchoolClass)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(SchoolYear)

