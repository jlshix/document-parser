# coding: utf-8

"""标准值基类
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Literal, Any

from pydantic import BaseModel


class BaseValue(BaseModel):
    """标准值基类"""
    type_name: Literal[""]

    @classmethod
    @abstractmethod
    def from_raw(cls, raw: Any) -> BaseValue:
        """从原始值构建"""
