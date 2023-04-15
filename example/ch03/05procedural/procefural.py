NAMES = ['小山', '大山', '中山']


def print_greetings():
    greeting_pattern = '{name}さんに、ご挨拶。'
    nice_person_pattern = '{name}さんはとても良い人です！'
    for name in NAMES:
        print(greeting_pattern.format(name=name))
        print(nice_person_pattern.format(name=name))


print_greetings()
