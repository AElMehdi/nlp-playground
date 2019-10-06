import unittest

from src import Main


class MyTestCase(unittest.TestCase):
    def test_tokenizer(self):
        result = Main.process(Main.RECIPE)
        self.assertEqual(result, ["Place", "the", "cayenne"])



if __name__ == '__main__':
    unittest.main()
