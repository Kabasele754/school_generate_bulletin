from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = "school_public/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slider = ArticleBlog.objects.filter(status="slider")
        article_event = ArticleBlog.objects.filter(status="event")
        context['article_slider'] = article_slider
        context['all_evennt'] = article_event
        return context
 # Begin gestion student