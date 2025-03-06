
import typing

from jsonified import JsonifiedProperty


class A(JsonifiedProperty):
    field = "value"

    def __init__(
        self,
        value: typing.Any
    ):

        self.value = value


class B(JsonifiedProperty):
    field = None

    def __init__(
        self,
        value: typing.Any
    ):

        self.value = value


class C(JsonifiedProperty):
    field = "QWERTY"

    def __init__(
        self,
        value: typing.Any
    ):

        self.value = value


class D(JsonifiedProperty):
    field = "QWERTY"


def test_field_errors_property():
    tests = [
        [A, None],
        [B, TypeError],
        [C, KeyError],
        [D, NotImplementedError],
    ]

    for inp, out in tests:
        try:
            inp(value=None)
            res = None

        except Exception as err:
            res = err

        if None in [res, out]:
            assert res is out

        else:
            assert res.__class__ == out


def test_field_value_errors_property():
    tests = [
        [0, None],
        ["", None],
        [None, None],
        [[], TypeError],
        [{}, TypeError],
        [A(value=1), TypeError]
    ]

    for inp, out in tests:
        try:
            A(value=inp).to_dict()
            res = None

        except Exception as err:
            res = err

        if None in [res, out]:
            assert res is out

        else:
            assert res.__class__ == out


def test_values_property():
    tests = [
        "hello", 123, None
    ]

    for test in tests:
        assert A(value=test).to_dict() == test
