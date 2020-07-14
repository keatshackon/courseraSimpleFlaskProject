from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    date  = db.Column(db.String, nullable = False)

    def __str__(self):
        return f"{self.title} Created on {self.date}"
