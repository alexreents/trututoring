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
from ..forms import (TeacherInterestsForm, TeacherSignUpForm, TeacherGradesForm, 
                    TeacherAvailabilityForm, TeacherSessionsForm, TeacherSchoolForm, TeacherDistanceForm, 
                    LessonAddForm, LessonChangeForm, TeacherRateForm)
from ..models import Lesson, User, Teacher


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
        return redirect('teachers:lesson_change_list')


# Teacher Profile Fields


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherInterestsView(UpdateView):
    model = Teacher
    form_class = TeacherInterestsForm
    template_name = 'classroom/teachers/interests_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Subjects updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherGradesView(UpdateView):
    model = Teacher
    form_class = TeacherGradesForm
    template_name = 'classroom/teachers/grade_level_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Grade level updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherAvailabilityView(UpdateView):
    model = Teacher
    form_class = TeacherAvailabilityForm
    template_name = 'classroom/teachers/availability_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Availability updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherSessionsView(UpdateView):
    model = Teacher
    form_class = TeacherSessionsForm
    template_name = 'classroom/teachers/sessions_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherSchoolView(UpdateView):
    model = Teacher
    form_class = TeacherSchoolForm
    template_name = 'classroom/teachers/school_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'School updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherDistanceView(UpdateView):
    model = Teacher
    form_class = TeacherDistanceForm
    template_name = 'classroom/teachers/distance_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherRateView(UpdateView):
    model = Teacher
    form_class = TeacherRateForm
    template_name = 'classroom/teachers/rate_form.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Lesson rate updated with success!')
        return super().form_valid(form)



@method_decorator([login_required, teacher_required], name='dispatch')
class TutorListView(TemplateView):
    template_name = 'classroom/teachers/lesson_change_list.html'


@method_decorator([login_required, teacher_required], name='dispatch')
class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonAddForm
    template_name = 'classroom/teachers/lesson_add_form.html'

    def form_valid(self, form):
        lesson = form.save(commit=False)
        lesson.tutor = self.request.user.teacher
        lesson.save()
        return redirect('teachers:lesson_change_list')
        

@method_decorator([login_required, teacher_required], name='dispatch')
class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonChangeForm  
    context_object_name = 'lesson'
    template_name = 'classroom/teachers/lesson_change_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing lessons that belongs
        to the logged in user.
        '''
        return self.request.user.teacher.lessons.all()

    def get_success_url(self):
        return reverse('teachers:lesson_change_list')


@method_decorator([login_required, teacher_required], name='dispatch')
class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'classroom/teachers/lesson_delete_confirm.html'
    success_url = reverse_lazy('teachers:lesson_change_list')

    def delete(self, request, *args, **kwargs):
        lesson = self.get_object()
        messages.success(request, 'The lesson %s was deleted with success!' % lesson.name)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.teacher.lessons.all()


@method_decorator([login_required, teacher_required], name='dispatch')
class LessonResultsView(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'classroom/teachers/lesson_results.html'

    def get_context_data(self, **kwargs):
        lesson = self.get_object()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.request.user.teacher.lessons.all()


