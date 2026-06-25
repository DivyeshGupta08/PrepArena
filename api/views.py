from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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