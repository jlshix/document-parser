# coding: utf-8

"""内置解析器类
"""

from collections import defaultdict

from bs4 import BeautifulSoup

from ..datastructures.document import Document
from ..datastructures.document_in import DocumentIn
from ..datastructures.types import Parsed


class BaseParser:
    """parser 基类"""

    doc_type: str = ""

    @staticmethod
    def parse(document_in: DocumentIn) -> Parsed:
        """子类自行实现的解析方法"""

    @staticmethod
    def contrast(parsed: Parsed, rv: Document):
        """子类自行实现的对照方法"""

    def parse_and_contrast(self, document_in: DocumentIn) -> Document:
        """调用入口, 给定输入文书, 给出解析结果"""
        rv = document_in.to_empty_document()

        parsed = self.parse(document_in)
        self.contrast(parsed, rv)

        return rv


class BaseSoupParser(BaseParser):
    """使用 bs4 的 Parser 基类"""

    @staticmethod
    def parse(soup: BeautifulSoup) -> Parsed:  # pylint: disable=arguments-renamed
        """子类自行实现的解析方法, 输入为 Soup"""

    def parse_and_contrast(self, document_in: DocumentIn) -> Document:
        """调用入口, 给定输入文书, 给出解析结果"""
        rv = document_in.to_empty_document()
        soup = BeautifulSoup(document_in.contents, "lxml")

        parsed = self.parse(soup)
        self.contrast(parsed, rv)

        return rv


class BaseSoupParserWithMixin(BaseSoupParser):
    """使用 bs4 的 Parser 基类, 支持混入类附加通用解析内容"""

    def init_result(self, soup: BeautifulSoup) -> Parsed:
        """初始化解析结果, 若 mro 中有 Mixin 且定义了 parse 方法, 则合并其调用结果"""
        rv = defaultdict(list)
        for cls in self.__class__.mro():
            name = cls.__name__
            if "Mixin" in name and hasattr(cls, "parse"):
                method = getattr(cls, "parse")
                parsed = method(soup) or {}
                for k, v in parsed.items():
                    rv[k].extend(v)
        return rv

    def parse_and_contrast(self, document_in: DocumentIn) -> Document:
        """调用入口, 给定输入文书, 给出解析结果"""
        rv = document_in.to_empty_document()
        soup = BeautifulSoup(document_in.contents, "lxml")

        origin = self.init_result(soup)
        parsed = self.parse(soup)
        parsed.update(origin)
        self.contrast(parsed, rv)

        return rv
