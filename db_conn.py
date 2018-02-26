#PostgreSQL database adapter
import psycopg2
import os
#Importing Models to fetch the data
from app import Authors
from app import Books

#Prompting User for the input
aut = input("Enter the author name: ")
author = Authors.query.filter(Authors.name == aut)

#extracting all the books written by the author
for i in author:
    bid = (i.oid)
    books = Books.query.filter(Books.id == bid)
    for j in books:
        print(j.name)

#following code is to Keep track of book id and author id since we have not used auto increment
conn = psycopg2.connect('postgresql://testdb:123@localhost/testdb')
c = conn.cursor()
#c.execute("select books.name from authors,books where books.id = authors.oid and  authors.name = 'William';")
c.execute("select books.id from Books order by Books.id DESC Limit 1")
rows = c.fetchall()
#print(rows[0])

for row in rows:
    print("\n" * 40)
    print(row[0])


c.execute("select authors.id from authors order by authors.id DESC Limit 1")
arows = c.fetchall()

for arow in arows:
    print("\n" * 40)
    print(arow[0])


