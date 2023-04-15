# 第4版 ラムダ関数の利用
from collections import Counter


def get_number_with_highest_count(counts):  # countsの要素のうち、頻度最高のものを得る
    return max(
        counts,
        key=lambda number: counts[number]
        # 第2引数keyの値として「numberを引数として受け取りcounts[number]を返す関数」を指定
    )


def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)
