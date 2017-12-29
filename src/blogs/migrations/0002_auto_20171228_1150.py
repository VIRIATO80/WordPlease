# Generated by Django 2.0 on 2017-12-28 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpersonal',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='blogpersonal',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='blogpersonal',
            name='nombre_usuario',
        ),
        migrations.AlterField(
            model_name='blogpersonal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]