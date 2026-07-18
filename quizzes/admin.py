from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer,
    AIFeedback,
)

from .admin_views import upload_questions


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

    def get_urls(self):

        urls = super().get_urls()

        custom_urls = [

            path(
                "upload-excel/",
                self.admin_site.admin_view(upload_questions),
                name="question-upload-excel",
            ),

        ]

        return custom_urls + urls

    change_list_template = "admin/question_change_list.html"


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