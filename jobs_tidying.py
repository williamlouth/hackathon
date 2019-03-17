import pandas as pd
import numpy as np
import seaborn as sns
from pandas import ExcelWriter
import will as w

df_stint = pd.read_pickle("stint.txt")
#df_business = pd.read_pickle("business.txt")
#df_review = pd.read_pickle("review.txt")
#df_student = pd.read_pickle("student.txt")
#df_studentavailability = pd.read_pickle("studentavailability.txt")
#df_university = pd.read_pickle("university.txt")


def count_works(type):
    return np.sum(df_stint['type'].str.contains('{}'.format(type), regex=True, case=False))


def create_series_of(series, type):
    return series[series.str.contains('{}'.format(type), regex=True, case=False) == True]


def get_list_of_works(series, type):
    return create_series_of(series, type).drop_duplicates().tolist()


def delete_from_series(series, list):
    return series[~series.isin(list)].dropna()


def flatten(list):
    flat_list = []
    for sublist in list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def save_to_excel(df, name):
    writer = pd.ExcelWriter('{}.xlsx'.format(name))
    df.to_excel(writer)
    writer.save()


list_of_works = []
my_series = df_stint['type']
keywords = ['wait', 'run', 'bar', 'cust', 'kitch', 'leaf', 'cloak',
            'cashier', 'host', 'clean', 'stock', 'door', 'other', 'errand',
            'deliv', 'chef', 'proof', 'assis']
for word in keywords:
    list_of_works.append(get_list_of_works(my_series, '{}'.format(word)))
    #print(list_of_works[keywords.index(word)])
    my_series = delete_from_series(my_series, list_of_works[keywords.index(word)])

print(my_series.value_counts())
#print(my_series.shape[0])
#print(list((2,2)))
w.iter_loop()