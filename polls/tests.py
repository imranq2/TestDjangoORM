from typing import List, Any

from django.test import TestCase
from django.test.utils import override_settings

from automapper.automapper import AutoMapper
from automapper.classes.my_author import MyAuthor
from automapper.classes.my_question import MyQuestion, MyChoice
from polls.models import Question, Choice


class QuestionTestCase(TestCase):
    # def setUp(self):
    #     # Question.objects.create(name="1", question_text="What is your name?", pub_date="2020-01-01")
    #     # Question.objects.create(name="2", question_text="Where do you live?", pub_date="2020-01-01")
    #
    # def test_questions_can_speak(self):
    #     first = Question.objects.get(name="1")
    #     second = Question.objects.get(name="2")
    #     self.assertEqual(first.question_text, 'What is your name?')
    #     self.assertEqual(second.question_text, 'Where do you live?')
    #     first.choice_set.add(
    #         Choice.objects.create(
    #             question_id=1,
    #             choice_text="1",
    #             votes=1
    #         ),
    #         Choice.objects.create(
    #             question_id=1,
    #             choice_text="2",
    #             votes=2
    #         )
    #     )
    #     print(first)

    # noinspection PyMethodMayBeStatic
    @override_settings(DEBUG=True)
    def test_automapper(self):
        obj = Question.objects.filter(name="1").first()

        automapper = AutoMapper().map(
            lambda row: MyQuestion(
                name=row["name"],
                question_text=row["question_text"],
                pub_date=row["pub_date"],
                author=MyAuthor(
                  name="Potter"
                ),
                choices=[
                    MyChoice(
                        choice_text="Choice1",
                        votes=1
                    ),
                    MyChoice(
                        choice_text="Choice2",
                        votes=2
                    )
                ]
            )
        )
        print("---------- first pass -----------")
        result: List[Any] = automapper.transform([
            {
                "name": "1",
                "question_text": "What is your name?",
                "pub_date": "2020-01-01",
            },
            {
                "name": "2",
                "question_text": "Where do you live?",
                "pub_date": "2020-01-02"
            },
        ])
        print("---------- second pass ----------")
        result2: List[Any] = automapper.transform([
            {
                "name": "1",
                "question_text": "What is your name?",
                "pub_date": "2020-01-01",
            },
            {
                "name": "2",
                "question_text": "Where do you live?",
                "pub_date": "2020-01-02"
            },
        ])
        print(result)
