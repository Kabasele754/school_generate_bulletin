# Generated by Django 4.1 on 2023-01-03 15:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_admin', '0007_alter_student_school_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type_article_slid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('publised', 'PUBLISHED'), ('draft', 'DRAFT')], max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(help_text='Must be in format +(243)9999999999', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_public.articleblog')),
            ],
            options={
                'ordering': ('-created', 'name', 'email'),
            },
        ),
        migrations.AddField(
            model_name='articleblog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_public.category'),
        ),
    ]
