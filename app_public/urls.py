from django.urls import path
from  .views import *

urlpatterns = [
   path('',HomeView.as_view(), name="home"),
   path('event/',EventView.as_view(), name="event"),
   path('event/detail/<pk>/', EventDetailView.as_view(), name='event_detail'),
   path('contact/', ContactView.as_view(), name="contact"),
]