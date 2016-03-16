"""Installs CLTK corpora in remote machine.
TODO: Display the current status in more detail.
"""

__author__ = ['Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>']
__license__ = 'MIT License. See LICENSE'

from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.latin.corpora import LATIN_CORPORA
from cltk.corpus.chinese.corpora import CHINESE_CORPORA
from cltk.corpus.coptic.corpora import COPTIC_CORPORA
from cltk.corpus.greek.corpora import GREEK_CORPORA
from cltk.corpus.multilingual.corpora import MULTILINGUAL_CORPORA
from cltk.corpus.pali.corpora import PALI_CORPORA
#from cltk.corpus.sanskrit.corpora import SANSKRIT_CORPORA
from cltk.corpus.tibetan.corpora import TIBETAN_CORPORA

def _install(lang, lst):
    print("Downloading %s " % (lang))
    corpus_importer = CorpusImporter(lang)
    for _corpus in lst:
        if _corpus['location'] == 'remote':
            print("    Downloading %s " % (_corpus['name']))
            corpus_importer.import_corpus(_corpus['name'])
            break

def main():
    _install('latin', LATIN_CORPORA)
    _install('chinese', CHINESE_CORPORA)
    _install('coptic', COPTIC_CORPORA)
    _install('greek', GREEK_CORPORA)
    _install('multilingual', MULTILINGUAL_CORPORA)
    _install('pali', PALI_CORPORA)
#    _install('sanskrit', SANSKRIT_CORPORA)
    _install('tibetan', TIBETAN_CORPORA)

if __name__ == '__main__':
    main()
