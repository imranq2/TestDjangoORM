from typing import Optional
from django.db import models

from automapper.classes.my_base import MyBase
from polls.models import Choice


class MyChoice(MyBase[Choice]):
    def __init__(self, choice_text: str, votes: int):
        self.choice_text = choice_text
        self.votes = votes
        super().__init__()

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
