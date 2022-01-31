from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Creates a 'user table'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)

# Creates a 'tweet table'


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)
