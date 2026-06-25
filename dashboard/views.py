from django.shortcuts import render
from quizzes.models import QuizAttempt
from django.db.models import Avg, Max, Min
from resources.models import StudyResource
import json

def dashboard(request):

    attempts = QuizAttempt.objects.filter(
        user=request.user
    )

    total_attempts = attempts.count()

    average_percentage = (
        attempts.aggregate(
            Avg('percentage')
        )['percentage__avg']
        or 0
    )

    highest_score = (
        attempts.aggregate(
            Max('score')
        )['score__max']
        or 0
    )

    lowest_score = (
        attempts.aggregate(
            Min('score')
        )['score__min']
        or 0
    )

    weak_topic = None
    resources = []

    topic_scores = {}

    for attempt in attempts:

        topic_name = attempt.quiz.topic.name

        if topic_name not in topic_scores:
            topic_scores[topic_name] = []

        topic_scores[topic_name].append(
            attempt.percentage
        )

    strong_topic = None

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
        
    if average_percentage >= 90:
        grade = 'A'

    elif average_percentage >= 75:
        grade = 'B'

    elif average_percentage >= 60:
        grade = 'C'

    else:
        grade = 'D'
    
    interview_readiness = round(
        average_percentage,
        2
    )
    
    recommendation = ""

    if interview_readiness >= 80:

        recommendation = (
            "You are interview ready."
        )

    elif interview_readiness >= 60:

        recommendation = (
            "Practice weak topics to improve confidence."
        )

    else:

        recommendation = (
            f"Focus on {weak_topic} before attempting interviews."
        )
        
    attempt_labels = []
    attempt_scores = []

    for attempt in attempts.order_by('-submitted_at')[:10]:

        attempt_labels.append(
            attempt.submitted_at.strftime('%d-%m')
        )

        attempt_scores.append(
            float(attempt.percentage)
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

        'total_attempts': total_attempts,

        'average_percentage': round(
            average_percentage,
            2
        ),

        'highest_score': highest_score,

        'lowest_score': lowest_score,

        'weak_topic': weak_topic,

        'resources': resources,
        
        'attempt_labels': json.dumps(
            attempt_labels
        ),

        'attempt_scores': json.dumps(
            attempt_scores
        ),

        'topic_labels': json.dumps(
            topic_labels
        ),

        'topic_percentages': json.dumps(
            topic_percentages
        ),
        
        'strong_topic': strong_topic,

        'grade': grade,

        'interview_readiness':
        interview_readiness,

        'recommendation':
        recommendation,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )