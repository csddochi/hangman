__author__ = 'user'

import unittest
import hangman

class hangmanTestCase(unittest.TestCase):

    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("apple", "apple")
        self.assertEqual(answer, True)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("google", "banana")
        self.assertEqual(answer, True)

if __name__ == "__main__":
    unittest.main()