from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.utils import timezone

from django.contrib.auth.decorators import login_required

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer
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

        return redirect(
            'quiz_result',
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

    return render(
        request,
        'quizzes/result.html',
        {
            'attempt': attempt
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