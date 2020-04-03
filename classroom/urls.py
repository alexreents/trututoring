from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('grade_level/', students.StudentGradesView.as_view(), name='student_grade_level'),
        path('availability/', students.StudentAvailabilityView.as_view(), name='student_availability'),
        path('sessions/', students.StudentSessionsView.as_view(), name='student_sessions'),

    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
    ], 'classroom'), namespace='teachers')),
]
