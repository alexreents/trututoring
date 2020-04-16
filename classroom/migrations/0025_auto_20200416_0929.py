# Generated by Django 3.0.5 on 2020-04-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0024_auto_20200414_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ManyToManyField(related_name='lessons', to='classroom.Subject', verbose_name='subject(s)'),
        ),
    ]