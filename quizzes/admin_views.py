import openpyxl

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ExcelUploadForm
from .models import Quiz, Question


def upload_questions(request):

    if request.method == "POST":

        form = ExcelUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            excel_file = request.FILES["excel_file"]

            workbook = openpyxl.load_workbook(
                excel_file
            )

            sheet = workbook.active

            count = 0

            for row in sheet.iter_rows(min_row=2, values_only=True):

                (
                    quiz_id,
                    question_text,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_option,
                    difficulty,
                ) = row

                try:

                    quiz = Quiz.objects.get(
                        id=quiz_id
                    )

                except Quiz.DoesNotExist:

                    continue

                Question.objects.create(

                    quiz=quiz,

                    question_text=question_text,

                    option_a=option_a,

                    option_b=option_b,

                    option_c=option_c,

                    option_d=option_d,

                    correct_option=correct_option,

                    difficulty=difficulty,

                )

                count += 1

            messages.success(
                request,
                f"{count} Questions Imported Successfully!"
            )

            return redirect("../")

    else:

        form = ExcelUploadForm()

    return render(
        request,
        "admin/upload_questions.html",
        {
            "form": form
        },
    )