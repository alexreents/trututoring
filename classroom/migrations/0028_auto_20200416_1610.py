# Generated by Django 3.0.5 on 2020-04-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0027_auto_20200416_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='material',
            field=models.TextField(null=True, verbose_name='Material Covered + Notes'),
        ),
    ]
