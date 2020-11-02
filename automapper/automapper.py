from typing import List, Any


class AutoMapper:
    def __int__(self):
        self.func = None

    def map(self, func):
        self.func = func
        return self

    def transform(self, data: List[Any]):
        result = [
            self.func(row) for row in data
        ]
        return result
