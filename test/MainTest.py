import unittest

from src import Main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = Main.process("blomm")
        self.assertEqual(result, "Gotchya!")


if __name__ == '__main__':
    unittest.main()
