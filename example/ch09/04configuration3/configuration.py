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

    if request.headers.get('Accept') == 'application/json':
        return json.dump({'food': food})
    elif request.headers.get('Accept') == 'application/xml':
        return f'<response><food>{food}</food></response>'
    else:
        return food
