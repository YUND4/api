# Generated by Django 2.1.5 on 2019-01-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_development',
            field=models.BooleanField(default=False, verbose_name='development status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_funcionary',
            field=models.BooleanField(default=False, verbose_name='funcionary status'),
        ),
    ]