from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)

from ..decorators import teacher_required
from ..forms import TeacherInterestsForm, TeacherSignUpForm, TeacherGradesForm, TeacherAvailabilityForm, TeacherSessionsForm
from ..models import User, Teacher


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherQuizListView(TemplateView):
    template_name = 'classroom/teachers/quiz_change_list.html'


# Teacher Profile Fields


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherInterestsView(UpdateView):
    model = Teacher
    form_class = TeacherInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Subjects updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherGradesView(UpdateView):
    model = Teacher
    form_class = TeacherGradesForm
    template_name = 'classroom/students/grade_level_form.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Grade level updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherAvailabilityView(UpdateView):
    model = Teacher
    form_class = TeacherAvailabilityForm
    template_name = 'classroom/students/availability_form.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Availability updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherSessionsView(UpdateView):
    model = Teacher
    form_class = TeacherSessionsForm
    template_name = 'classroom/students/sessions_form.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)