from abc import ABC
from dataclasses import dataclass


class AbstractReference(ABC):
    pass


@dataclass(frozen=True)
class ProceedingReference(AbstractReference):
    author: str
    title: str
    convention: str
    year: str
    pages: str
    publisher: str


@dataclass(frozen=True)
class ArticleReference(AbstractReference):
    author: str
    title: str
    journal: str
    year: str
    volume: str
    number: str
    pages: str
    issn: str
    publisher: str


# Website Reference
@dataclass(frozen=True)
class WebsiteReference(AbstractReference):
    author: str
    title: str
    url: str
    year: str
    access_date: str


# Software Reference
@dataclass(frozen=True)
class SoftwareReference(AbstractReference):
    author: str
    title: str
    version: str
    year: str
    publisher: str
