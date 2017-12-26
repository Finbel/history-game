import unittest
from game_functions import guess


class TestGuessMethod(unittest.TestCase):

    def test_correct_before(self):
        guessed_year = 1500
        correct_year = 1500
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), True)

    def test_wrong_before1(self):
        guessed_year = 1650
        correct_year = 1500
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_wrong_before2(self):
        guessed_year = 1500
        correct_year = 1650
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_correct_middle(self):
        guessed_year = 1650
        correct_year = 1650
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), True)

    def test_wrong_middle1(self):
        guessed_year = 1650
        correct_year = 1750
        years = [1600, 1700, 1800]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_order_wrong(self):
        guessed_year = 1650
        correct_year = 1750
        years = [1800, 1700, 1600]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_order_correct(self):
        guessed_year = 1650
        correct_year = 1650
        years = [1800, 1700, 1600]
        self.assertEqual(guess(guessed_year, correct_year, years), True)

    def test_wrong_middle2(self):
        guessed_year = 1750
        correct_year = 1650
        years = [1600, 1700, 1800]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_correct_after(self):
        guessed_year = 1800
        correct_year = 1800
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), True)

    def test_wrong_after1(self):
        guessed_year = 1650
        correct_year = 1800
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), False)

    def test_wrong_after2(self):
        guessed_year = 1800
        correct_year = 1650
        years = [1600, 1700]
        self.assertEqual(guess(guessed_year, correct_year, years), False)


if __name__ == '__main__':
    unittest.main()
