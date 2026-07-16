from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Max
from datetime import timedelta
from django.utils import timezone

from quizzes.models import QuizAttempt


@login_required
def analytics(request):

    attempts = QuizAttempt.objects.filter(
        user=request.user
    )

    total_attempts = attempts.count()

    average_accuracy = (
        attempts.aggregate(
            Avg("percentage")
        )["percentage__avg"] or 0
    )

    highest_score = (
        attempts.aggregate(
            Max("score")
        )["score__max"] or 0
    )

    readiness = round(
        average_accuracy,
        2
    )
    
    today = timezone.now()

    daily_attempts = attempts.filter(
        submitted_at__date=today.date()
    ).count()

    weekly_attempts = attempts.filter(
        submitted_at__gte=today - timedelta(days=7)
    ).count()

    monthly_attempts = attempts.filter(
        submitted_at__gte=today - timedelta(days=30)
    ).count()

    context = {

        "total_attempts": total_attempts,

        "average_accuracy": round(
            average_accuracy,
            2
        ),

        "highest_score": highest_score,

        "readiness": readiness,

        "daily_attempts": daily_attempts,

        "weekly_attempts": weekly_attempts,

        "monthly_attempts": monthly_attempts,

    }
    return render(
        request,
        "analytics_app/analytics.html",
        context
    )