from typing import Optional, Dict, Any
from django.db import models

from automapper.classes.my_base import MyBase
from polls.models import Author


class MyAuthor(MyBase[Author]):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.keys = ["name"]

    def __str__(self):
        return f"name={self.name}"

    def to_django(self, parent: Optional[models.Model]) -> Author:
        obj: Author = Author(
            name=self.name,
        )
        obj.save()
        return obj

    def get_obj_from_database(self) -> Author:
        key_args: Dict[str, Any] = self.get_key_args()
        obj: Author = Author.objects.filter(**key_args).first()
        return obj

    def get_key_args(self) -> Dict[str, Any]:
        key_args: Dict[str, Any] = {key: self.__getattribute__(key) for key in self.keys}
        return key_args
