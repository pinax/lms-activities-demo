import random

from pinax.lms.activities.base import TwoChoiceWithAnswersQuiz

from .models import Vocabulary


class VocabQuiz(TwoChoiceWithAnswersQuiz):

    title = "Vocabulary Test"
    description = "a vocab test with data sourced from database"
    repeatable = True

    def construct_quiz(self):
        quiz = []
        for word in Vocabulary.objects.all():
            question = "What is the word for: {}".format(word.definition)
            correct_answer = word.word
            answers = [correct_answer, random.choice(Vocabulary.objects.exclude(pk=word.pk)).word]
            random.shuffle(answers)
            quiz.append(
                (question, answers, correct_answer)
            )
        return quiz
