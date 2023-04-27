from abc import ABC, abstractmethod


class Predator(ABC):  # ABCから継承することでこのクラスを抽象基底クラスとする
    @abstractmethod  # 全てのサブクラスでこのメソッドが定義されなければならないことを示す
    def eat(self, prey):  # サブクラスにおいて、IDE（統合開発環境）でこのメソッドのシグニチャがチェック可能になる
        pass  # 抽象メソッドではデフォルトの実装を持たない


class Bear(Predator):  # 抽象基底クラスのサブクラスとすることで、インターフェイスを実装する
    def eat(self, prey):  # このメソッドは必ず定義する必要がある。定義しないと例外が発生する
        print(f'熊が{prey}を一撃！')


class Owl(Predator):
    def eat(self, prey):
        print(f'フクロウが{prey}めがけて急降下！')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'カメレオンが舌を伸ばして{prey}をペロリ！')


if __name__ == '__main__':
    bear = Bear()
    bear.eat('シカ')
    owl = Owl()
    owl.eat('ネズミ')
    chameleon = Chameleon()
    chameleon.eat('ハエ')
