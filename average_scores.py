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

# Calculating total_score, total_number and total_mean scores

scores = []

for k in reviews:

	student = k[0]
	del k[0]

	total_score = sum(k)
	total_number = len(k)
	total_mean = total_score / total_number


	scores.append([student, total_score,total_number,total_mean])

print(scores)





