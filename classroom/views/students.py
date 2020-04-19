from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.conf import settings

from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm

from ..decorators import student_required
from ..forms import StudentInterestsForm, StudentSignUpForm, StudentGradesForm, StudentAvailabilityForm, StudentSessionsForm, StudentSchoolForm
from ..models import Student, User, Lesson, Teacher

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
        return redirect('students:tutor_list')


# Student Profile Fields


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('students:tutor_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Subjects updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, student_required], name='dispatch')
class StudentGradesView(UpdateView):
    model = Student
    form_class = StudentGradesForm
    template_name = 'classroom/students/grade_level_form.html'
    success_url = reverse_lazy('students:tutor_list')

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
    success_url = reverse_lazy('students:tutor_list')

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
    success_url = reverse_lazy('students:tutor_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Sessions updated with success!')
        return super().form_valid(form)

@method_decorator([login_required, student_required], name='dispatch')
class StudentSchoolView(UpdateView):
    model = Student
    form_class = StudentSchoolForm
    template_name = 'classroom/students/school_form.html'
    success_url = reverse_lazy('students:tutor_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'School updated with success!')
        return super().form_valid(form)



#@method_decorator([login_required, student_required], name='dispatch')
#class StudentTutorListView(TemplateView):
#    template_name = 'classroom/students/tutor_list.html'


@method_decorator([login_required, student_required], name='dispatch')
class TutorListView(ListView):
    model = Student
    ordering = ('name', )
    context_object_name = 'teachers'
    template_name = 'classroom/students/tutor_list.html'

#    def get_queryset(self):
#        student = self.request.user.student
#        student_interests = student.interests.values_list('pk', flat=True)
#        queryset = Lesson.objects.filter(subject__in=student_interests) \
#            .annotate() \
#            .filter()
#        return queryset

    def get_queryset(self):
        student = self.request.user.student
        student_interests = student.interests.values_list('pk', flat=True)
        queryset = Teacher.objects.distinct() \
            .filter(interests__in=student_interests)
        return queryset


@method_decorator([login_required, student_required], name='dispatch')
class LessonListView(ListView):
    model = Lesson
    ordering = ('name', )
    context_object_name = 'lessons'
    template_name = 'classroom/students/lesson_list.html'

    def get_queryset(self):
        student_username = self.request.user.username
        queryset = Lesson.objects.all() \
            .filter(name=student_username)
        return queryset



@login_required
@student_required
def process_payment(request, pk):
    host = request.get_host()
    lesson = get_object_or_404(Lesson, pk=pk)
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': 0.02,
        'item_name': 'TRU Tutor: {}'.format(lesson.tutor.user.email),
        'invoice': str(lesson.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'classroom/students/process_payment.html', {'form': form})


@csrf_exempt
def payment_done(request):
    #return redirect('students:payment_done')
    return render(request, 'classroom/students/payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    #return redirect('students:payment_done')
    return render(request, 'classroom/students/payment_canceled.html')


#stripe.api_key = settings.STRIPE_SECRET_KEY
#
#@login_required
#@student_required
#def charge(request, pk): # new
#    lesson = get_object_or_404(Lesson, pk=pk)
#
#    if request.method == 'POST':
#        charge = stripe.Charge.create(
#            amount=2250,
#            currency='usd',
#            description='TUTOR: ' + lesson.tutor.user.username,
#            source=request.POST['stripeToken'],
#        )
#
#        lesson.paid = True
#        lesson.save()
#
#        #return render(request, 'classroom/students/charge.html')
#        return redirect('students:lesson_list')


    