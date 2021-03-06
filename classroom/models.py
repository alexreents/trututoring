from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.shortcuts import get_object_or_404



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#505050')

    def __str__(self):
        return self.name

    def get_text_name(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span id="badger">%s</span>' % (name)
        return mark_safe(html)


class Grade(models.Model):
    grade_level = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#505050')

    def __str__(self):
        return self.grade_level

    def get_text_name(self):
        return self.grade_level

    def get_html_badge(self):
        grade_level = escape(self.grade_level)
        color = escape(self.color)
        html = '<span id="badger">%s</span>' % (grade_level)
        return mark_safe(html)

class Availability(models.Model):
    day = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#505050')

    def __str__(self):
        return self.day + " " + self.time

    def get_text_name(self):
        return self.day + " " + self.time

    def get_html_badge(self):
        day = escape(self.day)
        time = escape(self.time)
        color = escape(self.color)
        html = '<span id="badger">%s %s</span>' % (day, time)
        return mark_safe(html)

class Session(models.Model):
    sessions = models.CharField(max_length=30)

    def __str__(self):
        return self.sessions

    def get_html_badge(self):
        sessions = escape(self.sessions)
        html = '<span id="badger">%s</span>' % (sessions)
        return mark_safe(html)

class Distance(models.Model):
    distance = models.CharField(max_length=30)

    def __str__(self):
        return self.distance

    def get_html_badge(self):
        distance = escape(self.distance)
        html = '<span id="badger">%s</span>' % (distance)
        return mark_safe(html)

class Rate(models.Model):
    rate = models.FloatField(max_length=30)

    def __str__(self):
        return self.rate

    def get_html_badge(self):
        rate = escape(self.reate)
        html = '<span id="badger">%s</span>' % (rate)
        return mark_safe(html)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name='interested_teachers', verbose_name='subjects')
    grade_level = models.ManyToManyField(Grade, related_name='leveled_teachers')
    availability = models.ManyToManyField(Availability, related_name='available_teachers')
    sessions = models.ManyToManyField(Session, related_name='session_teachers')
    school = models.CharField(max_length=50, verbose_name='your school', null=True)
    distance = models.ManyToManyField(Distance, related_name='distanced_teachers', verbose_name='max lesson radius')
    rate = models.FloatField(max_length=50, verbose_name='your asking rate (in $/hour', default='15')
    verified = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.username

class Lesson(models.Model):
    tutor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255, null=False, verbose_name="Student Username")
    rate = models.FloatField(max_length=30, default=22.50, verbose_name="Lesson Rate")
    date = models.DateField(null=True, verbose_name="Lesson Date (mm/dd/yyyy)")
    material = models.TextField(null=True, verbose_name="Zoom Link + Meeting Details")
    paid = models.BooleanField(default=False)

    def getStudentUser(self):
        my_user = get_object_or_404(User, username=self.name)
        return my_user

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    lessons = models.ManyToManyField(Lesson)
    interests = models.ManyToManyField(Subject, related_name='interested_students', verbose_name='subjects')
    grade_level = models.ManyToManyField(Grade, related_name='leveled_students')
    availability = models.ManyToManyField(Availability, related_name='available_students')
    sessions = models.ManyToManyField(Session, related_name='session_students')
    school = models.CharField(max_length=50, verbose_name='your school', null=True)

    def __str__(self):
        return self.user.username

