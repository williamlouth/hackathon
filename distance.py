import psycopg2 as py
import login
import numpy as np
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

def work_with(student_id,stint_id):

    conn = login.conn
    cur = conn.cursor()
    

    traveldistance = haversine(stud_lon,stud_lat,stin_lon,stin_lat)
    return traveldistance
