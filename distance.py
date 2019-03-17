import numpy as np
import csv
from psycopg2 import sql
import math
import pandas as pd
import psycopg2 as py
import login
import will
import timefn
# Implements Haversine formula to calculate great circle distance between two points on the earth

from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def getdistance(student_id,stint_id):

    conn = login.conn
    cur = conn.cursor()

    # Getting student location

    cur.execute(sql.SQL("select * from storm_studentavailability where student_id = %s;").format(),[student_id])
    datalist = cur.fetchall()
    studentlocation = [datalist[0][8]] + [datalist[0][9]]

    # Getting stint notation

    cur.execute(sql.SQL("select * from storm_stint where id = %s;").format(), [stint_id])
    datalist = cur.fetchall()
    stintlocation = [datalist[0][6]] + [datalist[0][7]]

    return haversine(studentlocation[0], studentlocation[1], stintlocation[0], stintlocation[1])

 
getdistance(6,10)


'''
            cur.execute(sql.SQL("SELECT ref FROM storm_business where id = %s;").format(),[new_bus_ref])

    cur.execute("select * from storm_studentavailability LIMIT 1;")
studentavs = cur.fetchall()

studenttimes = []

for av in studentavs:
    ii = [av[0]] + [av[6]] + [av[7]]
    studenttimes.append(ii)

print(studenttimes[0])
    '''
'''
    traveldistance = haversine(stud_lon,stud_lat,stin_lon,stin_lat)
    return traveldistance'''
