from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from quizzes.models import Topic, Quiz, Question
from .serializers import TopicSerializer, QuizSerializer, QuestionSerializer

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