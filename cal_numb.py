import numpy as np
import math
import pandas as pd
import psycopg2 as py

conn = py.connect("dbname=hackathon user=postgres password=pw")

cur = conn.cursor()
#cur.execute("select storm_stint.student_id,type,grade from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;")
#cur.execute("select * from storm_student LIMIT 1;")
#print(cur.fetchall())
c = pd.read_excel('possible_entries.xlsx')
keywords = pd.read_excel('keywords.xlsx')
keywords_vals = keywords.values


cur.execute("update storm_student set wait_number=0;" )
cur.execute("commit;")


#print(c.values[0][2])
a = pd.read_sql("select storm_stint.student_id,type,grade from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;",conn)
cur.execute("update storm_student set bar_number=0;" )
nump = c.values
for j in range(18):
    print(keywords_vals[j])
    for i in range(18):
        if nump[j][i] != "nan" and isinstance(nump[j][i],str) :
            to_test = nump[j][i]
            print(to_test)
            key_num_test = keywords_vals[j] +'_number'
            num_test = to_test+'_number'
            total_test = to_test+'_total'
            average_test = to_test+'_average'
            for i in range(a.shape[0]):
                b = a.loc[i].values
                print(b)
                if b[1] == to_test:
                    print(key_num_test[0])
                    print(b[0])
                    cur.execute("select %s from storm_student where baseuser_ptr_id=%s;",(str(key_num_test[0]),int(b[0])))
                    #query = "select %s from storm_student where baseuser_ptr_id=%s;"
                    #cur.execute(query,([key_num_test[0]],int(b[0])))
                    #cur.execute("select bar_number from storm_student where baseuser_ptr_id =%s;" , int(b[0]))     c = cur.fetchall()
                    c = cur.fetchall()
                    print("hu")
                    print(c)
                    d = int(c[0][0])
                    print("d")
                    print(d)
                    d+=1
                    cur.execute("update storm_student set %s=%s where baseuser_ptr_id=%s;" , (num_test,d,int(b[0])) )
                    

#for i in range(a.shape[0]):
#    b = a.loc[i].values
#    if b[1] == "Bar Back":
#        cur.execute("select bar_number from storm_student where baseuser_ptr_id=%s;",[int(b[0])])
#        #cur.execute("select bar_number from storm_student where baseuser_ptr_id =%s;" , int(b[0]))
#        c = cur.fetchall()
#        d = int(c[0][0])
#        d+=1
#        cur.execute("update storm_student set bar_number=%s where baseuser_ptr_id=%s;" , (d,int(b[0])) )
#        #cur.execute("update storm_student set bar_number=%s where baseuser_ptr_id = %s;" %(b[1],b[0]))
#
#
#    #print(b)
#
#cur.execute("update storm_student set bar_number=100;" )
cur.execute("commit;")

cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")
#print(cur.fetchall())
#print(cur.fetchall())

cur.execute("select bar_number,baseuser_ptr_id from storm_student where bar_number != 0;")
#print(cur.fetchall())

















