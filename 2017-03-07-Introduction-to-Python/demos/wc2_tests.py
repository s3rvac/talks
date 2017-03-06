# A sample test for the wc2 module.

import io
import unittest

from wc2 import count_lines_and_words

class CountLinesAndWordsTests(unittest.TestCase):
    def test_returns_correct_lines_and_words_for_empty_file(self):
        file = io.StringIO('')

        lines, words = count_lines_and_words(file)

        self.assertEqual(lines, 0)
        self.assertEqual(words, 0)

    def test_returns_correct_lines_and_words_for_file_with_single_line(self):
        file = io.StringIO('a b c')

        lines, words = count_lines_and_words(file)

        self.assertEqual(lines, 1)
        self.assertEqual(words, 3)

    def test_returns_correct_lines_and_words_for_file_with_empty_line(self):
        file = io.StringIO('a\n\nb')

        lines, words = count_lines_and_words(file)

        self.assertEqual(lines, 3)
        self.assertEqual(words, 2)
