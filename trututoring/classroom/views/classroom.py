from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return render(request, 'classroom/teachers/values.html')
        else:
            return render(request, 'classroom/students/quiz_list.html')
    return render(request, 'classroom/home.html')
