import datetime

from functools import partial, reduce
from itertools import chain, combinations
from typing import Any
from django.utils import timezone


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_from_dict(data_dict: dict, map_str: str, _default: Any = None):
    """Iterate nested dictionary
    input:
        data_dict = {"x": {"y": 1}}
        map_str = "x.y"
    output: _default or value
    """

    return reduce(
        lambda d, key: d.get(key, _default) if isinstance(d, dict) else _default,
        map_str.split("."),
        data_dict,
    )


def fast_dict_mapper(data_dict: dict):
    """
    Wraps get_from_dict and stores object
    """
    return partial(get_from_dict, data_dict)


def get_attribute(object, field):
    if object is None:
        return None
    attr = getattr(object, field)
    if isinstance(attr, datetime.datetime):
        attr = str(attr.astimezone(timezone.get_current_timezone()))
    return attr


if __name__ == "__main__":
    example1 = {"x": {"y": "z"}}

    assert get_from_dict(example1, "x.y") == "z"
    assert get_from_dict(example1, "x.y.z", "z") == "z"
    assert get_from_dict(example1, "3.y.z", "z") == "z"

    fdp = fast_dict_mapper(example1)
    assert fdp("x.y") == "z"
    assert fdp("x.y.z", "z") == "z"
