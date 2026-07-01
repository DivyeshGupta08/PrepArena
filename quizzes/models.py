from django.db import models
from django.contrib.auth.models import User


OPTION_CHOICES = [

    ('A', 'Option A'),

    ('B', 'Option B'),

    ('C', 'Option C'),

    ('D', 'Option D'),

]


class Topic(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="quizzes"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    time_limit_minutes = models.PositiveIntegerField()

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)

    option_b = models.CharField(max_length=255)

    option_c = models.CharField(max_length=255)

    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICES
    )

    explanation = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.question_text[:50]


class QuizAttempt(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quiz_attempts"
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    score = models.PositiveIntegerField(default=0)

    percentage = models.FloatField(default=0)

    started_at = models.DateTimeField(auto_now_add=True)

    submitted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    duration_seconds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"


class UserAnswer(models.Model):

    attempt = models.ForeignKey(
        QuizAttempt,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    selected_option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICES,
        blank=True
    )

    is_correct = models.BooleanField(default=False)