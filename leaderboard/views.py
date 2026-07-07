from django.shortcuts import render
from django.db.models import Avg, Count

from quizzes.models import QuizAttempt


def leaderboard(request):

    leaderboard_data = (

        QuizAttempt.objects

        .values(
            'user__username'
        )

        .annotate(

            average_score=Avg('percentage'),

            total_attempts=Count('id')

        )

        .order_by('-average_score')

    )

    context = {

        'leaderboard_data': leaderboard_data

    }

    return render(

        request,

        'leaderboard/leaderboard.html',

        context

    )