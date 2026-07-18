from django.core.management.base import BaseCommand
from quizzes.models import Question, Quiz
import openpyxl


class Command(BaseCommand):

    help = "Import questions from Excel file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)


    def handle(self, *args, **kwargs):

        file_path = kwargs["file_path"]

        workbook = openpyxl.load_workbook(file_path)

        sheet = workbook.active


        for row in sheet.iter_rows(min_row=2, values_only=True):

            (
                quiz_id,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                difficulty,
                correct_option,
                explanation
            ) = row


            quiz = Quiz.objects.get(id=quiz_id)


            Question.objects.create(
                quiz=quiz,
                question_text=question_text,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                difficulty=difficulty,
                correct_option=correct_option,
                explanation=explanation
            )


        self.stdout.write(
            self.style.SUCCESS(
                "Questions imported successfully!"
            )
        )