import numpy as np
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login

conn =  login.conn
cur = conn.cursor()
c = pd.read_excel('txt/possible_entries.xlsx')
keywords = pd.read_excel('txt/keywords.xlsx')
keywords_vals = keywords.values
c_vals = c.values
for i in range(0,17):
    print(keywords_vals[i])
    for j in range(0,17):
        if isinstance(c_vals[i][j],str):
            cur.execute(sql.SQL("update storm_stint set type_group=%s where type = %s;"),[i,str(c_vals[i][j])])

cur.execute("commit;")













