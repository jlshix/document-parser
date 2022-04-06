# coding: utf-8

"""数据模型基类, 基于 BaseModel 做一些定制
"""

from typing import Iterable

from pydantic import BaseModel, root_validator

from .content import Content, Contents
from .values import parse_raw


class BasicModel(BaseModel):
    """数据模型基类"""

    class Config:
        """配置类"""
        default_type_name = "str"

    @root_validator(pre=True)
    def del_none(cls, values: dict):    # pylint: disable=no-self-argument,no-self-use
        """去除输入数据中的 None"""
        return {k: v for k, v in values.items() if v is not None}

    def iter_content(self) -> Iterable[Content]:
        """根据 Field 的 extra info 对键值进行标准化, 迭代为 Content 对象"""
        for name, field in self.__fields__.items():
            extra = field.field_info.extra
            key = extra.get("key")
            type_name = extra.get("type_name") or self.Config.default_type_name
            if not key:
                continue
            raw = getattr(self, name)
            if raw is None:
                continue
            value = parse_raw(type_name=type_name, key=key, raw=raw)
            yield Content(key=key, value=value, raw=raw)

    def to_contents(self) -> Contents:
        """转为 contents"""
        rv = list(self.iter_content())
        return rv


class BasicListModel(BasicModel):
    """列表数据模型基类"""

    __root__: list[BasicModel]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]

    def __len__(self):
        return len(self.__root__)

    def to_contents(self) -> Contents:
        """转为 contents"""
        rv = []
        for item in self:
            tmp = item.to_contents()
            rv.extend(tmp)
        return rv
