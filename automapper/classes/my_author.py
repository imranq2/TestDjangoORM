from typing import Optional
from django.db import models

from automapper.classes.my_base import MyBase
from polls.models import Author


class MyAuthor(MyBase[Author]):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    def __str__(self):
        return f"name={self.name}"

    def to_django(self, parent: Optional[models.Model]) -> Author:
        obj: Author = Author(
            name=self.name,
        )
        obj.save()
        return obj
