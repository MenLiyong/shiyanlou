# -*- coding:utf-8 -*-
import pandas as pd 
from pandas import Series

def quarter_volume():

    data = pd.read_csv('apple.csv', header=0)
    timeindex = pd.to_datetime(data['Date'])
    data1 = pd.Series(list(data.Volume), index = timeindex)
    data2 = data1.resample('Q').sum().sort_values(ascending=False)
    second_volume = data2[1]

    return second_volume

if __name__ == '__main__':
    quarter_volume()