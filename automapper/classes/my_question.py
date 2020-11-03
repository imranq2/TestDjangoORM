from typing import List, Optional
from django.db import models

from automapper.classes.my_author import MyAuthor
from automapper.classes.my_base import MyBase
from automapper.classes.my_choice import MyChoice
from polls.models import Question


class MyQuestion(MyBase[Question]):
    def __init__(self,
                 name: str,
                 question_text: str,
                 pub_date: str,
                 author: MyAuthor,
                 choices: List[MyChoice]):
        self.name: str = name
        self.question_text = question_text
        self.pub_date = pub_date
        self.author = author
        self.choices: List[MyChoice] = choices
        super().__init__()

    def __str__(self):
        return f"name={self.name}, question_text={self.question_text}, pub_date={self.pub_date}" + \
               ",".join([str(c) for c in self.choices])

    def to_django(self, parent: Optional[models.Model]) -> Question:
        obj: Question = Question(
            name=self.name,
            question_text=self.question_text,
            pub_date=self.pub_date,
            author=self.author.to_django(None)
        )
        obj.save()
        for choice in self.choices:
            obj.choice_set.add(choice.to_django(parent=obj))
        return obj
