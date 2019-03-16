import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login

conn =  login.conn
cur = conn.cursor()
#cur.execute("select storm_stint.student_id,type,grade from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;")
#cur.execute("select * from storm_student LIMIT 1;")
#print(cur.fetchall())


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


cur.execute("commit;")
cur.execute("select * from storm_business limit 1 offset 3;")
print(cur.fetchall())
    



























