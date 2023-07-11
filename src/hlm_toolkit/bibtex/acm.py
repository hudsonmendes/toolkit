import re
from typing import List

from .references import (
    AbstractReference,
    ProceedingReference,
    ArticleReference,
    WebsiteReference,
    SoftwareReference,
)


class ACMReferenceParser:
    def __init__(self, filename: str):
        self.filename = filename

    def parse(self) -> List[AbstractReference]:
        references: List[AbstractReference] = []
        with open(self.filename, "r") as file:
            for line in file:
                references.append(self._parse_line(line))
        return references

    def _parse_line(self, line: str):
        # Pseudo-code for parsing, replace this with actual parsing logic
        # based on the specific format of the ACM bibliographic reference
        # Here we determine the type of the reference based on its content
        parts = re.split(r"\s+", line.strip())
        if "Proceedings" in line:
            return ProceedingReference(*parts)
        elif "www." in line:
            return WebsiteReference(*parts)
        elif "v." in line:
            return SoftwareReference(*parts)
        else:
            return ArticleReference(*parts)
