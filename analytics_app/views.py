from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Max
from datetime import timedelta
from django.utils import timezone

from quizzes.models import QuizAttempt
from resources.models import StudyResource

import json


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

    topic_scores = {}

    for attempt in attempts:

        topic = attempt.quiz.topic.name

        if topic not in topic_scores:
            topic_scores[topic] = []

        topic_scores[topic].append(
            attempt.percentage
        )

    weak_topic = None
    strong_topic = None
    recommendation = ""
    resources = []

    if topic_scores:

        averages = {

            topic: sum(scores) / len(scores)

            for topic, scores in topic_scores.items()

        }

        weak_topic = min(
            averages,
            key=averages.get
        )

        strong_topic = max(
            averages,
            key=averages.get
        )

        resources = StudyResource.objects.filter(
            topic_name=weak_topic
        )

    if readiness >= 80:

        recommendation = (
            "Excellent! You are interview ready."
        )

    elif readiness >= 60:

        recommendation = (
            "Good progress. Practice weak topics to improve."
        )

    else:

        recommendation = (
            f"Focus on {weak_topic} before attempting interviews."
            if weak_topic
            else
            "Start solving more quizzes."
        )

    attempt_labels = []
    attempt_scores = []

    for attempt in attempts.order_by(
        "-submitted_at"
    )[:10]:

        if attempt.submitted_at:

            attempt_labels.append(
                attempt.submitted_at.strftime("%d-%m")
            )

        else:

            attempt_labels.append("Unknown")

        attempt_scores.append(
            float(
                attempt.percentage
            )
        )

    topic_labels = []
    topic_percentages = []

    for topic, scores in topic_scores.items():

        topic_labels.append(topic)

        topic_percentages.append(
            round(
                sum(scores) / len(scores),
                2
            )
        )

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

        "weak_topic": weak_topic,

        "strong_topic": strong_topic,

        "recommendation": recommendation,

        "resources": resources,

        "attempt_labels": json.dumps(
            attempt_labels
        ),

        "attempt_scores": json.dumps(
            attempt_scores
        ),

        "topic_labels": json.dumps(
            topic_labels
        ),

        "topic_percentages": json.dumps(
            topic_percentages
        ),

    }

    return render(
        request,
        "analytics_app/analytics.html",
        context
    )