import pandas as pd
import psycopg2 as py
import login

conn = login.conn

cur = conn.cursor()

a = pd.read_excel('keywords.xlsx')
b=a.values
print(b)
#c = pd.read_excel('possible_entries.xlsx')
#print(c)
#empty_list = []
#for  i in range(c.shape[0]):
#    empty_list.append(c.iloc[i].values)
# 
#print(empty_list)
#for i in empty_list:
#    print(i)
#    print("hi")

for i in b:
    print(i[0])
    tot = i[0] + '_total'
    number = i[0] + '_number'
    average = i[0] + '_average'
    cur.execute("alter table storm_student add %s int;" % tot)
    cur.execute("alter table storm_student add %s int;" % number)
    cur.execute("alter table storm_student add %s int;" % average)
    #cur.execute("alter table storm_student drop %s ;" % tot)
    #cur.execute("alter table storm_student drop %s ;" % average)
    #cur.execute("alter table storm_student drop %s ;" % number)

#cur.execute("alter table storm_student drop bar_number ;")
cur.execute("select * from storm_student LIMIT 1;")
print(cur.fetchall())
cur.execute("commit;")
cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")
print(cur.fetchall())
#print(cur.fetchall())


















