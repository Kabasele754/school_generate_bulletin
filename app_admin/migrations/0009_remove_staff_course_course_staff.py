# Generated by Django 4.1 on 2023-01-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0008_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_admin.staff'),
        ),
    ]