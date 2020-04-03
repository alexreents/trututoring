from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from classroom.models import (Student, Subject, User, Grade, Availability)


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
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


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        student.grade_level.add(*self.cleaned_data.get('grade_level'))
        student.availability.add(*self.cleaned_data.get('availability'))
        return user


class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.SelectMultiple
        }

class StudentGradesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('grade_level', )
        widgets = {
            'grade_level': forms.SelectMultiple
        }

class StudentAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('availability', )
        widgets = {
            'availability': forms.SelectMultiple
        }

