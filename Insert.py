#following code is meant to insert values to the database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import Books, Authors
from sqlalchemy.orm import sessionmaker

#engine maintains reference to database connection pool and it can be used directly to issue SQL to the database
from sqlalchemy import create_engine
import psycopg2

app = Flask(__name__)
# app.config.from_pyfile('flask.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testdb:123@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#Creating connection object of PostgreSQL database adapter
conn = psycopg2.connect('postgresql://testdb:123@localhost/testdb')
engine = create_engine('postgresql://testdb:123@localhost/testdb', echo=True)
c = conn.cursor()
#c.execute("select books.name from books")
brows = Books.query.all()
c.execute("select books.id from Books order by Books.id DESC Limit 1")
rows = c.fetchall()
for row in rows:
    r=(row[0])  #Track of Book id

c.execute("select authors.id from authors order by authors.id DESC Limit 1")
arows = c.fetchall()

for arow in arows:
    ar=(arow[0]) #Track of Author id

#Prompting User to enter the details
aname = input("Enter the author name: ")
bname = input("Enter the Book name: ")
b_id=r+1  #book_id_recent
a_id=ar+1 #author_id_recent
for s in brows: #This will be executed if the book name is already there and the author is different so in that case no need to insert the book name again.
    if(s.name == bname):
        print(s.id)
        o_id = s.id
        AuthorModel = Authors(id=a_id, name=aname, oid=o_id)
        db.session.add(AuthorModel)
        db.session.commit()
        #print(s.name)
        #print(bname)
        break
else: #This code will be executed if both book as well as author is new and not present in the database
    #print('else')
    o_id = b_id
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    BookModel = Books(id=b_id, name=bname)
    db.session.add(BookModel)
    db.session.commit()
    AuthorModel = Authors(id=a_id, name=aname, oid=o_id)
    db.session.add(AuthorModel)
    db.session.commit()

# o_id=input("Enter the author oid: ")


#for s in brows:
 #  if s.name == bname:
        #o = Books.query.filter(s.name == bname)

  #      s.id)
    #print(s.name)
    #else:
     #   o_id = b_id
'''
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
BookModel = Books(id=b_id, name=bname)
db.session.add(BookModel)
db.session.commit();
AuthorModel = Authors(id=a_id, name=aname, oid=o_id)
db.session.add(AuthorModel)
db.session.commit();
'''