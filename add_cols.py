import pandas as pd
import psycopg2 as py
import login

conn = login.conn

cur = conn.cursor()

a = pd.read_excel('keywords.xlsx')
b=a.values
print(b)

for i in b:
    print(i[0])
    tot = i[0] + '_total'
    number = i[0] + '_number'
    average = i[0] + '_average'

    cur.execute("alter table storm_student add %s float;" % tot)
    cur.execute("alter table storm_student add %s int;" % number)
    cur.execute("alter table storm_student add %s float;" % average)
    #cur.execute("alter table storm_student drop %s ;" % tot)
    #cur.execute("alter table storm_student drop %s ;" % average)
    #cur.execute("alter table storm_student drop %s ;" % number)

    print(tot)
    
cur.execute("alter table storm_student add total_score float;")
cur.execute("alter table storm_student add total_number int;")
cur.execute("alter table storm_student add total_average float;")
#cur.execute("alter table storm_student drop total_average ;")
#cur.execute("alter table storm_student drop total_score ;")
#cur.execute("alter table storm_student drop total_number ;")


#cur.execute("alter table storm_business add past_1 int;" )
#cur.execute("alter table storm_business add past_2 int;" )
#cur.execute("alter table storm_business add past_3 int;" )
#cur.execute("alter table storm_business add past_4 int;" )
#cur.execute("alter table storm_business add past_5 int;" )
#cur.execute("alter table storm_business drop past_1 ;")
#cur.execute("alter table storm_business drop past_2 ;")
#cur.execute("alter table storm_business drop past_3 ;")
#cur.execute("alter table storm_business drop past_4 ;")
#cur.execute("alter table storm_business drop past_5 ;")

cur.execute("select column_name from information_schema.columns where table_name = 'storm_business';")
print(cur.fetchall())
#print(cur.fetchall())
#cur.execute("alter table storm_student drop bar_number ;")
#cur.execute("select * from storm_student LIMIT 1;")
#print(cur.fetchall())
cur.execute("commit;")
cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")
print(cur.fetchall())
#print(cur.fetchall())


















