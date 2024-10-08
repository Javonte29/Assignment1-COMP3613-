from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'reviews': [review.get_json() for review in self.reviews]
        }