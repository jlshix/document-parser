# coding: utf-8

"""标准值基类
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Literal, Any, Type, TypeVar

from pydantic import BaseModel


class BaseValue(BaseModel):
    """标准值基类"""
    type_name: Literal[""]

    @classmethod
    @abstractmethod
    def from_raw(cls, raw: Any) -> BaseValue:
        """从原始值构建"""

    @classmethod
    def subclasses(cls) -> dict[str, Type[BaseValue]]:
        """所有子类 type_name 与类型的对应关系"""
        rv = {}
        for sub in cls.__subclasses__():
            try:
                type_name = sub.__fields__["type_name"].type_.__dict__["__args__"][0]
                if not type_name:
                    raise ValueError(f"请指定{sub.__name__}的 type_name")
                rv[type_name] = sub
                if sub.__subclasses__():
                    rv.update(sub.subclasses())
            except KeyError as e:
                raise ValueError(f"请指定{sub.__name__}的 type_name") from e
        return rv


#: :class:`BaseValue` 的泛型
ValueT = TypeVar("ValueT", bound=BaseValue)
