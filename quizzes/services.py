from google import genai
from decouple import config
from .models import AIFeedback
import re
import traceback

client = genai.Client(
    api_key=config("GEMINI_API_KEY")
)


def generate_feedback(attempt):

    user = attempt.user
    quiz = attempt.quiz

    total_questions = quiz.questions.count()
    correct = attempt.answers.filter(is_correct=True).count()
    wrong = total_questions - correct
    percentage = attempt.percentage

    prompt = f"""
You are an expert interview mentor.

A student attempted a quiz.

Topic:
{quiz.topic.name}

Quiz:
{quiz.title}

Score:
{correct}/{total_questions}

Percentage:
{percentage:.2f}%

Wrong Answers:
{wrong}

Generate ONLY these sections exactly.

Strengths:
Weaknesses:
Recommendations:

Do not use markdown.
Keep each section under 80 words.
"""

    strengths = ""
    weaknesses = ""
    recommendations = ""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        print("\n========== GEMINI RESPONSE ==========")
        print(text)
        print("=====================================\n")

        strength_match = re.search(
            r"Strengths:\s*(.*?)\s*Weaknesses:",
            text,
            re.DOTALL | re.IGNORECASE,
        )

        weakness_match = re.search(
            r"Weaknesses:\s*(.*?)\s*Recommendations:",
            text,
            re.DOTALL | re.IGNORECASE,
        )

        recommendation_match = re.search(
            r"Recommendations:\s*(.*)",
            text,
            re.DOTALL | re.IGNORECASE,
        )

        if strength_match:
            strengths = strength_match.group(1).strip()

        if weakness_match:
            weaknesses = weakness_match.group(1).strip()

        if recommendation_match:
            recommendations = recommendation_match.group(1).strip()

    except Exception:

        print("\n========== GEMINI ERROR ==========")
        traceback.print_exc()
        print("==================================\n")

        strengths = "You have a basic understanding of the topic."

        weaknesses = "Some concepts need additional practice."

        recommendations = (
            "Review the incorrect answers and attempt another quiz."
        )

    feedback, created = AIFeedback.objects.get_or_create(
        attempt=attempt,
        defaults={
            "user": user,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendations": recommendations,
        },
    )

    if not created:
        feedback.strengths = strengths
        feedback.weaknesses = weaknesses
        feedback.recommendations = recommendations
        feedback.save()

    return feedback