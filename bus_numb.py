import numpy as np
from psycopg2 import sql
import csv
import math
import pandas as pd
import psycopg2 as py
import login
import io

conn =  login.conn
cur = conn.cursor()


with io.open('txt/BusinessRank.csv',encoding='utf-8') as f:
    r = csv.reader(f)
    bus_ranks = list(r)

for i in range(1,6):
    field = "past_" + str(i)
    cur.execute(sql.SQL("update storm_business set {}=0;").format(sql.Identifier(str(field))))
cur.execute("commit;")

cur.execute("select grade,business_id from storm_review;")
data = cur.fetchall()
for i in data:
    grade = i[0]
    bus_id = i[1]
    field = "past_" + str(grade)

    cur.execute(sql.SQL("update storm_business set {}={}+1 where id=%s;").format(sql.Identifier(field),sql.Identifier(field)),[bus_id])

cur.execute(sql.SQL("update storm_business set rank=0;")) #set all rank to zero
for i in bus_ranks[1:]:
    rank = i[1]
    if len(rank) == 0:
        rank =0
    m_id = i[0]
    rank = int(rank)
    cur.execute(sql.SQL("update storm_business set rank=%s where ref=%s;"),[rank,m_id])

    cur.execute("commit;")


cur.execute("commit;")
cur.execute("select * from storm_business limit 1 offset 3;")
print(cur.fetchall())
    



























