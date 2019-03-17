import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import will
import timefn

people = 100
matrix = np.zeros((people,10))

conn =  login.conn
cur = conn.cursor()

# Getting stints

cur.execute("select type_group,id from storm_stint limit 10 offset 10")
stint_list = cur.fetchall()
#stint_list = (type_group, stint_id)

# Will look like [(stint_type_index, stint_id)]

# Getting students

cur.execute(sql.SQL("SELECT * FROM storm_student LIMIT %s offset 100;").format(),[people])
a = cur.fetchall()



b = []

for i in a:
    ii = [i[0]] + list(i[5:])
    b.append(ii)

# Getting a 'universal' student score - simple for now

for i in range(len(stint_list)):
    for j in range(len(b)):
        if isinstance(stint_list[i][0],str):
            average = b[j][int(stint_list[i][0])*3+3]
        else:
            average = 0
            # here we don't put 0 but rather average scores

            print(b[j])

        if timefn.isAvailable(stint_list[i][1],b[j][0]):
            matrix[j][i] =  average
        else:
            matrix[j][i] =  np.nan



#np.savetxt("matrix.txt" ,matrix,delimiter=",")
list_of_pairs = will.iter_loop(matrix) #get pairs from will.py
matches = []
for i in list_of_pairs:
    matches.append([stint_list[i[1]][1],b[i[0]][0]])

for i in matches:
    cur.execute(sql.SQL("select ref from storm_stint where id = %s;").format(),[i[0]])
    cur.execute(sql.SQL("select ref from storm_baseuser where id = %s;").format(),[i[1]])

print(matches)













