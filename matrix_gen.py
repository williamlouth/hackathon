# Implements matching algorithm 

import numpy as np
import csv
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import will
import timefn

from backports import csv
import io

people = 6000
matrix = np.zeros((people,10))

conn =  login.conn
cur = conn.cursor()

# Getting stints



################################################################################################
# Getting high-level businesses for testing #

cur.execute("SELECT storm_business.id, stints.cnt FROM storm_business INNER JOIN (SELECT COUNT(*) AS cnt, business_id FROM storm_stint GROUP BY business_id) AS stints ON stints.business_id=storm_business.id ORDER BY cnt DESC LIMIT 30;")
bigbusiness = cur.fetchall()

#with open('txt/BusinessRank.csv','r') as f:
#    reader = csv.reader(f)
#    bus_ranks = list(reader)
#print(bus_ranks)

with io.open('txt/BusinessRank.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    bus_ranks = list(r)

businessids = []

for business in bigbusiness:
    businessids.append(business[0])

#print(businessids)

cur.execute("select type_group,id from storm_stint where business_id in %s limit 10",(tuple(businessids),))
stint_list = cur.fetchall()

#print(stint_list)

################################################################################################

#cur.execute("select type_group,id from storm_stint limit 10 offset 300")

#cur.execute("select type_group,id from storm_stint where business_id = 454 limit 10")
#stint_list = cur.fetchall()

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
            number = b[j][int(stint_list[i][0])*3+2]
            total = b[j][int(stint_list[i][0])*3+1]

            overallaverage = b[j][-1]
            overallnumber = b[j][-2]


            m_stint = stint_list[i][1]
            
            cur.execute(sql.SQL("SELECT business_id FROM storm_stint where id = %s;").format(),[m_stint])
            new_bus_ref = cur.fetchall()[0][0]
            cur.execute(sql.SQL("SELECT ref FROM storm_business where id = %s;").format(),[new_bus_ref])
            new_bus_ref = cur.fetchall()[0]
            new_bus_rank = 0
            for k in bus_ranks:
                if k[0] == new_bus_ref:
                    new_bus_rank = k[1]
                    

            if number < 3:

                if overallaverage == 0.0:
                    average = 0.6
                else:
                    average = overallaverage
            else:
                average += 0.03*math.log(number) #better to be more experienced
                average += overallaverage/7.5

            if new_bus_rank == 4:
                if overallnumber < 5:
                    average = 0.0
            

        else:
            average = 0
        
        # Have implemented checking for availability below 
        # but database deletes availability instances in past
        # so will need current data to run.

        matrix[j][i] = average

        #if timefn.isAvailable(stint_list[i][1],b[j][0]):
        #    matrix[j][i] =  average
        #else:
        #    #matrix[j][i] =  np.nan
        #    matrix[j][i] =  average
        #if timefn.isAvailable(stint_list[i][1],b[j][0]):
        #    matrix[j][i] =  average
        #else:
        #    matrix[j][i] =  np.nan

#print(matrix)
#print(matrix.shape)

np.savetxt("matrix.txt" ,matrix,delimiter=",")
list_of_pairs = will.iter_loop(matrix) #get pairs from will.py
matches = []
for i in list_of_pairs:
    matches.append([stint_list[i[1]][1],b[i[0]][0]])


#print(matches)

refmatches = []

for i in matches:
    cur.execute(sql.SQL("select ref from storm_stint where id = %s;").format(),[i[0]])
    ref1 = cur.fetchall()[0][0]
    cur.execute(sql.SQL("select ref from storm_baseuser where id = %s;").format(),[i[1]])
    ref2 = cur.fetchall()[0][0]

    refmatches.append([ref1,ref2])

print(refmatches)
print(len(refmatches))




