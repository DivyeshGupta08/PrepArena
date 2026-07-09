import google.generativeai as genai

from decouple import config

from .models import AIFeedback


genai.configure(
    api_key=config("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_feedback(attempt):

    user = attempt.user

    quiz = attempt.quiz

    percentage = attempt.percentage

    total_questions = quiz.questions.count()

    correct_answers = attempt.answers.filter(
        is_correct=True
    ).count()

    wrong_answers = total_questions - correct_answers

    topic_name = quiz.topic.name

    prompt = f"""
You are an expert interview mentor.

Analyze the following quiz result.

Topic:
{topic_name}

Quiz Score:
{percentage:.2f}%

Correct Answers:
{correct_answers}

Wrong Answers:
{wrong_answers}

Provide feedback in three sections.

Strengths:
Weaknesses:
Recommendations:

Keep the feedback professional, encouraging and concise.
"""

    try:

        response = model.generate_content(
            prompt
        )

        ai_feedback = response.text

        strengths = ai_feedback

        weaknesses = ""

        recommendations = ""

    except Exception:

        if percentage >= 80:

            strengths = (
                f"You answered {correct_answers} out of "
                f"{total_questions} questions correctly. "
                f"You have an excellent understanding of "
                f"{topic_name}."
            )

            weaknesses = (
                "Very few mistakes were detected."
            )

            recommendations = (
                "Practice advanced interview questions "
                "to further strengthen your skills."
            )

        elif percentage >= 60:

            strengths = (
                "Your fundamentals are good."
            )

            weaknesses = (
                f"You missed {wrong_answers} questions."
            )

            recommendations = (
                "Revise important concepts and attempt "
                "another quiz."
            )

        elif percentage >= 40:

            strengths = (
                "You have a basic understanding."
            )

            weaknesses = (
                "Your concepts are not yet consistent."
            )

            recommendations = (
                "Review the basics and practice more."
            )

        else:

            strengths = (
                "Good effort attempting the quiz."
            )

            weaknesses = (
                "Your fundamentals need improvement."
            )

            recommendations = (
                "Study the basics carefully and "
                "practice beginner-level questions."
            )

    feedback, created = AIFeedback.objects.get_or_create(

        attempt=attempt,

        defaults={

            "user": user,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "recommendations": recommendations,
        }
    )

    if not created:

        feedback.strengths = strengths

        feedback.weaknesses = weaknesses

        feedback.recommendations = recommendations

        feedback.save()

    return feedback