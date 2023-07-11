from typing import List

from .references import (
    AbstractReference,
    ProceedingReference,
    ArticleReference,
    WebsiteReference,
    SoftwareReference,
)


class BibtexWriter:
    def __init__(self, references: List[AbstractReference], filename: str):
        self.references = references
        self.filename = filename

    def write(self):
        with open(self.filename, "w") as file:
            for ref in self.references:
                file.write(self._convert_to_bibtex(ref))

    def _convert_to_bibtex(self, ref: AbstractReference) -> str:
        # Here we use different conversion logic based on the type of the reference
        if isinstance(ref, ArticleReference):
            return self._convert_article(ref)
        elif isinstance(ref, WebsiteReference):
            return self._convert_website(ref)
        elif isinstance(ref, SoftwareReference):
            return self._convert_software(ref)
        elif isinstance(ref, ProceedingReference):
            return self._convert_proceeding(ref)

    def _convert_article(self, ref: ArticleReference) -> str:
        # Continue with the earlier format for articles
        bibtex = (
            "@article{{,\n"
            "\tauthor = {{{}}},\n"
            "\ttitle = {{{}}},\n"
            "\tjournal = {{{}}},\n"
            "\tyear = {{{}}},\n"
            "\tvolume = {{{}}},\n"
            "\tnumber = {{{}}},\n"
            "\tpages = {{{}}},\n"
            "\tissn = {{{}}},\n"
            "\tpublisher = {{{}}},\n"
            "}}\n\n".format(
                ref.author,
                ref.title,
                ref.journal,
                ref.year,
                ref.volume,
                ref.number,
                ref.pages,
                ref.issn,
                ref.publisher,
            )
        )
        return bibtex

    def _convert_website(self, ref: WebsiteReference) -> str:
        # Define your format for websites
        # This is a basic example
        bibtex = (
            "@misc{{,\n"
            "\tauthor = {{{}}},\n"
            "\ttitle = {{{}}},\n"
            "\tyear = {{{}}},\n"
            "\turl = {{{}}},\n"
            "\tnote = {{Accessed: {}}}\n"
            "}}\n\n".format(ref.author, ref.title, ref.year, ref.url, ref.access_date)
        )
        return bibtex

    def _convert_software(self, ref: SoftwareReference) -> str:
        # Define your format for software
        # This is a basic example
        bibtex = (
            "@misc{{,\n"
            "\tauthor = {{{}}},\n"
            "\ttitle = {{{}}},\n"
            "\tyear = {{{}}},\n"
            "\tversion = {{{}}},\n"
            "\tpublisher = {{{}}},\n"
            "}}\n\n".format(ref.author, ref.title, ref.year, ref.version, ref.publisher)
        )
        return bibtex

    def _convert_proceeding(self, ref: ProceedingReference) -> str:
        # Define your format for proceeding references
        # This is a basic example
        bibtex = (
            "@inproceedings{{,\n"
            "\tauthor = {{{}}},\n"
            "\ttitle = {{{}}},\n"
            "\tbooktitle = {{{}}},\n"
            "\tyear = {{{}}},\n"
            "\tpages = {{{}}},\n"
            "\tpublisher = {{{}}},\n"
            "}}\n\n".format(
                ref.author,
                ref.title,
                ref.convention,
                ref.year,
                ref.pages,
                ref.publisher,
            )
        )
        return bibtex
