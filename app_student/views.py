from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, CreateView


# Create your views here.

class DashbordardView(TemplateView):
    template_name = "school_student/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = "Hi "
        return context
