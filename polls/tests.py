from django.test import TestCase
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
