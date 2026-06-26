from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from quizzes.models import Topic, Quiz, Question, QuizAttempt, UserAnswer
from .serializers import TopicSerializer, QuizSerializer, QuestionSerializer, QuizSubmissionSerializer, QuizAttemptSerializer
from django.utils import timezone

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