import numpy as np
from psycopg2 import sql
import math
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

# Setting total scores fields to 0

cur.execute(sql.SQL("update storm_student set {}=0;").format(sql.Identifier("total_score")))
cur.execute(sql.SQL("update storm_student set {}=0.0;").format(sql.Identifier("total_number")))
cur.execute(sql.SQL("update storm_student set {}=0.0;").format(sql.Identifier("total_average")))
cur.execute("commit;")

# Adding total scores data

for score in scores:

    cur.execute("update storm_student set total_score = %s where baseuser_ptr_id = %s;",[score[1],score[0]])  
    cur.execute("update storm_student set total_number = %s where baseuser_ptr_id = %s;",[score[2],score[0]])  
    cur.execute("update storm_student set total_average = %s where baseuser_ptr_id = %s;",[score[3],score[0]])  

cur.execute("commit;")
