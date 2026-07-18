from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.topic_list,
        name="topic_list"
    ),

    path(
        "topic/<int:topic_id>/",
        views.quiz_list,
        name="quiz_list"
    ),

    path(
        "start/<int:quiz_id>/",
        views.quiz_start,
        name="quiz_start"
    ),

    path(
        "take/<int:quiz_id>/",
        views.take_quiz,
        name="take_quiz"
    ),

    path(
        "result/<int:attempt_id>/",
        views.quiz_result,
        name="quiz_result"
    ),

    path(
        "review/<int:attempt_id>/",
        views.review_answers,
        name="review_answers"
    ),

    # NEW
    path(
        "history/",
        views.attempt_history,
        name="attempt_history"
    ),
]