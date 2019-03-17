# Implements matching algorithm 

import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import will
import timefn

people = 6000
matrix = np.zeros((people,10))

conn =  login.conn
cur = conn.cursor()

# Getting stints

cur.execute("select type_group,id from storm_stint limit 10 offset 300 where business_id = ")
stint_list = cur.fetchall()

################################################################################################
# Getting high-level businesses #
################################################################################################

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

            if average == 0.0:

                overallaverage = b[j][-3]

                if overallaverage == 0.0:
                    average = 0.6

        else:
            average = 0
        


        # Have implemented checking for availability below 
        # but database deletes availability instances in past
        # so will need current data to run.

        #matrix[j][i] = average

        if timefn.isAvailable(stint_list[i][1],b[j][0]):
            matrix[j][i] =  average
        else:
            matrix[j][i] =  np.nan

print(matrix)

np.savetxt("matrix.txt" ,matrix,delimiter=",")
list_of_pairs = will.iter_loop(matrix) #get pairs from will.py
matches = []
for i in list_of_pairs:
    matches.append([stint_list[i[1]][1],b[i[0]][0]])

print(matches)

refmatches = []

for i in matches:
    cur.execute(sql.SQL("select ref from storm_stint where id = %s;").format(),[i[0]])
    ref1 = cur.fetchall()[0][0]
    cur.execute(sql.SQL("select ref from storm_baseuser where id = %s;").format(),[i[1]])
    ref2 = cur.fetchall()[0][0]

    refmatches.append([ref1,ref2])

print(refmatches)
print(len(refmatches))




