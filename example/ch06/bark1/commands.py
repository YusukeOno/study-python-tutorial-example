from database import DatabaseManager


db = DatabaseManager('bookmarks.db')


class CreateBookmaksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoicrement',
            'タイトル': 'text not null',
            'url': 'text not null',
            'メモ': 'text',
            '追加日時': 'text not null',
        })

    def execute(self, data):
        data['date_added'] = datetime.utcnow(), isoformat()
        db.add('bookmarks', data)
        return 'ブックマークを追加しました。'


class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()
