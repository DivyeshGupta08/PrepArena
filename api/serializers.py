from rest_framework import serializers

from quizzes.models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt
)


class TopicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Topic

        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):

    class Meta:

        model = Quiz

        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question

        fields = "__all__"


class QuizSubmissionSerializer(
    serializers.Serializer
):

    quiz_id = serializers.IntegerField()

    answers = serializers.DictField(
        child=serializers.CharField()
    )
    
class QuizAttemptSerializer(
    serializers.ModelSerializer
):

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    quiz_title = serializers.CharField(
        source='quiz.title',
        read_only=True
    )

    topic = serializers.CharField(
        source='quiz.topic.name',
        read_only=True
    )

    class Meta:

        model = QuizAttempt

        fields = [

            'id',

            'username',

            'quiz',

            'quiz_title',

            'topic',

            'score',

            'percentage',

            'started_at',

            'submitted_at',

            'duration_seconds'
        ]