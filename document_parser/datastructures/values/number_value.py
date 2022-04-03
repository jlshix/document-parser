# coding: utf-8

"""数字包装类型
"""

from __future__ import annotations

from typing import Literal, Any

from .identical_value import IdenticalValue


class NumberValue(IdenticalValue):
    """字符串包装类型"""
    type_name: Literal["number"] = "number"

    @classmethod
    def from_raw(cls, raw: Any) -> NumberValue:
        """创建数字包装类型"""
        return cls(value=float(raw))
