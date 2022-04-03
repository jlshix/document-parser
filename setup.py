# coding: utf-8

"""打包
"""

from pathlib import Path

import setuptools

from emr_document_parser import __version__

with open("README.md", encoding="utf8") as f:
    long_description = f.read()


def find_requirements(path: Path):
    """查找所有依赖"""
    with path.open() as g:
        s = g.read()
        return s.split("\n")


setuptools.setup(
    name="emr-document-parser",
    version=__version__,
    url="https://github.com/jlshix/emr-document-parser",
    download_url="https://github.com/jlshix/emr-document-parser/releases",
    author="jlshix",
    author_email="jlshix@163.com",
    description="电子病历文书数据解析与标准化",
    long_description=long_description,
    packages=["emr_document_parser"],
    python_requires='>=3.9',
    install_requires=find_requirements(path=Path("requirements/requirements.txt")),
)
