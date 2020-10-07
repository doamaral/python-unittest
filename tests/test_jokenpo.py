from unittest import TestCase
from jokenpo import *


class TestIaTest(TestCase):
    def test_number_is_less_than_five(self):
        test_num = 4
        self.assertEqual(str(test_num) + " is less than 5.", check_five(self, test_num))

    def test_number_is_equal_to_five(self):
        test_num = 5
        self.assertEqual(str(test_num) + " is equal to 5.", check_five(self, test_num))

    def test_number_is_greater_than_five(self):
        test_num = 6
        self.assertEqual(str(test_num) + " is greater than 5.", check_five(self, test_num))

    def test_rock_tie(self):
        self.assertEqual("TIE!", who_won(self, "rock", "rock"))

    def test_scissors_tie(self):
        self.assertEqual("TIE!", who_won(self, "scissors", "scissors"))

    def test_paper_tie(self):
        self.assertEqual("TIE!", who_won(self, "paper", "paper"))

    def test_rock_wins_against_scissors(self):
        self.assertEqual("Player 1 wins!", who_won(self, "rock", "scissors"))

    def test_rock_looses_against_paper(self):
        self.assertEqual("Player 2 wins!", who_won(self, "rock", "paper"))

    def test_paper_wins_against_rock(self):
        self.assertEqual("Player 1 wins!", who_won(self, "paper", "rock"))

    def test_paper_looses_against_scissors(self):
        self.assertEqual("Player 2 wins!", who_won(self, "paper", "scissors"))

    def test_scissors_wins_against_paper(self):
        self.assertEqual("Player 1 wins!", who_won(self, "scissors", "paper"))

    def test_scissors_looses_against_rock(self):
        self.assertEqual("Player 2 wins!", who_won(self, "scissors", "rock"))
