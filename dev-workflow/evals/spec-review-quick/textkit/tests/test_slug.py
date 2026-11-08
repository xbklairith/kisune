import unittest

from textkit import slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_punctuation(self):
        self.assertEqual(slugify("Hi, there!"), "hi-there")


if __name__ == "__main__":
    unittest.main()
