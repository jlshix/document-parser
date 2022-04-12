# coding: utf-8

"""文书基类
"""

from pydantic import BaseModel

from .types import StrSet


class DocumentBase(BaseModel):
    """文书基类"""

    #: 文书编号
    id: str

    #: 文书标题
    title: str

    #: 解析类型
    types: StrSet
