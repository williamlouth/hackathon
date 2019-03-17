# Populates studentavailability to allow for testing of 
# matching algorithm with implementation of time matching

import numpy as np
import random
from decimal import *
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import stats
import timefn
import login
import datetime

conn =  login.conn
cur = conn.cursor()
#c = pd.read_excel('txt/possible_entries.xlsx')
#keywords = pd.read_excel('txt/keywords.xlsx')
#keywords_vals = keywords.values


#cur.execute(sql.SQL("ALTER TABLE storm_studentavailability ALTER COLUMN id SERIAL ;"))

cur.execute(sql.SQL("select max(id) from storm_studentavailability"))
id_max = cur.fetchall()[0][0]
id_max +=1
cur.execute(sql.SQL("select count(id) from storm_stint"))
stu_len = cur.fetchall()[0][0]

for i in range(stu_len):
    cur.execute(sql.SQL("select max(id) from storm_studentavailability"))
    id_max = cur.fetchall()[0][0]
    id_max +=1
    #cur.execute(sql.SQL("select max(ref) from storm_studentavailability"))
    #ref_max = cur.fetchall()[0][0]
    #ref_max +=1
    ref_max = str(random.randint(10000,999999999999))
    cur.execute(sql.SQL("insert into storm_studentavailability (id,student_id,date_from,date_to,longitude,latitude,created_at,modified_at,ref,address,disabled) select %s, student_id,date_from,date_to,longitude,latitude,date_from,date_from,%s,location_address,false from storm_stint limit 1;"),[id_max,ref_max])
