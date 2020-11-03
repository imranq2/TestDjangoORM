from django.db import models
from typing import Type, Union, TypeVar, Generic, Optional, Dict, Any, List

_T = TypeVar("_T", bound=Union[models.Model])


class MyBase(Generic[_T]):
    def __init__(self):
        self.django_type: models.Model = _T
        self.keys: List[str] = []

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def to_django(self, parent: Optional[models.Model]) -> _T:
        raise NotImplementedError

    def update(self, obj: _T) -> _T:
        raise NotImplementedError
