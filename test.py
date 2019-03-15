import psycopg2 as py
import login

conn = login.conn
#conn  = py.connect("dbname = hack user = will")
cur = conn.cursor()
print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("dt;"))
print(cur.fetchall())


