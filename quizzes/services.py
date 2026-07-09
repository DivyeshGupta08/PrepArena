from .models import AIFeedback


def generate_feedback(attempt):

    user = attempt.user

    percentage = attempt.percentage

    strengths = ""

    weaknesses = ""

    recommendations = ""

    if percentage >= 80:

        strengths = (
            "Excellent performance. You have a strong understanding of this topic."
        )

        weaknesses = (
            "No major weaknesses detected."
        )

        recommendations = (
            "Continue practicing advanced interview questions to maintain your performance."
        )

    elif percentage >= 50:

        strengths = (
            "You have a good understanding of the basic concepts."
        )

        weaknesses = (
            "Some concepts still require more revision."
        )

        recommendations = (
            "Revise the weak topics and solve more practice quizzes."
        )

    else:

        strengths = (
            "You attempted the quiz and identified your learning gaps."
        )

        weaknesses = (
            "Your fundamentals need improvement."
        )

        recommendations = (
            "Review the study material carefully and practice beginner-level questions before attempting this quiz again."
        )

    feedback = AIFeedback.objects.create(

        user=user,

        attempt=attempt,

        strengths=strengths,

        weaknesses=weaknesses,

        recommendations=recommendations

    )

    return feedback