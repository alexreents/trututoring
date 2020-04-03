from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from ..decorators import student_required
from ..forms import StudentInterestsForm, StudentSignUpForm, StudentGradesForm, StudentAvailabilityForm, StudentSessionsForm
from ..models import Student, User


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:quiz_list')

@method_decorator([login_required, student_required], name='dispatch')
class QuizListView(TemplateView):
    template_name = 'classroom/students/quiz_list.html'


# Student Profile Fields


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, student_required], name='dispatch')
class StudentGradesView(UpdateView):
    model = Student
    form_class = StudentGradesForm
    template_name = 'classroom/students/grade_level_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Grade level updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, student_required], name='dispatch')
class StudentAvailabilityView(UpdateView):
    model = Student
    form_class = StudentAvailabilityForm
    template_name = 'classroom/students/availability_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Availability updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, student_required], name='dispatch')
class StudentSessionsView(UpdateView):
    model = Student
    form_class = StudentSessionsForm
    template_name = 'classroom/students/sessions_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)