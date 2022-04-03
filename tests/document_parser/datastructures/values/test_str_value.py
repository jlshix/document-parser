# coding: utf-8

"""str_value.py 的测试
"""

from __future__ import annotations

from typing import Any

import pytest

from document_parser.datastructures.values.str_value import StrValue


@pytest.mark.parametrize(
    argnames="raw,value",
    argvalues=(
        (42, "42"),
        (None, 'None'),
        ("the force", "the force"),
    ),
)
def test_str_value(raw: Any, value: str):
    """StrValue 实例的组建"""
    v = StrValue.from_raw(raw)
    assert v.value == value
