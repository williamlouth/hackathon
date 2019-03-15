import psycopg2 as py
import login

conn = login.conn
#conn  = py.connect("dbname = hack user = will")
cur = conn.cursor()
print(cur.execute("select * FROM storm_stint LIMIT 1;"))
print(cur.fetchall())

# added comment
