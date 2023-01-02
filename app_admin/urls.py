from django.urls import path
from  .views import *

urlpatterns = [
   path('',admin_home, name="admin_home"),
   path('student/',StudentView.as_view(), name="student"),
   path('staf/',add_staff, name="staf"),
   path('class/',ClassView.as_view(), name="class"),
   path('book/',BookView.as_view(), name="book"),

   # inbox

   path('inbox/',InboxView.as_view(), name="inbox"),
   path('inbox/compose/',ComposeView.as_view(), name="compose"),
   path('bulletin/',BulletinView.as_view(), name="bulletin"),
]
