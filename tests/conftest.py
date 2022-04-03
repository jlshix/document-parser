# coding: utf-8

"""测试配置与固件
"""

from pathlib import Path

import pytest


def pytest_collection_modifyitems(items):
    """pytest 的 hook, 将 nodeid 和 name 转为可读中文, 每次执行结束后自动调用"""

    def no_unicode(s: str) -> str:
        return s.encode("utf-8").decode("unicode_escape")

    for item in items:
        item._nodeid = no_unicode(item.nodeid)  # pylint: disable=protected-access
        item.name = no_unicode(item.name)


@pytest.fixture(scope="package", name="tests_path")
def absolute_tests_path() -> Path:
    """tests 目录路径"""
    return Path(__file__).parent.absolute()
