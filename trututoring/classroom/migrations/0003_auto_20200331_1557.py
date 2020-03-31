# Generated by Django 2.0.1 on 2020-03-31 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='interests',
        ),
        migrations.AddField(
            model_name='student',
            name='topics',
            field=models.ManyToManyField(related_name='topical_students', to='classroom.Subject'),
        ),
    ]
