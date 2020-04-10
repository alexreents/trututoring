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
        path('school/', students.StudentSchoolView.as_view(), name='student_school'),
        
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),

    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('interests/', teachers.TeacherInterestsView.as_view(), name='teacher_interests'),
        path('grade_level/', teachers.TeacherGradesView.as_view(), name='teacher_grade_level'),
        path('availability/', teachers.TeacherAvailabilityView.as_view(), name='teacher_availability'),
        path('sessions/', teachers.TeacherSessionsView.as_view(), name='teacher_sessions'),
        path('school/', teachers.TeacherSchoolView.as_view(), name='teacher_school'),
        path('distance/', teachers.TeacherDistanceView.as_view(), name='teacher_distance'),

        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),

    ], 'classroom'), namespace='teachers')),
]
