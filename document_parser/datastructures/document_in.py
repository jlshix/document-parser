# coding: utf-8

"""输入文书类型
"""

from typing import Any

from pydantic import BaseModel

from .document import Document
from .document_base import DocumentBase


class DocumentIn(DocumentBase):
    """输入文书"""

    #: 文书内容, 结构不限
    contents: Any

    def to_empty_document(self) -> Document:
        """转为 contents 为空的 Document 对象"""
        rv = Document(**self.dict(exclude={"contents", }))
        return rv


class DocumentsIn(BaseModel):
    """输入文书列表"""
    __root__: list[DocumentIn]
