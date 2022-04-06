# coding: utf-8

"""文书类型
"""

from pydantic import BaseModel

from .content import Contents
from .document_base import DocumentBase


class Document(DocumentBase):
    """文书类型"""

    #: 解析后的文书内容
    contents: Contents = []


class Documents(BaseModel):
    """输入文书列表"""
    __root__: list[Document]
