import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


def to_json(food):
    return json.dumps({'food': food})


def to_xml(food):
    return f'<response><food>{food}</food></response>'


def random_food(request):
    food = random.choice(FOODS)

    formats = {
        'application/json': to_json,
        'application/xml': to_xml,
    }

    format_function = formats.get(
        request.headers.get('Accept'),
        lambda val: val
    )

    return format_function(food)
