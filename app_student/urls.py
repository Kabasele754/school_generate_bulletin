from django.urls import path
from  .views import *
urlpatterns = [
   path('',DashbordardView.as_view(), name="dashboard_student"),
]
