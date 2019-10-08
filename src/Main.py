import nltk
from nltk.corpus import stopwords

RECIPE = """Place the cayenne, black pepper, paprika, ginger, turmeric and cinnamon into a small bowl and mix to
         combine. Place the lamb in a large bowl and toss together with half of the spice mix. Cover and leave
         overnight in the fridge"""


def process(recipe) -> []:
    noiseWords = set(stopwords.words('english'))
    tokenizedRecipe = nltk.word_tokenize(recipe)
    result = [word for word in tokenizedRecipe if word not in noiseWords]
    return result[:3]


if __name__ == '__main__':
    process(RECIPE)
