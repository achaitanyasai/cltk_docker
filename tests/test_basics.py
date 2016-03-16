"""Test version, corpus
"""

__author__ = 'Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>'
__license__ = 'MIT License. See LICENSE.'

from cltk.corpus.latin.corpora import LATIN_CORPORA
import sys
import unittest
import os

class TestSequenceFunctions(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test_version(self):
        """Tests python version"""
        self.assertEqual(sys.version_info.major, 3)
        self.assertEqual(sys.version_info.minor, 5)

    def test_installed_latin_corpora(self):
        """Tests if latin corpora is correctly installed or not"""
        path = os.path.expanduser('~/cltk_data/latin/')
        dirs = []
        for root, subFolders, files in os.walk(path):
            for _subFolders in subFolders:
                dirs.append(_subFolders)
        for _corpus in LATIN_CORPORA:
            if _corpus['location'] == 'remote':
                self.assertTrue(_corpus['name'] in dirs)


if __name__ == '__main__':
    unittest.main()
