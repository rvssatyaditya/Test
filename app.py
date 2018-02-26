from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # imported SQLAlchemy for data storage and retrival

app = Flask(__name__)
# Initializing Database String
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testdb:123@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db contains flask object
db = SQLAlchemy(app)


# created Books Model to fetch Book related data
class Books(db.Model):
    # __tablename__ = 'books'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))

    # Constructor of Books Model
    def __init__(self, id, name) -> object:
        self.id = id
        self.name = name


# created Authors Model to fetch Author related data
class Authors(db.Model):
    # __tablename__ = 'author';
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    oid = db.Column(db.String)

    # Constructor of Author Model
    def __init__(self, id, name, oid):
        self.id = id
        self.name = name
        self.oid = oid


if __name__ == '__main__':
    app.run();
