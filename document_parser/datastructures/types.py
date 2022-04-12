# coding: utf-8

"""用于类型注解
"""

from typing import Union

StrSet = set[str]

StrOrDict = Union[str, dict]
Parsed = dict[str, list[StrOrDict]]
