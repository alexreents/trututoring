from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from classroom.models import (Student, Teacher, Subject, User, Grade, Availability, Session)


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user


class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )

    grade_level = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )

    availability = forms.ModelMultipleChoiceField(
        queryset=Availability.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )

    sessions = forms.ModelMultipleChoiceField(
        queryset=Session.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        student.grade_level.add(*self.cleaned_data.get('grade_level'))
        student.availability.add(*self.cleaned_data.get('availability'))
        student.sessions.add(*self.cleaned_data.get('sessions'))
        return user


class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.SelectMultiple(attrs={'style':'height: 10em'})
        }

class StudentGradesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('grade_level', )
        widgets = {
            'grade_level': forms.SelectMultiple(attrs={'style':'height: 10em'})
        }

class StudentAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('availability', )
        widgets = {
            'availability': forms.SelectMultiple(attrs={'style':'height: 10em'})
        }

class StudentSessionsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('sessions', )
        widgets = {
            'sessions': forms.SelectMultiple(attrs={'style':'height: 10em'})
        }
