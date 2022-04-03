# coding: utf-8

"""解析值类型
"""

from typing import Any, Optional

from pydantic import BaseModel

from .values import parse_raw
from .values.base_value import ValueT


class Content(BaseModel):
    """解析值类型"""

    #: 字段名
    key: str

    #: 字段值
    value: ValueT

    #: 原始值, 与 value 一致时用 None 表示
    raw: Optional[Any]

    #: 附加属性, 若无则用 None 表示
    extra: Optional[dict]

    @classmethod
    def create(cls, type_name: str, key: str, raw: Any, **extra):
        """创建实例"""
        value = parse_raw(type_name=type_name, key=key, raw=raw)
        rv = cls(
            key=key,
            value=value,
            raw=None if type_name == "identical" else raw,
            extra=extra or None
        )
        return rv


#: 解析结果列表
Contents = list[Content]
