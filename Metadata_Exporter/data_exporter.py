# pip install psycopg2-binary

import psycopg2
import os

try:
    connection = psycopg2.connect("dbname='scratchpad' user='scale' host='10.3.2.220' password='scale'")
except:
    print "unable to connect to db"

cur = connection.cursor()

# namedict = ({"first_name":"Joshua", "last_name":"Drake"},
#             {"first_name":"Steven", "last_name":"Foo"},
#             {"first_name":"David", "last_name":"Bar"})

# cur = connection.cursor()
# cur.executemany("""INSERT INTO table(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)

try:
    cur.execute("""INSERT INTO "BASIC_INFO" (id,payload,created_date) VALUES(3,'i love potatoes', '2020-02-27 13:11:14.162894-05')""")
except: 
    print "cant do it yo"

connection.commit()

