from django.urls import include, path
from django.contrib import admin
from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'), 

    path('students/', include(([
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
    ], 'classroom'), namespace='students')),
    
    
    path('teachers/', include(([
        path('values', teachers.TeacherValuesView.as_view(), name='teacher_values'),
    ], 'classroom'), namespace='teachers')),
]

