from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from quizzes.models import Topic, Quiz, Question, QuizAttempt, UserAnswer
from .serializers import (
    TopicSerializer,
    QuizSerializer,
    QuestionSerializer,
    QuizSubmissionSerializer,
    QuizAttemptSerializer,
    DashboardSerializer,
    LeaderboardSerializer
)
from django.utils import timezone
from django.db.models import Avg, Max, Min
from resources.models import StudyResource
from django.contrib.auth.models import User


@api_view(['GET'])
def topic_api(request):

    topics = Topic.objects.all()

    serializer = TopicSerializer(
        topics,
        many=True
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
def quiz_api(request):

    quizzes = Quiz.objects.all()

    serializer = QuizSerializer(
        quizzes,
        many=True
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
def question_api(request):

    questions = Question.objects.all()

    serializer = QuestionSerializer(
        questions,
        many=True
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
def topic_quizzes_api(
    request,
    topic_id
):

    topic = get_object_or_404(
        Topic,
        id=topic_id
    )

    quizzes = Quiz.objects.filter(
        topic=topic
    )

    serializer = QuizSerializer(
        quizzes,
        many=True
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
def quiz_questions_api(
    request,
    quiz_id
):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    questions = Question.objects.filter(
        quiz=quiz
    )

    serializer = QuestionSerializer(
        questions,
        many=True
    )

    return Response(
        serializer.data
    )
    
@api_view(['POST'])
def login_api(request):

    username = request.data.get(
        'username'
    )

    password = request.data.get(
        'password'
    )

    user = authenticate(
        username=username,
        password=password
    )

    if user:

        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response({

            'token': token.key,

            'username': user.username

        })

    return Response({

        'error': 'Invalid Credentials'

    })
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_api(request):

    return Response({

        'username': request.user.username,

        'email': request.user.email,

        'id': request.user.id

    })
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def submit_quiz_api(request):

    serializer = QuizSubmissionSerializer(
        data=request.data
    )

    if not serializer.is_valid():

        return Response(
            serializer.errors,
            status=400
        )

    quiz = get_object_or_404(
        Quiz,
        id=serializer.validated_data['quiz_id']
    )

    answers = serializer.validated_data['answers']

    questions = Question.objects.filter(
        quiz=quiz
    )

    attempt = QuizAttempt.objects.create(
        user=request.user,
        quiz=quiz
    )

    score = 0

    for question in questions:

        selected_option = answers.get(
            str(question.id),
            ""
        )

        is_correct = (
            selected_option.upper() ==
            question.correct_option.upper()
        )

        if is_correct:
            score += 1

        UserAnswer.objects.create(
            attempt=attempt,
            question=question,
            selected_option=selected_option,
            is_correct=is_correct
        )

    total_questions = questions.count()

    percentage = (
        score / total_questions * 100
        if total_questions > 0
        else 0
    )

    attempt.score = score
    attempt.percentage = percentage
    attempt.submitted_at = timezone.now()

    attempt.save()

    return Response({

        "score": score,

        "total_questions": total_questions,

        "percentage": percentage

    })
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def attempt_history_api(request):

    attempts = QuizAttempt.objects.filter(
        user=request.user
    ).order_by('-submitted_at')

    serializer = QuizAttemptSerializer(
        attempts,
        many=True
    )

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def attempt_detail_api(request, attempt_id):

    attempt = get_object_or_404(
        QuizAttempt,
        id=attempt_id,
        user=request.user
    )

    serializer = QuizAttemptSerializer(
        attempt
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_api(request):

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

    topic_scores = {}

    for attempt in attempts:

        topic = attempt.quiz.topic.name

        topic_scores.setdefault(
            topic,
            []
        )

        topic_scores[topic].append(
            attempt.percentage
        )

    weak_topic = ""

    strong_topic = ""

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

    interview_readiness = round(
        average_percentage,
        2
    )

    if interview_readiness >= 80:

        grade = "A"

    elif interview_readiness >= 60:

        grade = "B"

    elif interview_readiness >= 40:

        grade = "C"

    else:

        grade = "D"

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

    data = {

        "total_attempts": total_attempts,

        "average_percentage": round(
            average_percentage,
            2
        ),

        "highest_score": highest_score,

        "lowest_score": lowest_score,

        "weak_topic": weak_topic,

        "strong_topic": strong_topic,

        "grade": grade,

        "interview_readiness": interview_readiness,

        "recommendation": recommendation,
    }

    serializer = DashboardSerializer(
        instance=data
    )

    return Response(
        serializer.data
    )
    
@api_view(['GET'])
def leaderboard_api(request):

    users = User.objects.all()

    leaderboard = []

    for user in users:

        attempts = QuizAttempt.objects.filter(
            user=user
        )

        if attempts.exists():

            leaderboard.append({

                "username": user.username,

                "best_score": (
                    attempts.aggregate(
                        Max('score')
                    )['score__max']
                ),

                "average_percentage": round(

                    attempts.aggregate(
                        Avg('percentage')
                    )['percentage__avg'],

                    2
                )
            })

    leaderboard = sorted(

        leaderboard,

        key=lambda x: (
            x['best_score'],
            x['average_percentage']
        ),

        reverse=True
    )

    serializer = LeaderboardSerializer(

        leaderboard,

        many=True
    )

    return Response(
        serializer.data
    )
