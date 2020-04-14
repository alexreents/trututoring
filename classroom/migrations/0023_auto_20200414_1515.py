# Generated by Django 3.0.5 on 2020-04-14 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0022_auto_20200414_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='classroom.Teacher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='classroom.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='quizzes',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.AddField(
            model_name='student',
            name='lessons',
            field=models.ManyToManyField(to='classroom.Lesson'),
        ),
    ]