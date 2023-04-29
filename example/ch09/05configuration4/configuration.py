import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


def random_food(request):
    food = random.choice(FOODS)

    formats = {
        'application/json': json.dump({'food': food}),
        'application/xml': f'<response><food>{food}</food></response>'
    }

    return formats.get(request.headers.get('Accept'), food)
