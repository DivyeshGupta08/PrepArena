from django.urls import path

from .views import (
    topic_api,
    quiz_api,
    question_api,
    topic_quizzes_api,
    quiz_questions_api,
    login_api,
    profile_api,
    submit_quiz_api,
    attempt_history_api,
    attempt_detail_api,
    dashboard_api
)

urlpatterns = [

    path(
        'topics/',
        topic_api,
        name='topic_api'
    ),

    path(
        'quizzes/',
        quiz_api,
        name='quiz_api'
    ),

    path(
        'questions/',
        question_api,
        name='question_api'
    ),

    path(
        'topics/<int:topic_id>/quizzes/',
        topic_quizzes_api,
        name='topic_quizzes_api'
    ),

    path(
        'quizzes/<int:quiz_id>/questions/',
        quiz_questions_api,
        name='quiz_questions_api'
    ),
    
    path(
        'login/',
        login_api,
        name='login_api'
    ),
    
    path(
      'profile/',
        profile_api,
        name='profile_api'
    ),
    
    path(
        'submit-quiz/',
        submit_quiz_api,
        name='submit_quiz_api'
    ),
    
    path(
        'attempt-history/',
        attempt_history_api,
        name='attempt_history_api'
    ),
    
    path(
        'attempt/<int:attempt_id>/',
        attempt_detail_api,
        name='attempt_detail_api'
    ),
    
    path(
        'dashboard/',
        dashboard_api,
        name='dashboard_api'
    ),

]