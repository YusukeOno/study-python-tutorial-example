# 入れ子になったforループ
def has_duplicates(sequence):
    for index1, item1 in enumerate(sequence):
        for index2, item2 in enumerate(sequence):
            if item1 == item2 and index1 != index2:
                return True
    return False
