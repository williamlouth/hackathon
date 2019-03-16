import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import datetime
import mergetime


conn = login.conn
cur = conn.cursor()

##print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_studentavailability';"))
#print(cur.fetchall())

#cur.execute("select * from storm_studentavailability LIMIT 1;")
#print(cur.fetchall())

def Sort(sub_list): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_list.sort(key = lambda x: x[1]) 
    return sub_list

def toSeconds(t):
    return (t-datetime.datetime(1970,1,1)).total_seconds() 

def isAvailable(stintid,studentid):

    cur.execute(sql.SQL("select * from storm_stint where id=%s;"),[stintid])
    stintdata = cur.fetchall()

    stinttimes = []

    for stinttime in stintdata:
        ii = [toSeconds(stinttime[3].replace(tzinfo=None))] + [toSeconds(stinttime[5].replace(tzinfo=None))]
        stinttimes.append(ii)

    stinttimes = stinttimes[0]

    cur.execute(sql.SQL("select * from storm_studentavailability where student_id=%s;"),[studentid])
    studentdata = cur.fetchall()

    studenttimes = []

    for av in studentdata:
        ii = [toSeconds(av[6].replace(tzinfo=None))] + [toSeconds(av[7].replace(tzinfo=None))]
        studenttimes.append(ii)
    

    print("Stint Time")
    print(stinttimes)
    print("Student Times")
    print(studenttimes)
    print("Student Times 2")
    print(Sort(studenttimes))

    sorted_studenttimes = mergetime.merge_times(Sort(studenttimes))

    # Testing if stint time is included in one of the student times

    for time in sorted_studenttimes:
        if time[0] < stinttimes[0] and time[1] > stinttimes[1]:
            return True
    return False

print(isAvailable(1,6))
