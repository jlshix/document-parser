# coding: utf-8

"""wrong_value.py 的测试
"""

import pytest

from document_parser.datastructures.values.wrong_value import WrongValue


@pytest.mark.parametrize(
    argnames="message",
    argvalues=(
            "无法将原始值`None`转为数字",
            "原始值`20220403`不是合法的日期时间"
    )
)
def test_wrong_value(message: str):
    """错误值的测试"""
    v = WrongValue.from_raw(message=message)
    assert v.message == message
