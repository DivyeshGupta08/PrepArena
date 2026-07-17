from django.contrib import admin

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer,
    AIFeedback
)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = (
        "name",
    )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "time_limit_minutes",
        "is_published",
    )
    list_filter = (
        "topic",
        "is_published",
    )
    search_fields = (
        "title",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question_text",
        "quiz",
        "difficulty",
        "correct_option",
    )
    list_filter = (
        "quiz",
        "difficulty",
    )
    search_fields = (
        "question_text",
    )


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quiz",
        "score",
        "percentage",
        "submitted_at",
    )
    list_filter = (
        "quiz",
    )


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "attempt",
        "question",
        "selected_option",
        "is_correct",
    )


@admin.register(AIFeedback)
class AIFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "attempt",
        "created_at",
    )