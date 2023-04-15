# 第3版 Counterの利用
from collections import Counter  # Counterもモジュールcollectionsに入っている


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = Counter(numbers)  # このコードは自作した辞書と同じように動作する
    return get_number_with_highest_count(counts)
