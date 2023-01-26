from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def choices(cls):
        result = []
        for x in cls:
            if not callable(x):
                result.append((x.name, x.value))
        return result
