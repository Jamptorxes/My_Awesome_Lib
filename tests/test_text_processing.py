import unittest
from my_awesome_lib.text_processing import *


class TestTextProcessing(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("abc"), "cba")
        self.assertEqual(reverse("123"), "321")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse(""), "")

    def test_palindrome(self):
        self.assertTrue(palindrome("kajak"))
        self.assertTrue(palindrome("Kajak"))
        self.assertTrue(palindrome("A to idiota"))
        self.assertFalse(palindrome("abc"))
        self.assertFalse(palindrome("abc "))
        self.assertFalse(palindrome("nieee eee"))

    def test_count_words(self):
        self.assertEqual(count_words("Ala ma kota"), 3)
        self.assertEqual(count_words("Ala"), 1)

    def test_count_chars(self):
        self.assertEqual(count_chars("Ala ma kota"), 11)
        self.assertEqual(count_chars("Ala"), 3)


if __name__ == "__main__":
    unittest.main()
