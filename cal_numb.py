import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import stats
import timefn
import login

conn =  login.conn
cur = conn.cursor()
c = pd.read_excel('txt/possible_entries.xlsx')
keywords = pd.read_excel('txt/keywords.xlsx')
keywords_vals = keywords.values

def distribution_maker(bus_id):
    cur.execute(sql.SQL("select past_5, past_4,past_3,past_2,past_1 from  storm_business where id = %s;"),[bus_id])
    distribution = cur.fetchall()[0]
    if sum(distribution) > 20:
        return distribution
    else:
        cur.execute(sql.SQL("select sum(past_5), sum(past_4),sum(past_3),sum(past_2),sum(past_1) from  storm_business;"))
        distribution = cur.fetchall()[0]
        return distribution

a = pd.read_sql("select storm_stint.student_id,type,grade,storm_review.business_id from storm_stint inner join storm_review on storm_stint.id = storm_review.stint_id;",conn)
nump = c.values
for j in range(18):
    print(j)
    key_num_test = keywords_vals[j] +'_number'
    key_total_test = keywords_vals[j] +'_total'
    key_average_test = keywords_vals[j] +'_average'

    cur.execute(sql.SQL("update storm_student set {}=0;").format(sql.Identifier(str(key_num_test[0]))))
    cur.execute(sql.SQL("update storm_student set {}=0.0;").format(sql.Identifier(str(key_total_test[0]))))
    cur.execute(sql.SQL("update storm_student set {}=0.0;").format(sql.Identifier(str(key_average_test[0]))))
    cur.execute("commit;")

    print(keywords_vals[j])
    for i in range(18):
        if nump[j][i] != "nan" and isinstance(nump[j][i],str) :
            to_test = nump[j][i]
            num_test = to_test+'_number'
            total_test = to_test+'_total'
            average_test = to_test+'_average'
            for i in range(a.shape[0]):
                b = a.loc[i].values
                if b[1] == to_test:
                    cur.execute(sql.SQL("select {} from storm_student where baseuser_ptr_id=%s;").format(sql.Identifier(key_num_test[0])),[int(b[0])])
                    c = cur.fetchall()
                    new_number = int(c[0][0])
                    new_number+=1
                    cur.execute(sql.SQL("update storm_student set {}=%s where baseuser_ptr_id=%s;").format(sql.Identifier(key_num_test[0])),[new_number,int(b[0])])
                    
                    cur.execute(sql.SQL("select {} from storm_student where baseuser_ptr_id=%s;").format(sql.Identifier(key_total_test[0])),[int(b[0])])
                    c = cur.fetchall()
                    new_total = float(c[0][0])

                    #cur.execute(sql.SQL("select business_id from storm_stint where id=%s;").format(),[int(b[3])])
                    #bus_id = cur.fetchall()[0][0]
                    bus_id = int(b[3])
                    distr = distribution_maker(bus_id)
                    new_total+=stats.normalize(distr,int(b[2]))
                    cur.execute(sql.SQL("update storm_student set {}=%s where baseuser_ptr_id=%s;").format(sql.Identifier(key_total_test[0])),[new_total,int(b[0])])

                    if new_number != 0:
                        new_average = new_total/float(new_number)
                    else:
                        new_average = 0
                    cur.execute(sql.SQL("update storm_student set {}=%s where baseuser_ptr_id=%s;").format(sql.Identifier(key_average_test[0])),[new_average,int(b[0])])


cur.execute("commit;")

cur.execute("select * from storm_student LIMIT 1;")
print(cur.fetchall())
cur.execute("select column_name from information_schema.columns where table_name = 'storm_student';")










