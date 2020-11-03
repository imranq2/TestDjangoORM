from typing import List, Optional, Dict, Any
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
        super().__init__()
        self.name: str = name
        self.question_text = question_text
        self.pub_date = pub_date
        self.author = author
        self.choices: List[MyChoice] = choices
        self.keys = ["name"]

    def __str__(self):
        return f"name={self.name}, question_text={self.question_text}, pub_date={self.pub_date}" + \
               ",".join([str(c) for c in self.choices])

    def to_django(self, parent: Optional[models.Model]) -> Question:
        # see if question already exists
        obj: Question = self.get_obj_from_database()
        # if author exists then use that otherwise create one
        author = self.author.get_obj_from_database() or self.author.to_django(None)
        if obj:
            # check if all the fields are the same.  If not, update them
            obj.name = self.name
            obj.question_text = self.question_text
            obj.pub_date = self.pub_date,
            obj.author = author
        else:
            # create the question
            obj = Question(
                name=self.name,
                question_text=self.question_text,
                pub_date=self.pub_date,
                author=author
            )
            obj.save()
        for choice in self.choices:
            # first see if it already exists
            choice_in_db = obj.choice_set.filter(**choice.get_key_args()).first()
            if not choice_in_db:
                obj.choice_set.add(choice.to_django(parent=obj))
        return obj

    def get_obj_from_database(self) -> Question:
        key_args: Dict[str, Any] = self.get_key_args()
        obj: Question = Question.objects.filter(**key_args).first()
        return obj

    def get_key_args(self) -> Dict[str, Any]:
        key_args: Dict[str, Any] = {key: self.__getattribute__(key) for key in self.keys}
        return key_args
