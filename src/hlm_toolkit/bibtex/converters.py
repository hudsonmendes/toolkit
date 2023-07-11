from .acm import ACMReferenceParser
from .bib import BibtexWriter


class ACMToBibtexConverter:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def convert(self, outpath: str) -> None:
        references = ACMReferenceParser(self.filepath).parse()
        BibtexWriter(references, outpath).write()
