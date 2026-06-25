from django.urls import path

from .views import topic_api, quiz_api, question_api


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

]