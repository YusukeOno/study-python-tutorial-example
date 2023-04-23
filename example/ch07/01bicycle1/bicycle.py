class Tire:
    def __repr__(self):
        return 'ゴムのタイヤ'


class Frame:
    def __repr__(self):
        return 'アルミのフレーム'


class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def print_specs(self):
        print(f'フレーム: {self.frame}')
        print(f'前のタイヤ： {self.front_tire}。後ろのタイヤ： {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle()
    bike.print_specs()
