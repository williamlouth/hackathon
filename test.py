import psycopg2 as py


conn  = py.connect("dbname = hack user = will")
cur = conn.cursor()
print(cur.execute("select * FROM storm_stint;"))
print(cur.fetchall())


