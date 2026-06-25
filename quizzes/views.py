from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.utils import timezone

from .models import (
    Topic,
    Quiz,
    Question,
    QuizAttempt,
    UserAnswer
)


def topic_list(request):

    topics = Topic.objects.all()

    return render(
        request,
        'quizzes/topic_list.html',
        {
            'topics': topics
        }
    )
    
def quiz_list(request, topic_id):

    topic = get_object_or_404(
        Topic,
        id=topic_id
    )

    quizzes = Quiz.objects.filter(
        topic=topic,
        is_published=True
    )

    return render(
        request,
        'quizzes/quiz_list.html',
        {
            'topic': topic,
            'quizzes': quizzes
        }
    )
    
    
def quiz_start(request, quiz_id):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    question_count = quiz.question_set.count()

    return render(
        request,
        'quizzes/quiz_start.html',
        {
            'quiz': quiz,
            'question_count': question_count
        }
    )
    
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
                selected_answer.upper() ==
                question.correct_option.upper()
            )

            if is_correct:
                score += 1

            UserAnswer.objects.create(
                attempt=attempt,
                question=question,
                selected_option=selected_answer
                if selected_answer
                else "",
                is_correct=is_correct
            )

        percentage = (
            score /
            questions.count()
        ) * 100

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
    
def quiz_result(request, attempt_id):

    attempt = get_object_or_404(
        QuizAttempt,
        id=attempt_id
    )

    return render(
        request,
        'quizzes/result.html',
        {
            'attempt': attempt
        }
    )

def review_answers(request, attempt_id):

    attempt = get_object_or_404(
        QuizAttempt,
        id=attempt_id
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