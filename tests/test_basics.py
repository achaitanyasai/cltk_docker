"""Test version, corpus
"""

__author__ = 'Chaitanya Sai Alaparthi <achaitanyasai@gmail.com>'
__license__ = 'MIT License. See LICENSE.'

import sys
import unittest


class TestSequenceFunctions(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test_version(self):
        """Tests python version"""
        self.assertEqual(sys.version_info.major, 3)
        self.assertEqual(sys.version_info.minor, 5)

if __name__ == '__main__':
    unittest.main()
