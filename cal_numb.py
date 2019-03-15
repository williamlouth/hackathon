import pandas as pd
import psycopg2 as py
import login

conn = login.conn

cur = conn.cursor()
cur.execute("alter table storm_student add bar_average int ;")
cur.execute("select * from storm_student LIMIT 1;")
print(cur.fetchall())
cur.execute("commit;")
cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")
print(cur.fetchall())
#print(cur.fetchall())


















