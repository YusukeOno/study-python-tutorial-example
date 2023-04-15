class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'一匹の{name}が「こんにちは！」と言った。')


class RollOverMixin:
    def roll_over(self):
        print('横回転をした！')


class Dog(SpeakMixin, RollOverMixin):
    pass  # 何もしない


dog = Dog()
dog.speak()
dog.roll_over()
