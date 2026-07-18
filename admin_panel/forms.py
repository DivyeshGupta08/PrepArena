from django import forms
from quizzes.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question

        fields = [
            "quiz",
            "question_text",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "difficulty",
            "correct_option",
            "explanation",
        ]

        widgets = {

            "question_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "option_a": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "option_b": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "option_c": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "option_d": forms.TextInput(
                    attrs={
                    "class": "form-control"
                }
            ),

            "difficulty": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "correct_option": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "explanation": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }