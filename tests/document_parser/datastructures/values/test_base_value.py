# coding: utf-8

"""base_value.py 的测试
"""

from __future__ import annotations

from typing import Literal

from document_parser.datastructures.values.base_value import BaseValue


class ExclamationSentenceValue(BaseValue):
    """从字符串语句创建叹号结尾的 Value"""
    type_name: Literal["test"] = "exclamation"
    value: str

    @classmethod
    def from_raw(cls, raw: str) -> ExclamationSentenceValue:
        """创建实例"""
        return cls(value=f"{raw} !")


def test_base_value_sub_class():
    """测试子类的使用"""
    v = ExclamationSentenceValue.from_raw("yes i do")
    assert v.value == "yes i do !"
