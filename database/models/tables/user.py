from database.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(80))

    @classmethod
    def create(cls, **kwargs):
        user = cls(**kwargs)
        return user.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
