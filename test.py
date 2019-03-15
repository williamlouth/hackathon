import pandas as pd
import psycopg2 as py
import login

conn = login.conn
#conn  = py.connect("dbname = hack user = will")
cur = conn.cursor()
#print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("copy storm_stint to 'stint.csv' delimeter ',' csv header;"))
#print(cur.fetchall())


a = pd.read_sql('select * from storm_student',conn)
a.to_pickle('student.txt')
print(a)
