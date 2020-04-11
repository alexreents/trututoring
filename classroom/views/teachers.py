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
                    QuizAddForm, QuizChangeForm)
from ..models import Quiz, User, Teacher


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


# Teacher Profile Fields


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherInterestsView(UpdateView):
    model = Teacher
    form_class = TeacherInterestsForm
    template_name = 'classroom/teachers/interests_form.html'
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
    template_name = 'classroom/teachers/grade_level_form.html'
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
    template_name = 'classroom/teachers/availability_form.html'
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
    template_name = 'classroom/teachers/sessions_form.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

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
    success_url = reverse_lazy('teachers:quiz_change_list')

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
    success_url = reverse_lazy('teachers:quiz_change_list')

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)


#@method_decorator([login_required, teacher_required], name='dispatch')
#class TeacherQuizListView(TemplateView):
#    template_name = 'classroom/teachers/quiz_change_list.html'

@method_decorator([login_required, teacher_required], name='dispatch')
class QuizListView(ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'classroom/teachers/quiz_change_list.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject')
        return queryset



@method_decorator([login_required, teacher_required], name='dispatch')
class QuizCreateView(CreateView):
    model = Quiz
    fields = ('name', 'subject', 'zoom')

    #form_class = QuizAddForm
    template_name = 'classroom/teachers/quiz_add_form.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.save()
        messages.success(self.request, 'The quiz was successfully created!')
        return redirect('teachers:quiz_change_list')



@method_decorator([login_required, teacher_required], name='dispatch')
class QuizUpdateView(UpdateView):
    model = Quiz
    #form_class = QuizChangeForm  
    fields = ('name', 'subject', 'zoom')  
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_change_form.html'

    def get_context_data(self, **kwargs):
        #kwargs['questions'] = self.get_object().questions.annotate(answers_count=Count('answers'))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.user.quizzes.all()

    def get_success_url(self):
        return reverse('teachers:quiz_change_list')


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizDeleteView(DeleteView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_delete_confirm.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        messages.success(request, 'The quiz %s was deleted with success!' % quiz.name)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.quizzes.all()


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizResultsView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_results.html'

    def get_context_data(self, **kwargs):
        quiz = self.get_object()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.request.user.quizzes.all()


