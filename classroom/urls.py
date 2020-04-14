from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.TutorListView.as_view(), name='tutor_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('grade_level/', students.StudentGradesView.as_view(), name='student_grade_level'),
        path('availability/', students.StudentAvailabilityView.as_view(), name='student_availability'),
        path('sessions/', students.StudentSessionsView.as_view(), name='student_sessions'),
        path('school/', students.StudentSchoolView.as_view(), name='student_school'),
        
        path('lesson/<int:pk>/', students.take_lesson, name='take_lesson'),

    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.TutorListView.as_view(), name='lesson_change_list'),
        path('interests/', teachers.TeacherInterestsView.as_view(), name='teacher_interests'),
        path('grade_level/', teachers.TeacherGradesView.as_view(), name='teacher_grade_level'),
        path('availability/', teachers.TeacherAvailabilityView.as_view(), name='teacher_availability'),
        path('sessions/', teachers.TeacherSessionsView.as_view(), name='teacher_sessions'),
        path('school/', teachers.TeacherSchoolView.as_view(), name='teacher_school'),
        path('distance/', teachers.TeacherDistanceView.as_view(), name='teacher_distance'),
        path('rate/', teachers.TeacherRateView.as_view(), name='teacher_rate'),

        path('lesson/add/', teachers.LessonCreateView.as_view(), name='lesson_add'),
        path('lesson/<int:pk>/', teachers.LessonUpdateView.as_view(), name='lesson_change'),
        path('lesson/<int:pk>/delete/', teachers.LessonDeleteView.as_view(), name='lesson_delete'),
        path('lesson/<int:pk>/results/', teachers.LessonResultsView.as_view(), name='lesson_results'),

    ], 'classroom'), namespace='teachers')),
]
