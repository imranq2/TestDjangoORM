from django.db import models
from typing import Type, Union, TypeVar, Generic, Optional

_T = TypeVar("_T", bound=Union[models.Model])


class MyBase(Generic[_T]):
    def __init__(self):
        self.django_type: models.Model = _T

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def to_django(self, parent_id: Optional[int]) -> _T:
        raise NotImplementedError
