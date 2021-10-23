#from myconfig import db_url
from app import db
from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, intro, text):
        self.title = title
        self.intro = intro
        self.text = text

    def __repr__(self):
        return '<Article %r>' % self.id

    def add_article(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_article(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update_article(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
