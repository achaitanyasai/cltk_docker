"""Installs CLTK corpora in remote machine.
TODO: Printing current status.
TODO: Add the remaining corpora.
"""

__author__ = ['Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>']
__license__ = 'MIT License. See LICENSE'

from cltk.corpus.utils.importer import CorpusImporter


corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_text_perseus')
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_text_perseus')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_proper_names_cltk')
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_proper_names_cltk')
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_treebank_perseus')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_treebank_perseus')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_text_lacus_curtius')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_text_latin_library')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_pos_lemmata_cltk')
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_models_cltk')
corpus_importer = CorpusImporter('coptic')
corpus_importer.import_corpus('coptic_text_scriptorium')
corpus_importer = CorpusImporter('tibetan')
corpus_importer.import_corpus('tibetan_pos_tdc')
corpus_importer = CorpusImporter('tibetan')
corpus_importer.import_corpus('tibetan_lexica_tdc')
