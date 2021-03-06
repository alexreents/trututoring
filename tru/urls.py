from django.urls import include, path
from django.contrib import admin
from classroom.views import classroom, students, teachers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('classroom.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

    path('about/', classroom.AboutView.as_view(), name='about'),

    path('services/', classroom.ServicesView.as_view(), name='services'),
    path('faq/', classroom.FAQView.as_view(), name='faq'),
    path('pricing/', classroom.PricingView.as_view(), name='pricing'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/terms/', classroom.TermsView.as_view(), name='terms'),
    path('accounts/privacy/', classroom.PrivacyView.as_view(), name='privacy'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]

urlpatterns += staticfiles_urlpatterns()