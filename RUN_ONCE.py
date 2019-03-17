import pandas as pd
import psycopg2 as py
import login

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
print("Success")

















