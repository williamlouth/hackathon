import pandas as pd
import psycopg2 as py
import login

conn = login.conn
cur = conn.cursor()

# Getting stint times

cur.execute("select * from storm_stint LIMIT 1;")
stints = cur.fetchall()

stinttimes = []

for stint in stints:
    ii = [stint[0]] + [stint[3]] + [stint[5]]
    stinttimes.append(ii)

print(stinttimes[0])

# Getting times when students available

cur.execute("select * from storm_studentavailability LIMIT 1;")
studentav = cur.fetchall()
print(studentav)

cur.execute("select column_name from information_schema.columns where table_name = 'storm_studentavailability';")
print(cur.fetchall())

# --

#print(cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';"))
#print(cur.execute("copy storm_stint to 'stint.csv' delimeter ',' csv header;"))
#print(cur.fetchall())

#a = pd.read_sql('select * from storm_student',conn)
#a.to_pickle('student.txt')
#print(a)

#cur.execute("select * from storm_student LIMIT 100;")
#print(cur.fetchall())


# Instead of manually creating categories, it may be worth seeing whether there are correlations 
# between ratings in certain areas across students that allow us to group them more effectively.
