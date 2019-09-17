#!/usr/bin/env python
"""Installs CLTK corpora in remote machine.
TODO: Display the current status in more detail.
"""

__author__ = ['Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>']
__license__ = 'MIT License. See LICENSE'

from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.utils.importer import LANGUAGE_CORPORA
import sys

def _install(lang, lst):
    print("Downloading %s " % (lang))
    corpus_importer = CorpusImporter(lang)
    for _corpus in lst:
        if _corpus['location'] == 'remote':
            print("    Downloading %s " % (_corpus['name']))
            corpus_importer.import_corpus(_corpus['name'])

def main():
    if (len(sys.argv) > 1):
        for lang in sys.argv[1:]:
            _install(lang, LANGUAGE_CORPORA[lang])
    else:
        for key, value in LANGUAGE_CORPORA.items():
            _install(key, value)

if __name__ == '__main__':
    main()
