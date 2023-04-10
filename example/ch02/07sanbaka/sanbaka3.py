# 関数にまとめる
def introdule_stooges(names):  # ばか大将を紹介
    message = '三ばか大将：'

    for index, name in enumerate(names):
        if index > 0:
            message += 'に'
        if index == len(names) - 1:
            message += '、それから'
        message += name
    print(message)


introdule_stooges(['モー', 'ラリー', 'シェンプ'])
introdule_stooges(['ラリー', 'カーリー', 'モー'])
