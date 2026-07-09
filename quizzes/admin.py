from django.contrib import admin

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer,
    AIFeedback
)

admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizAttempt)
admin.site.register(UserAnswer)
admin.site.register(AIFeedback)

list_display = (
    'question_text',
    'quiz'
)