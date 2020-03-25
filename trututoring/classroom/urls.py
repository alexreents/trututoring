from django.urls import include, path

from .views import classroom, students, tutors

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('tutors/', include(([
        path('', tutors.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', tutors.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', tutors.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', tutors.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', tutors.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', tutors.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', tutors.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', tutors.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='tutors')),
]
