# 第2版 defaultdictの利用
from collections import defaultdict  # モジュールcollectionsからdefaultdictをインポート


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = defaultdict(int)  # countsは整数の辞書なので、defaultdictの各要素はintとする
    for number in numbers:
        counts[number] += 1  # intのデフォルト値は0なので、最初にその数値が出現したときは「0+1」が計算され、1になる
    return get_number_with_highest_count(counts)
