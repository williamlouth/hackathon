import pandas as pd
import psycopg2 as py
import login

conn = login.conn
cur = conn.cursor()
cur.execute("SELECT student_id, grade FROM storm_review;")
a = cur.fetchall()

d = {}

for k, v in a:
	d.setdefault(k, [k]).append(v)
b = map(tuple, d.values())

rvw_tuple = []

for j in b:
	rvw_tuple.append(j)

reviews = []

for i in rvw_tuple:

	reviews.append(list(i))

print(reviews)



