from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView
from .models import *
from app_admin.forms import *

# Create your views here.
class HomeView(TemplateView):
    template_name = "school_public/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slider = ArticleBlog.objects.filter(status="slider")
        article_event = ArticleBlog.objects.filter(status="event")
        context['article_slider'] = article_slider
        context['all_evennt'] = article_event
        context['logo'] = SystemConfig.objects.all().last()
        return context
    
class SystemLogoView(TemplateView):
    template_name = "public_school/partials/header.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slider = ArticleBlog.objects.filter(status="slider")
        article_event = ArticleBlog.objects.filter(status="event")
        context['article_slider'] = article_slider
        context['all_evennt'] = article_event
        context['logo'] = SystemConfig.objects.all().last()
        return context

class EventView(TemplateView):
    template_name = "school_public/event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slider = ArticleBlog.objects.filter(status="slider")
        article_event = ArticleBlog.objects.filter(status="event")
        context['article_slider'] = article_slider
        context['all_evennt'] = article_event
        context['recent_blogs'] = ArticleBlog.objects.order_by('-created')
        return context


class EventDetailView(DetailView):
    model = ArticleBlog
    template_name = "school_public/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        # slug = self.kwargs["slug"]

        form = CommentForm()
        post_blogs = get_object_or_404(ArticleBlog, pk=pk)
        comments = post_blogs.comment_set.all()
        comments_count = post_blogs.comment_set.all().count()


        context['post'] = post_blogs
        context['comments'] = comments
        context['comments_count'] = comments_count
        context['form'] = form
        context['categories'] = Category.objects.all()
        context['recent_blogs'] = ArticleBlog.objects.order_by('-created')

        return context

    # create a post for show one and to make a comment
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CommentForm(request.POST)
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)

            blog_id = ArticleBlog.objects.filter(id=self.kwargs['pk'])[0]
            comments = blog_id.comment_set.all()
            comments_count = blog_id.comment_set.all().count()

            context['post'] = blog_id
            context['comments'] = comments
            context['comments_count'] = comments_count
            context['form'] = form

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                content = form.cleaned_data['content']

                comment = Comment.objects.create(
                    name=name, email=email, content=content, article_blog=blog_id
                )
                comment.save()
                messages.success(request, "Votre commentaire est Successfull")
                form = CommentForm()

                context['form'] = form
                return self.render_to_response(context=context)

            return self.render_to_response(context=context)


class ContactView(View):
    model = Contact
    # template_name = "hotel/contact.html"
    success_msg = 'Contact created.'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = ContactForm()
        return render(request, "school_public/contact.html", context)

    # create a post for show one and to make a comment
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = {}

        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = Contact.objects.create(
                name=name, phone=phone, subject=subject, email=email, message=message, )
            contact.save()
            messages.success(request, f"{name} Votre message a ??t?? envoyer avec succ??")

            form = ContactForm()
            context['form'] = form
            # return render(request, "hotel/contact.html", context=context)

        return render(request, "school_public/contact.html", context=context)
