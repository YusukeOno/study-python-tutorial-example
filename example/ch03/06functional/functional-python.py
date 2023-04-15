from functools import reduce

squares = map(lambda x: x*x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])

evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
