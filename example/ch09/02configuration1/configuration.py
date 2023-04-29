import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


def random_food(request):
    return random.choice(FOODS)
