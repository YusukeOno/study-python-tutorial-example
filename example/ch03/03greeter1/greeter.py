from datetime import datetime
import locale  # 日時などの日本語化のため
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')  # 日本語に設定


class Greeter:
    def __init__(self, name):
        self.name = name

    def _day(self):
        return datetime.now().strftime('%A')

    def _part_of_day(self):
        current_hour = datetime.now().hour

        if current_hour < 12:
            part_of_day = '午前'
        elif 12 <= current_hour < 17:
            part_of_day = '午後'
        else:
            part_of_day = '夜'

        return part_of_day

    def greet(self, store):
        print(f'{store}へようこそ！私、{self.name}と申します。')
        print(f'{self._day()}の{self._part_of_day()}、いかがお過ごしですか？')
        print('本日のお客様に20% OFFのクーポンを差し上げます！')


greet = Greeter('Joe')
greet.greet('Apple Shop')
