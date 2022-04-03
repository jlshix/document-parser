# coding: utf-8

"""标准值
"""

from functools import lru_cache
from typing import Any, Callable

from .base_value import BaseValue, ValueT
from .wrong_value import WrongValue


@lru_cache
def parse_function(type_name: str) -> Callable[[Any], ValueT]:
    """根据类型名称推断解析函数"""
    value_types = BaseValue.subclasses()
    try:
        return value_types[type_name].from_raw
    except KeyError as e:
        msg = f"类型名称 {type_name} 未注册; 已注册的类型名称为: {tuple(value_types.keys())}"
        raise ValueError(msg) from e


def parse_raw(type_name: str, key: str, raw: Any) -> ValueT:
    """解析原始值为 :class:`BaseValue` 的子类实例"""
    func = parse_function(type_name=type_name)
    try:
        value = func(raw)
    except ValueError as e:
        value = WrongValue.from_raw(message=str(e))
    except Exception as e:  # pylint: disable=broad-except
        value = WrongValue.from_raw(message=f"解析失败: {type_name=}; {key=}; {raw=}; {type(e)=}; {e=}")
    return value
