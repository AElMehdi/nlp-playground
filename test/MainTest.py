import unittest

from src import Main


class MyTestCase(unittest.TestCase):
    def test_tokenizer(self):
        result = Main.process(Main.RECIPE)
        self.assertEqual(result, ["place", "cayenne", "black"])

    def test_remove_stopwords_and_punctation(self):
        result = Main.process(Main.RECIPE)
        self.assertEqual(result, ["place", "cayenne", "black"])


if __name__ == '__main__':
    unittest.main()

    # "Place the cayenne, black pepper, paprika, ginger, turmeric and cinnamon into a small bowl and mix to " \
    # "combine. Place the lamb in a large bowl and toss together with half of the spice mix. Cover and leave " \
    # "overnight in the fridge"
