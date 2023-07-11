from .converters import ACMToBibtexConverter


class BibtexCLI:
    def acm_to_bibtext(self, filepath: str, outpath: str) -> None:
        ACMToBibtexConverter(filepath).convert(outpath)
