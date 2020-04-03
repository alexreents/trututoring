from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Grade(models.Model):
    grade_level = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.grade_level

    def get_html_badge(self):
        grade_level = escape(self.grade_level)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, grade_level)
        return mark_safe(html)

class Availability(models.Model):
    day = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.day + " " + self.time

    def get_html_badge(self):
        day = escape(self.day)
        time = escape(self.time)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s %s</span>' % (color, day, time)
        return mark_safe(html)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name='interested_students')
    grade_level = models.ManyToManyField(Grade, related_name='leveled_students')
    availability = models.ManyToManyField(Availability, related_name='available_students')

    def __str__(self):
        return self.user.username
