from django.urls import include, path
from django.contrib import admin
from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'), 

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('topics/', students.StudentTopicsView.as_view(), name='student_topics'),
    ], 'classroom'), namespace='students')),
    
    
    path('teachers/', include(([
        path('values', teachers.TeacherValuesView.as_view(), name='values'),
    ], 'classroom'), namespace='teachers')),
]

