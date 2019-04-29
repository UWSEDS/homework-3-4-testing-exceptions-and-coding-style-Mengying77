"""This module create a dataframe df from reading the data in hw2.py"""
from hw2 import df

LIST_OF_COLS = ('COUNT PARTICIPANTS', 'COUNT PERMANENT RESIDENT ALIEN', 'COUNT US CITIZEN',
                'COUNT CITIZEN STATUS TOTAL')

"""This woould generate an ValueError execption if the dataframe doesn't have the expected
column name as defined above"""
for i in LIST_OF_COLS:
    if i not in list(df.columns):
        raise ValueError('No expected column')
