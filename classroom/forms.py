from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from classroom.models import (Student, Teacher, Subject, User, Grade, Availability, Session, Distance, Lesson) 


class TeacherSignUpForm(UserCreationForm):
    school = forms.CharField(label='your school',
        widget=forms.TextInput(attrs={'id':'selector-school'}),
        required=True,
        empty_value=''
    )

    rate = forms.CharField(label='your asking rate (in $/hour)',
        widget=forms.TextInput(attrs={'id':'selector-school'}),
        required=True,
        empty_value='15'
    )
    
    interests = forms.ModelMultipleChoiceField(label='select subjects',
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True,
    )

    grade_level = forms.ModelMultipleChoiceField(label='select preferred grade level',
        queryset=Grade.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    availability = forms.ModelMultipleChoiceField(label='select avialabilities',
        queryset=Availability.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    sessions = forms.ModelMultipleChoiceField(label='select sessions/week',
        queryset=Session.objects.all(),
        widget=forms.SelectMultiple(attrs={'id':'selector'}),
        required=True
    )

    distance = forms.ModelMultipleChoiceField(label='select max lesson distance',
        queryset=Distance.objects.all(),
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
        teacher = Teacher.objects.create(user=user, school=self.cleaned_data.get('school'), rate=self.cleaned_data.get('rate'))
        teacher.interests.add(*self.cleaned_data.get('interests'))
        teacher.grade_level.add(*self.cleaned_data.get('grade_level'))
        teacher.availability.add(*self.cleaned_data.get('availability'))
        teacher.sessions.add(*self.cleaned_data.get('sessions'))
        teacher.distance.add(*self.cleaned_data.get('distance'))
        teacher.verified = False

        return user


class StudentSignUpForm(UserCreationForm):
    school = forms.CharField(label='your school',
        widget=forms.TextInput(attrs={'id':'selector-school'}),
        required=True,
        empty_value=""
    )
    
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

    sessions = forms.ModelMultipleChoiceField(label='select sessions/week',
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
        student = Student.objects.create(user=user, school=self.cleaned_data.get('school'))
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

class StudentSchoolForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('school', )
        widgets = {
            'school': forms.TextInput(attrs={'id':'selector-school'})
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

class TeacherSchoolForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('school', )
        widgets = {
            'school': forms.TextInput(attrs={'id':'selector-school'})
        }

class TeacherDistanceForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('distance', )
        widgets = {
            'distance': forms.SelectMultiple(attrs={'id':'selector'})
        }

class TeacherRateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('rate', )
        widgets = {
            'rate': forms.TextInput(attrs={'id':'selector-school'})
        }

# For Lessons -- NOT CURRENTLY USED BECUASE FUNCTIONED INCORRECTLY 


class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name','rate','date','material')
        widgets = {
            'name': forms.TextInput(),
            'rate': forms.NumberInput(),
            'date': forms.DateInput(),
            'material': forms.Textarea(attrs={"id": "material-text"}),
        }

    def clean(self):
        try:
            if (User.objects.filter(username=self.cleaned_data['name']).exists() == False):
                raise ValidationError('The username entered does not correspond to a student!')
        except:
                pass
        


class LessonChangeForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'rate','date', 'material',)
        widgets = {
            'name': forms.TextInput(),
            'rate': forms.NumberInput(),
            'date': forms.DateInput(),
            'material': forms.Textarea(attrs={"id": "material-text"}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
