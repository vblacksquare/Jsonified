
from abc import ABC, abstractmethod
import json


class BaseJsonifed(type, ABC):
    def __new__(cls, name, bases, dct):
        original_init = dct.get('__init__')

        def new_init(self: "BaseJsonifed", *args, **kwargs):
            if not original_init:
                raise NotImplementedError(f"{cls} doesn't implement __init__ method")

            original_init(self, *args, **kwargs)
            self.__check_init__(self, *args, **kwargs)

        dct['__init__'] = new_init
        return super().__new__(cls, name, bases, dct)

    @abstractmethod
    def __check_init__(self, *args, **kwargs):
        return

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
