# Generated by Django 2.0.4 on 2018-09-27 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
    ]
