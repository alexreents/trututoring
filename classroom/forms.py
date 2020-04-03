from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from classroom.models import (Student, Teacher, Subject, User, Grade, Availability, Session)


class TeacherSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(label='select subjects',
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True,
    )

    grade_level = forms.ModelMultipleChoiceField(label='select your grade level',
        queryset=Grade.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    availability = forms.ModelMultipleChoiceField(label='select avialabilities',
        queryset=Availability.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    sessions = forms.ModelMultipleChoiceField(label='select # of sessions/week',
        queryset=Session.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.interests.add(*self.cleaned_data.get('interests'))
        teacher.grade_level.add(*self.cleaned_data.get('grade_level'))
        teacher.availability.add(*self.cleaned_data.get('availability'))
        teacher.sessions.add(*self.cleaned_data.get('sessions'))
        return user


class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(label='select subjects',
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    grade_level = forms.ModelMultipleChoiceField(label='select your grade level',
        queryset=Grade.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    availability = forms.ModelMultipleChoiceField(label='select availabilities',
        queryset=Availability.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    sessions = forms.ModelMultipleChoiceField(label='select # of sessions/week',
        queryset=Session.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
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

# For Students

class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.SelectMultiple(attrs={'id':'selector'})
        }

class StudentGradesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('grade_level', )
        widgets = {
            'grade_level': forms.SelectMultiple(attrs={'id':'selector'})
        }

class StudentAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('availability', )
        widgets = {
            'availability': forms.SelectMultiple(attrs={'id':'selector'})
        }

class StudentSessionsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('sessions', )
        widgets = {
            'sessions': forms.SelectMultiple(attrs={'id':'selector'})
        }

# For Teachers

class TeacherInterestsForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('interests', )
        widgets = {
            'interests': forms.SelectMultiple(attrs={'id':'selector'})
        }

class TeacherGradesForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('grade_level', )
        widgets = {
            'grade_level': forms.SelectMultiple(attrs={'id':'selector'})
        }

class TeacherAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('availability', )
        widgets = {
            'availability': forms.SelectMultiple(attrs={'id':'selector'})
        }

class TeacherSessionsForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('sessions', )
        widgets = {
            'sessions': forms.SelectMultiple(attrs={'id':'selector'})
        }
