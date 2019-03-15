import psycopg2 as py
import login

conn = login.conn
#conn  = py.connect("dbname = hack user = will")

cur = conn.cursor()
print(cur.execute("select * FROM storm_stint LIMIT 1;"))
print(cur.fetchall())
print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("dt;"))
print(cur.fetchall())

# Instead of manually creating categories, it may be worth seeing whether there are correlations 
# between ratings in certain areas across students that allow us to group them more effectively.

