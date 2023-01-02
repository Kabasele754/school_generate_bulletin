from django.urls import path
from .views import *

urlpatterns = [
   path('',admin_home, name="admin_home"),
   path('student/',StudentView.as_view(), name="student"),
   path('staf/',StaffView.as_view(), name="staff"),
   path('class/',ClassView.as_view(), name="school_class"),
   path('course/',CourseView.as_view(), name="book"),

   # inbox
   path('inbox/',InboxView.as_view(), name="inbox"),
   path('inbox/compose/',ComposeView.as_view(), name="compose"),
   path('bulletin/',BulletinView.as_view(), name="bulletin"),
]
