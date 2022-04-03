# coding: utf-8

"""number_value.py 的测试
"""

from __future__ import annotations

from typing import Any

import pytest

from document_parser.datastructures.values.number_value import NumberValue


@pytest.mark.parametrize(
    argnames="raw,value",
    argvalues=(
        (42, 42.0),
        ("117", 117.0),
        ("inf", float("inf")),
    ),
)
def test_number_value(raw: Any, value: float):
    """NumberValue 实例的组建"""
    v = NumberValue.from_raw(raw)
    assert v.value == value
