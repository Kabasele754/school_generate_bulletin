from django.urls import path
from  .views import *
urlpatterns = [
   path('',DashbordardView.as_view(), name="staff_home"),
   path('all-course/',StaffCourseView.as_view(), name="staff_all_course"),
   path('all-course/detail_course/<int:course_id>/',detail_course, name="course_detail"),
   path('profile',staff_view_profile, name='profile_staff')
]
