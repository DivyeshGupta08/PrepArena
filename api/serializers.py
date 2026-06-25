from rest_framework import serializers

from quizzes.models import Topic, Quiz, Question

class TopicSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Topic

        fields = '__all__'
        
class QuizSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Quiz

        fields = '__all__'
        
class QuestionSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Question

        fields = '__all__'