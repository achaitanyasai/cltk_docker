"""Test version, corpus
"""

__author__ = 'Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>'
__license__ = 'MIT License. See LICENSE.'

from cltk.corpus.latin.corpora import LATIN_CORPORA
from cltk.corpus.chinese.corpora import CHINESE_CORPORA
from cltk.corpus.coptic.corpora import COPTIC_CORPORA
from cltk.corpus.greek.corpora import GREEK_CORPORA
from cltk.corpus.multilingual.corpora import MULTILINGUAL_CORPORA
from cltk.corpus.pali.corpora import PALI_CORPORA
#from cltk.corpus.sanskrit.corpora import SANSKRIT_CORPORA
from cltk.corpus.tibetan.corpora import TIBETAN_CORPORA
import sys
import unittest
import os

def read_directories(language):
    path = os.path.expanduser('~/cltk_data/%s/' % (language))
    dirs = []
    for root, subFolders, files in os.walk(path):
        for _subFolders in subFolders:
            if _subFolders.startswith(language):
                dirs.append(_subFolders)
    return dirs

class TestSequenceFunctions(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test_version(self):
        """Tests python version"""
        self.assertEqual(sys.version_info.major, 3)
        self.assertEqual(sys.version_info.minor, 5)

    def test_installed_latin_corpora(self):
        """Tests if latin corpora is correctly installed or not"""
        dirs = read_directories('latin')
        for _corpus in LATIN_CORPORA:
            if _corpus['location'] == 'remote':
                self.assertTrue(_corpus['name'] in dirs)

    def test_installed_chinese_corpora(self):
        """Tests if chinese corpora is correctly installed or not"""
        dirs = read_directories('chinese')
        for _corpus in CHINESE_CORPORA:
            if _corpus['location'] == 'remote':
                self.assertTrue(_corpus['name'] in dirs)

    def test_installed_coptic_corpora(self):
        """Tests if chinese corpora is correctly installed or not"""
        dirs = read_directories('coptic')
        for _corpus in COPTIC_CORPORA:
            if _corpus['location'] == 'remote':
                self.assertTrue(_corpus['name'] in dirs)
    
    def test_installed_greek_corpora(self):
        """Tests if chinese corpora is correctly installed or not"""
        dirs = read_directories('greek')
        for _corpus in GREEK_CORPORA:
            if _corpus['location'] == 'remote':
                self.assertTrue(_corpus['name'] in dirs)

    def test_installed_multilingual_corpora(self):
        """Tests if multilingual corpora is correctly installed or not"""
        dirs = read_directories('multilingual')
        for _corpus in MULTILINGUAL_CORPORA:
            if _corpus['location'] == 'remote':
               self.assertTrue(_corpus['name'] in dirs)

    def test_installed_pali_corpora(self):
        """Tests if pali corpora is correctly installed or not"""
        dirs = read_directories('pali')
        for _corpus in PALI_CORPORA:
            if _corpus['location'] == 'remote':
               self.assertTrue(_corpus['name'] in dirs)

    """def test_installed_sanskrit_corpora(self):
        "Tests if sanskrit corpora is correctly installed or not"
        "Right now SANSKRIT corpora in not integrated with pip.\
         Uncomment once it's done."
        dirs = read_directories('sanskrit')
        for _corpus in SANSKRIT_CORPORA:
            if _corpus['location'] == 'remote':
               self.assertTrue(_corpus['name'] in dirs)"""

    def test_installed_tibetan_corpora(self):
        """Tests if tibetan corpora is correctly installed or not"""
        dirs = read_directories('tibetan')
        for _corpus in TIBETAN_CORPORA:
            if _corpus['location'] == 'remote':
               self.assertTrue(_corpus['name'] in dirs)

if __name__ == '__main__':
    unittest.main()
