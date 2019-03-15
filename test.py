import psycopg2 as py


conn = py.connect("dbname = hackathon user = postgres password=Koteczek123")
cur = conn.cursor()
print(cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'YourTableName'"))
print(cur.fetchall())



