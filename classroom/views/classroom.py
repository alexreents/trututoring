from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class TermsView(TemplateView):
    template_name = 'registration/terms.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            #return render(request, 'classroom/teachers/lesson_change_list.html')
            return redirect('teachers:lesson_change_list')
        else:
            #return render(request, 'classroom/students/tutor_list.html')
            return redirect('students:tutor_list')
    return render(request, 'classroom/home.html')