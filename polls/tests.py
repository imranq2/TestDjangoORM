from typing import List, Any

from django.test import TestCase

from automapper.automapper import AutoMapper
from polls.models import Question


class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(name="1", question_text="What is your name?", pub_date="2020-01-01")
        Question.objects.create(name="2", question_text="Where do you live?", pub_date="2020-01-01")

    def test_questions_can_speak(self):
        first = Question.objects.get(name="1")
        second = Question.objects.get(name="2")
        self.assertEqual(first.question_text, 'What is your name?')
        self.assertEqual(second.question_text, 'Where do you live?')

    # noinspection PyMethodMayBeStatic
    def test_automapper(self):
        automapper = AutoMapper().map(
            lambda row: Question.objects.create(
                name=row["name"],
                question_text=row["question_text"],
                pub_date=row["pub_date"]
            )
        )
        result: List[Any] = automapper.transform([
            {
                "name": "1",
                "question_text": "What is your name?",
                "pub_date": "2020-01-01"
            },
            {
                "name": "2",
                "question_text": "Where do you live?",
                "pub_date": "2020-01-02"
            }
        ])
        print(result)
