# coding: utf-8

"""任意值包装类型
"""

from __future__ import annotations

from typing import Literal, Any

from .base_value import BaseValue


class AnyValue(BaseValue):
    """任意值包装类型"""
    type_name: Literal["any"] = "any"
    value: Any

    @classmethod
    def from_raw(cls, raw: Any) -> AnyValue:
        """从原始值构建"""
        return cls(value=raw)
