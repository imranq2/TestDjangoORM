from typing import Optional, Dict, Any
from django.db import models
from django.db.models import QuerySet

from automapper.classes.my_base import MyBase
from polls.models import Choice


class MyChoice(MyBase[Choice]):
    def __init__(self, choice_text: str, votes: int):
        super().__init__()
        self.choice_text = choice_text
        self.votes = votes
        self.keys = ["choice_text"]

    def __str__(self):
        return f"choice_text={self.choice_text}, votes={self.votes}"

    def to_django(self, parent: Optional[models.Model]) -> Choice:
        obj: Choice = Choice(
            question=parent,
            choice_text=self.choice_text,
            votes=self.votes
        )
        obj.save()
        return obj

    def get_obj_from_database(self) -> Choice:
        key_args: Dict[str, Any] = self.get_key_args()
        q: QuerySet = Choice.objects.filter(**key_args)
        obj: Choice = q.first()
        return obj

    def get_key_args(self) -> Dict[str, Any]:
        key_args: Dict[str, Any] = {key: self.__getattribute__(key) for key in self.keys}
        return key_args
