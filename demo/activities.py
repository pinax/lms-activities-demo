from django import forms

from pinax.lms.activities.base import Survey, TwoChoiceQuiz


class SuggestionBox(Survey):

    title = "Suggestion Box"
    description = "make a suggestion on how to improve the site"

    repeatable = True

    questions = [
        {
            "name": "suggestion",
            "label": "Suggestion",
            "field_class": forms.CharField,
            "extra_args": {
                "widget": forms.Textarea(attrs={"rows": "5", "class": "col-md-8"}),
            }
        }
    ]


class WouldYouRatherQuiz(TwoChoiceQuiz):

    title = "Would You Rather"
    description = "A simple would you rather game"
    repeatable = True

    def construct_quiz(self):
        return [
            ("Would you rather: ", ["eat a live cockroach", "speak in front of a live audience"]),
            ("Would you rather: ", ["win the World Series", "win the Superbowl"]),
            ("Would you rather: ", ["eat chicken", "eat steak"]),
            ("Would you rather: ", ["drink wine", "drink whiskey"]),
            ("Would you rather: ", ["collect goats", "collect stamps"]),
            ("Would you rather: ", ["watch a movie at home alone", "watch live music in a crowded bar with friends"]),
        ]
