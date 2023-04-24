class Tire:
    def __repr__(self):
        return 'ゴムのタイヤ'


class Frame:
    def __repr__(self):
        return 'アルミのフレーム'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'フレーム: {self.frame}')
        print(f'前のタイヤ: {self.front_tire}。後ろのタイヤ: {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())
    bike.print_specs()
