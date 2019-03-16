import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import datetime


conn = login.conn
cur = conn.cursor()

##print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_studentavailability';"))
#print(cur.fetchall())

#cur.execute("select * from storm_studentavailability LIMIT 1;")
#print(cur.fetchall())

def toSeconds(t):
    return (t-datetime.datetime(1970,1,1)).total_seconds() 

def isAvailable(stintid,studentid):

    cur.execute(sql.SQL("select * from storm_stint where id=%s;"),[stintid])
    stintdata = cur.fetchall()

    stinttimes = []

    for stinttime in stintdata:
        ii = [stinttime[0]] + [toSeconds(stinttime[3].replace(tzinfo=None))] + [toSeconds(stinttime[5].replace(tzinfo=None))]
        stinttimes.append(ii)

    

    cur.execute(sql.SQL("select * from storm_studentavailability where student_id=%s;"),[studentid])
    studentdata = cur.fetchall()

    studenttimes = []

    for av in studentdata:
        ii = [av[0]] + [toSeconds(av[6].replace(tzinfo=None))] + [toSeconds(av[7].replace(tzinfo=None))]
        studenttimes.append(ii)

    print("Stint Time ")
    print(stinttimes)
    print("Student Times ")
    print(studenttimes)





isAvailable(1,6)

############################



# Getting stint times

'''cur.execute("select * from storm_stint LIMIT 1;")
stints = cur.fetchall()
 
stinttimes = []

for stint in stints:
    ii = [stint[0]] + [stint[3]] + [stint[5]]
    stinttimes.append(ii)

print(stinttimes[0])

# Getting times when students available

cur.execute("select * from storm_studentavailability LIMIT 1;")
studentavs = cur.fetchall()

studenttimes = []

for av in studentavs:
    ii = [av[0]] + [av[6]] + [av[7]]
    studenttimes.append(ii)

print(studenttimes[0])


# --

#print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("copy storm_stint to 'stint.csv' delimeter ',' csv header;"))
#print(cur.fetchall())

#a = pd.read_sql('select * from storm_student',conn)
#a.to_pickle('student.txt')
#print(a)

#cur.execute("select * from storm_student LIMIT 100;")
#print(cur.fetchall())


# Instead of manually creating categories, it may be worth seeing whether there are correlations 
# between ratings in certain areas across students that allow us to group them more effectively.
'''