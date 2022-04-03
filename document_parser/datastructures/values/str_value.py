# coding: utf-8

"""字符串包装类型
"""

from __future__ import annotations

from typing import Literal, Any

from .identical_value import IdenticalValue


class StrValue(IdenticalValue):
    """创建字符串包装类型"""
    type_name: Literal["str"] = "str"

    @classmethod
    def from_raw(cls, raw: Any) -> StrValue:
        """创建字符串类型"""
        return cls(value=str(raw))
