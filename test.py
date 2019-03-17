import pandas as pd
import psycopg2 as py
import login

conn = login.conn
#conn  = py.connect("dbname = hack user = will")

cur = conn.cursor()

print(cur.execute("select * FROM storm_stint LIMIT 1;"))

print(cur.fetchall())
print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_studentavailability';"))
#print(cur.execute("dt;"))
print(cur.fetchall())
#cur.execute("select * from storm_student LIMIT 1;")
#print(cur.fetchall())

#print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("copy storm_stint to 'stint.csv' delimeter ',' csv header;"))
#print(cur.fetchall())

a = pd.read_sql('select * from storm_business',conn)
a.to_pickle('new_business.txt')
#print(a)

#cur.execute("select * from storm_student LIMIT 1;")

# Instead of manually creating categories, it may be worth seeing whether there are correlations 
# between ratings in certain areas across students that allow us to group them more effectively.
