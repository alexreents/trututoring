# Generated by Django 3.0.5 on 2020-04-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0025_auto_20200416_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
