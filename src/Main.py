import nltk

RECIPE = """Place the cayenne, black pepper, paprika, ginger, turmeric and cinnamon into a small bowl and mix to
         combine. Place the lamb in a large bowl and toss together with half of the spice mix. Cover and leave
         overnight in the fridge"""


def process(recipe) -> []:
    return nltk.word_tokenize(recipe)[:3]


if __name__ == '__main__':
    process(RECIPE)
