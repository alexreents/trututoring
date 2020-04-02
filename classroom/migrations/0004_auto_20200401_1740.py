# Generated by Django 3.0.5 on 2020-04-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200401_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='grade_level',
            field=models.ManyToManyField(related_name='graded_students', to='classroom.Grade'),
        ),
    ]
