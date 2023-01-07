from django.db import models
from django.utils import timezone
from app_admin.models import Admin

# Create your models here.

# Model Category
class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ArticleBlog(models.Model):
    choice_etat = (
        ('slider', 'Slider'),
        ('event', 'Event')
    )


    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    #slug = models.SlugField(blank=True, max_length=100, unique=True)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=choice_etat, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # user tag pip install django-taggit
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.title) if self.title else ''




# Model Comments for Article and Blog

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    article_blog = models.ForeignKey(ArticleBlog, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', 'name', 'email')

    def __str__(self):
        return 'Comment by {}'.format(self.name)

# class Like(models.Model):
#     user = models.ForeignKey(UserPLU)
#     post = models.ForeignKey(ArticleBlog)
#     timestamp = models.DateTimeField()
#     value = models.CharField(choices=Like_Choice, default='Like', max_length=20)
#
#     def __str__(self):
#         return f'{self.user.nom} likes \'{self.post.title}\''

# Model contact

class Contact(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=False, help_text='Must be in format +(243)9999999999')
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

