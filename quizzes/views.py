from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.utils import timezone
from django.db.models import Avg
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from .services import generate_feedback

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer,
    AIFeedback
)


def topic_list(request):

    search_query = request.GET.get(
        'search',
        ''
    )

    topics = Topic.objects.all()

    if search_query:

        topics = topics.filter(
            name__icontains=search_query
        )

    return render(
        request,
        'quizzes/topic_list.html',
        {
            'topics': topics,
            'search_query': search_query
        }
    )


def quiz_list(request, topic_id):

    topic = get_object_or_404(
        Topic,
        id=topic_id
    )

    search_query = request.GET.get(
        'search',
        ''
    )

    quizzes = Quiz.objects.filter(
        topic=topic,
        is_published=True
    )

    if search_query:

        quizzes = quizzes.filter(
            title__icontains=search_query
        )

    return render(
        request,
        'quizzes/quiz_list.html',
        {
            'topic': topic,
            'quizzes': quizzes,
            'search_query': search_query
        }
    )


@login_required
def quiz_start(request, quiz_id):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    question_count = quiz.questions.count()

    return render(
        request,
        'quizzes/quiz_start.html',
        {
            'quiz': quiz,
            'question_count': question_count
        }
    )


@login_required
def take_quiz(request, quiz_id):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    questions = Question.objects.filter(
        quiz=quiz
    )

    if request.method == "POST":

        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz
        )

        score = 0

        for question in questions:

            selected_answer = request.POST.get(
                f"question_{question.id}"
            )

            is_correct = (
                selected_answer
                and
                selected_answer.upper() ==
                question.correct_option.upper()
            )

            if is_correct:
                score += 1

            UserAnswer.objects.create(
                attempt=attempt,
                question=question,
                selected_option=selected_answer if selected_answer else "",
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

# -----------------------------------
# Update User Profile
# -----------------------------------

        profile = request.user.profile
        
        # -----------------------------------
# Daily Streak System
# -----------------------------------

        today = timezone.now().date()

        if profile.last_activity is None:

            profile.streak = 1

        elif profile.last_activity == today:

    # Already active today
            pass

        elif profile.last_activity == today - timedelta(days=1):

            profile.streak += 1

        else:

            profile.streak = 1

        profile.last_activity = today

        profile.total_attempts += 1
        
        

        attempts = QuizAttempt.objects.filter(user=request.user)

        profile.overall_average = round(
            attempts.aggregate(
                Avg("percentage")
            )["percentage__avg"] or 0,
            2
        )

# XP System
        xp_earned = int(percentage)

        profile.xp += xp_earned

# Level System
        profile.level = (profile.xp // 100) + 1
        
        # -----------------------------------
# Badge System
# -----------------------------------

        badges = 0

# First Quiz
        if profile.total_attempts >= 1:
            badges += 1

# 5 Quizzes
        if profile.total_attempts >= 5:
            badges += 1

# 10 Quizzes
        if profile.total_attempts >= 10:
            badges += 1

# 500 XP
        if profile.xp >= 500:
            badges += 1

# 7-Day Streak
        if profile.streak >= 7:
            badges += 1

# Perfect Score
        if percentage == 100:
            badges += 1

        profile.badges = badges

        profile.save()

        return redirect(
            "quiz_result",
            attempt.id
        )

    return render(
        request,
        'quizzes/take_quiz.html',
        {
            'quiz': quiz,
            'questions': questions
        }
    )


@login_required
def quiz_result(request, attempt_id):

    attempt = get_object_or_404(
        QuizAttempt,
        id=attempt_id,
        user=request.user
    )

    feedback, created = AIFeedback.objects.get_or_create(
        attempt=attempt,
        defaults={
            "user": request.user
        }
    )

    if created:
        feedback = generate_feedback(attempt)

    percentage = attempt.percentage

    if percentage >= 80:

        grade = "A"

        message = "Excellent performance! Keep it up."

    elif percentage >= 60:

        grade = "B"

        message = "Good job! A little more practice will make you even better."

    elif percentage >= 40:

        grade = "C"

        message = "Average performance. Focus on your weak areas."

    else:

        grade = "D"

        message = "Keep practicing. You'll improve with consistency."

    return render(
        request,
        "quizzes/result.html",
        {
            "attempt": attempt,
            "feedback": feedback,
            "grade": grade,
            "message": message,
        }
    )


@login_required
def review_answers(request, attempt_id):

    attempt = get_object_or_404(
        QuizAttempt,
        id=attempt_id,
        user=request.user
    )

    answers = UserAnswer.objects.filter(
        attempt=attempt
    )

    return render(
        request,
        'quizzes/review_answers.html',
        {
            'attempt': attempt,
            'answers': answers
        }
    )