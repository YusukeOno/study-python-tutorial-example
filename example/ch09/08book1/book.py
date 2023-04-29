class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']

        # 表示用タイトルの決定
        if self.title and self.subtitle:
            # サブタイトルが指定されているときは、メインのタイトルの後ろに付加する
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            # タイトルのみが指定されているときはそれを表示用タイトルにする
            self.display_title = self.title
        else:
            # どちらも指定さえれていない場合はUntited（無題）とする
            self.display_title = 'Unitled'
