from django.shortcuts import render, redirect
from .forms import QuestionForm
from quizzes.models import Quiz, Question



def admin_dashboard(request):

    context = {
        "total_quizzes": Quiz.objects.count(),
        "total_questions": Question.objects.count(),
    }

    return render(
        request,
        "admin_panel/dashboard.html",
        context
    )



def add_question(request):

    if request.method == "POST":

        form = QuestionForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                "admin_panel:add_question"
            )

    else:

        form = QuestionForm()


    return render(
        request,
        "admin_panel/add_question.html",
        {
            "form": form
        }
    )