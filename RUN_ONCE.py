import pandas as pd
import psycopg2 as py
import login
import numpy as np
import random
from decimal import *
import math
import stats
import timefn
import datetime
from psycopg2 import sql

####################################################################################
# This is a file meant to be run once to make database modifications - uncomment   #
# commented sections to reverse operations such as adding columns                  #
####################################################################################

conn = login.conn
cur = conn.cursor()

# Reading stint type keywords from file 

a = pd.read_excel('txt/keywords.xlsx')
b= a.values

# Generating student columns for ratings in stint types

for i in b:
    tot = i[0] + '_total'
    number = i[0] + '_number'
    average = i[0] + '_average'

    cur.execute("alter table storm_student add %s float;" % tot)
    cur.execute("alter table storm_student add %s int;" % number)
    cur.execute("alter table storm_student add %s float;" % average)

    #cur.execute("alter table storm_student drop %s ;" % tot)
    #cur.execute("alter table storm_student drop %s ;" % average)
    #cur.execute("alter table storm_student drop %s ;" % number)

# Adding stint column for stint type

cur.execute("alter table storm_stint add type_group Text;")
#cur.execute("alter table storm_stint drop type_group ;")

# Adding student columns for overall ratings

cur.execute("alter table storm_student add total_score float;")
cur.execute("alter table storm_student add total_number int;")
cur.execute("alter table storm_student add total_average float;")
#cur.execute("alter table storm_student drop total_average ;")
#cur.execute("alter table storm_student drop total_score ;")
#cur.execute("alter table storm_student drop total_number ;")

# Adding business columns to keep track of past ratings and develop rating distributions

cur.execute("alter table storm_business add past_1 int;" )
cur.execute("alter table storm_business add past_2 int;" )
cur.execute("alter table storm_business add past_3 int;" )
cur.execute("alter table storm_business add past_4 int;" )
cur.execute("alter table storm_business add past_5 int;" )
#cur.execute("alter table storm_business drop past_1 ;")
#cur.execute("alter table storm_business drop past_2 ;")
#cur.execute("alter table storm_business drop past_3 ;")
#cur.execute("alter table storm_business drop past_4 ;")
#cur.execute("alter table storm_business drop past_5 ;")

# Committing database modifications

cur.execute("commit;")
print("Success creating columns.")

# Reads possible entries and keywords for stint types from files

c = pd.read_excel('txt/possible_entries.xlsx')
keywords = pd.read_excel('txt/keywords.xlsx')
keywords_vals = keywords.values

# For a stint, pulls out distribution of ratings associated with that stint

def distribution_maker(bus_id):
    cur.execute(sql.SQL("select past_5, past_4,past_3,past_2,past_1 from  storm_business where id = %s;"),[bus_id])
    distribution = cur.fetchall()[0]
    if sum(distribution) > 20:
        return distribution
    else:
        cur.execute(sql.SQL("select sum(past_5), sum(past_4),sum(past_3),sum(past_2),sum(past_1) from  storm_business;"))
        distribution = cur.fetchall()[0]
        return distribution

# Populating stint type fields created

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

                    bus_id = int(b[3])
                    distr = distribution_maker(bus_id)
                    new_total+=stats.normalize(distr,int(b[2]))
                    cur.execute(sql.SQL("update storm_student set {}=%s where baseuser_ptr_id=%s;").format(sql.Identifier(key_total_test[0])),[new_total,int(b[0])])

                    if new_number != 0:
                        new_average = new_total/float(new_number)
                    else:
                        new_average = 0
                    cur.execute(sql.SQL("update storm_student set {}=%s where baseuser_ptr_id=%s;").format(sql.Identifier(key_average_test[0])),[new_average,int(b[0])])

# Committing changes

cur.execute("commit;")
print("Success populating new columns.")







