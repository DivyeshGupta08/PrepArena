from django.urls import path

from .views import topic_api, quiz_api, question_api, topic_quizzes_api, quiz_questions_api, login_api, profile_api


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

]