import pandas as pd
import psycopg2 as py
import login

conn = login.conn

cur = conn.cursor()
#cur.execute("select storm_stint.student_id,type,grade from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;")
#cur.execute("select * from storm_student LIMIT 1;")
#print(cur.fetchall())
a = pd.read_sql("select storm_stint.student_id,type,grade from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;",conn)
#print(a)
for i in range(a.shape[0]):
    b = a.loc[i].values
    if b[1] == "Bar Back":
        print("HIT")
        #cur.execute("update storm_student set bar_number=100;" )


    #print(b)

cur.execute("update storm_student set bar_number=100;" )
cur.execute("commit;")

cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")
print(cur.fetchall())
#print(cur.fetchall())

cur.execute("select bar_number from storm_student where bar_number = 100;")
print(cur.fetchall())

















