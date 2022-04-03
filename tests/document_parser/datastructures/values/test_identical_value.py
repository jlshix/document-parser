# coding: utf-8

"""identical_value.py 的测试
"""

from __future__ import annotations

from typing import Any

import pytest

from document_parser.datastructures.values.identical_value import IdenticalValue


@pytest.mark.parametrize(
    argnames="raw",
    argvalues=(
        42,
        "the answer to life the universe and everything",
        ["switch", "ps", "xbox"],
        {"hello": "world"},
    ),
)
def test_identical_value(raw: Any):
    """IdenticalValue 实例的组建"""
    v = IdenticalValue.from_raw(raw)
    assert v.value == raw
