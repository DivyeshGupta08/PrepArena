import openpyxl

from .models import Quiz, Question


def import_questions_from_excel(file):

    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    count = 0

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if not row:
            continue

        quiz_id = row[0]
        question_text = row[1]
        option_a = row[2]
        option_b = row[3]
        option_c = row[4]
        option_d = row[5]
        correct_option = str(row[6]).strip().upper()

        if not quiz_id or not question_text:
            continue

        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            continue

        # Skip duplicate questions
        if Question.objects.filter(
            quiz=quiz,
            question_text=question_text
        ).exists():
            continue

        Question.objects.create(
            quiz=quiz,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option
        )

        count += 1

    return count