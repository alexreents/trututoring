# Generated by Django 3.0.5 on 2020-04-03 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_create_initial_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=7)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='grade_level',
            field=models.ManyToManyField(related_name='leveled_students', to='classroom.Grade'),
        ),
        migrations.AddField(
            model_name='student',
            name='availability',
            field=models.ManyToManyField(related_name='available_students', to='classroom.Availability'),
        ),
    ]