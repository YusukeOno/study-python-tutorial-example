class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author_data = data['author']  # 著者をデータからの辞書として記憶

    @property
    def author_for_display(self):  # 表示用の著者名を表示。「名前＋姓」の順に表示する
        return f'{self.author_data["first_name"]} {self.author_data["last_name"]}'

    @property
    def author_for_citation(self):  # 参考文献（citation）用の著者名。「姓, イニシャル」の順に表示する
        return f'{self.author_data["last_name"]}, {self.author_data["first_name"][0]}.'


book = Book({
    'title': 'Brillo-iant',
    'subtitle': 'The pad that changed everything',
    'author': {
        'first_name': 'Rusty',
        'last_name': 'Potts',
    }
})

print(book.author_for_display)  # Web表示用
print(book.author_for_citation)  # 論文参考文献用
