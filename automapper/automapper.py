from django.db import models
from django.db import transaction

from typing import List, Any, Union, Dict

from automapper.classes.my_base import MyBase


class AutoMapper:
    def __int__(self):
        self.func = None

    def map(self, func):
        self.func = func
        return self

    def transform_simple(self, data: List[Union[str, Dict[str, Any], List[Dict[str, Any]]]]):
        result = [
            self.func(row) for row in data
        ]
        return result

    # @transaction.atomic
    def transform(self, data: List[Union[str, Dict[str, Any], List[Dict[str, Any]]]]) -> List[models.Model]:
        result: List[MyBase] = self.transform_simple(data=data)
        result_django: List[models.Model] = [
            obj.to_django(parent=None) for obj in result
        ]
        return result_django

    def convert_to_django(self,
                          entities: List[Union[str, MyBase, List[MyBase]]],
                          parent: MyBase,
                          property_name: str
                          ):
        # now you have a simple Python object
        # there are 3 cases:
        # 1. property is a simple property so just assign
        # 2. property is a dict (i.e., struct).  use xx.objects.create() and assign
        #   recurse into the struct
        if isinstance(entities, MyBase):
            parent[property_name] = entities.django_type.objects.create(MyBase.to_django())
        # 3. property is a list.  use xx.objects.create() for each item which would be a struct)
        #   and recurse and then add to collection
