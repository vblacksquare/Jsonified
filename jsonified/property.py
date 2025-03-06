
from .base import BaseJsonifed


class JsonifiedProperty(metaclass=BaseJsonifed):
    field = "base"

    def __check_init__(self, *args, **kwargs):
        field_type = type(self.field)
        if field_type not in [str]:
            raise TypeError(f"{self}'s field type must be str, not {field_type}")

        try:
            self.__getattribute__(self.field)

        except AttributeError:
            raise KeyError(f"{self} doesn't have any field with name: \"{self.field}\"")

    def to_dict(self) -> dict:
        value = self.__getattribute__(self.field)

        if not value is None:
            value_type = type(value)
            valied_types = [int, str]

            if value_type not in valied_types:
                raise TypeError(
                    f"{self.__class__}'s field have to be {valied_types} or {None} not {value_type}"
                )

        return value
