import unittest
from main import reverse_string

class TestReverseString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_numbers(self):
        self.assertEqual(reverse_string("123"), "321")
