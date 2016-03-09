"""Installs CLTK corpora in remote machine.
TODO: Printing current status.
TODO: Add the remaining corpora.
"""

__author__ = ['Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>']
__license__ = 'MIT License. See LICENSE'

from cltk.corpus.utils.importer import CorpusImporter

_latin = ['latin_text_perseus', 'latin_proper_names_cltk',\
          'latin_treebank_perseus', 'latin_text_lacus_curtius',\
          'latin_text_latin_library', 'latin_models_cltk',\
          'latin_pos_lemmata_cltk']
_greek = ['greek_text_perseus', 'greek_proper_names_cltk',\
         'greek_treebank_perseus', 'greek_models_cltk']
_coptic = ['coptic_text_scriptorium']
_tibetan = ['tibetan_pos_tdc', 'tibetan_lexica_tdc']


def main():
    print(" Downloading greek")
    corpus_importer = CorpusImporter('greek')
    for _corpus in _greek:
        print("    Downloading %s " % (_corpus))
        corpus_importer.import_corpus(_corpus)
    print(" Downloading latin")
    corpus_importer = CorpusImporter('latin')
    for _corpus in _latin:
        print("    Downloading %s " % (_corpus))
        corpus_importer.import_corpus(_corpus)
    print(" Downloading coptic")
    corpus_importer = CorpusImporter('coptic')
    for _corpus in _coptic:
        print("    Downloading %s " % (_corpus))
        corpus_importer.import_corpus(_corpus)
    print("Downloading tibetan")
    corpus_importer = CorpusImporter('tibetan')
    for _corpus in _tibetian:
        print("    Downloading %s " % (_corpus))
        corpus_importer.import_corpus(_corpus)


if __name__ == '__main__':
    main()
