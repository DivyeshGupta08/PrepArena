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


class QuizSerializer(
    serializers.ModelSerializer
):

    topic_name = serializers.CharField(
        source='topic.name',
        read_only=True
    )

    class Meta:

        model = Quiz

        fields = [

            'id',

            'title',

            'description',

            'topic',

            'topic_name',

            'time_limit_minutes',

            'is_published',

            'created_at'
        ]


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

    quiz = QuizSerializer(
        read_only=True
    )

    class Meta:

        model = QuizAttempt

        fields = [

            'id',

            'username',

            'quiz',

            'score',

            'percentage',

            'started_at',

            'submitted_at',

            'duration_seconds'
        ]
        
class DashboardSerializer(
    serializers.Serializer
):

    total_attempts = serializers.IntegerField()

    average_percentage = serializers.FloatField()

    highest_score = serializers.IntegerField()

    lowest_score = serializers.IntegerField()

    weak_topic = serializers.CharField()

    strong_topic = serializers.CharField()

    grade = serializers.CharField()

    interview_readiness = serializers.FloatField()

    recommendation = serializers.CharField()
    
class LeaderboardSerializer(
    serializers.Serializer
):

    username = serializers.CharField()

    best_score = serializers.IntegerField()

    average_percentage = serializers.FloatField()