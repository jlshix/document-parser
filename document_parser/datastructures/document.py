# coding: utf-8

"""文书类型
"""

from typing import Type

from pydantic import BaseModel

from .basic_model import BasicModel
from .content import Contents
from .document_base import DocumentBase
from .types import StrSet


class Document(DocumentBase):
    """文书类型"""

    #: 解析后的文书内容
    contents: Contents = []

    @classmethod
    def parse_basic_model(
            cls,
            model: BasicModel,
            id_: str = None,
            title: str = None,
            types: StrSet = None,
    ):
        """从 BasicModel 子类型实例创建"""
        name = model.__class__.__name__
        contents = model.to_contents()
        rv = cls(
            id=id_ or name,
            title=title or name,
            types=types or {name, },
            contents=contents,
        )
        return rv

    @classmethod
    def parse_data_by_model_type(
            cls,
            data: dict,
            model_type: Type[BasicModel],
            id_: str = None,
            title: str = None,
            types: StrSet = None,
    ):
        """根据数据模型类和数据直接创建实例"""
        model = model_type.parse_obj(data)
        rv = cls.parse_basic_model(model=model, id_=id_, title=title, types=types)
        return rv


class Documents(BaseModel):
    """输入文书列表"""
    __root__: list[Document]
