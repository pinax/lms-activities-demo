from __future__ import division

import random

from django import forms

from pinax.lms.activities.base import Survey, TwoChoiceQuiz, TwoChoiceWithAnswersQuiz


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


class MathQuiz(TwoChoiceWithAnswersQuiz):

    title = "Quick Math"
    description = "a simple little math quiz"
    repeatable = True

    def make_equation(self):
        num1 = random.choice(range(100))
        num2 = random.choice(range(100))
        op = random.choice(["+", "-", "*", "/"])
        equation = "{} {} {}".format(num1, op, num2)
        return (equation, eval(equation))

    def construct_quiz(self):
        quiz = []
        while len(quiz) < 10:
            equation, correct_answer = self.make_equation()
            _, wrong_answer = self.make_equation()
            question = "What is {}?".format(equation)
            answers = [correct_answer, wrong_answer]
            random.shuffle(answers)
            quiz.append(
                (question, answers, correct_answer)
            )
        return quiz
