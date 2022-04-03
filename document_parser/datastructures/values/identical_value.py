# coding: utf-8

"""无需转换的原始值类型
"""

from __future__ import annotations

from typing import Literal, Any

from .base_value import BaseValue


class IdenticalValue(BaseValue):
    """无需转换的原始值类型"""
    type_name: Literal["identical"] = "identical"
    value: Any

    @classmethod
    def from_raw(cls, raw: Any) -> IdenticalValue:
        """从原始值构建"""
        return cls(value=raw)
