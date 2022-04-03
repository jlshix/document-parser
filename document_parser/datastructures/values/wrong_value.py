# coding: utf-8

"""值转换失败时使用此值作为代替, 说明转换失败的状态
"""

from __future__ import annotations

from typing import Literal

from .base_value import BaseValue


class WrongValue(BaseValue):
    """错误值类型"""
    type_name: Literal["_wrong"] = "_wrong"

    #: 错误信息
    message: str

    @classmethod
    def from_raw(cls, message: str) -> WrongValue:  # pylint: disable=arguments-renamed
        """创建错误值类型, 不应手动调用, 会在转换失败时以此值代替"""
        return cls(message=message)
