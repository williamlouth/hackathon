# Location Test
import pandas as pd
import psycopg2 as py

conn = py.connect("dbname=hackathon user=postgres password=pw")
cur = conn.cursor()
cur.execute("SELECT student_id, longitude, latitude FROM storm_studentavailability;")

output = cur.fetchall()
print(output)
