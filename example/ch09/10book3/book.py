class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']

    @property
    def displaay_title(self):

        if self.title and self.subtitle:
            return f'{self.title}: {self.subtitle}'
        elif self.title:
            return self.title
        else:
            return 'Untitled'
