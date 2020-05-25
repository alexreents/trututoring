from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ..forms import ContactForm
from ..models import Lesson

#class AboutView(TemplateView):
#    template_name = 'classroom/about.html'

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class TermsView(TemplateView):
    template_name = 'registration/terms.html'

class PrivacyView(TemplateView):
    template_name = 'registration/privacy.html'    

class ServicesView(TemplateView):
    template_name = 'classroom/services.html'

class FAQView(TemplateView):
    template_name = 'classroom/faq.html'

class PricingView(TemplateView):
    template_name = 'classroom/pricing.html'



def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            #return render(request, 'classroom/teachers/lesson_change_list.html')
            return redirect('teachers:lesson_change_list')
        else:
            #return render(request, 'classroom/students/tutor_list.html')
            return redirect('students:tutor_list')
    return render(request, 'classroom/home.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['trututoring@gmail.com'])
            return render(request, 'classroom/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'classroom/contact.html', {'form': form})


class AboutView(ListView):
    model = Lesson
    template_name = 'classroom/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num = Lesson.objects.count()
        context['count'] = num+556      # 556 completed already at time of release
        return context