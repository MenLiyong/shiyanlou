# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

def co2():

    Income_group = ["High income: OECD","High income: nonOECD","Low income","Lower middle income","Upper middle income"]
    Columns_list = ['Sum_emissions', 'Highest_emission_country', 'Highest_emissions', 'Lowest_emission_country','Lowest_emissions']
    
    df_Data = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    df_Data = df_Data[df_Data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    df_Data.drop(labels=['Country name','Series code', 'Series name', 'SCALE', 'Decimals'], axis=1, inplace=True)
    df_Data.replace({'..':pd.np.NaN},inplace=True)
    df_Data = df_Data.fillna(method='ffill', axis=1).fillna(method='bfill',axis=1)
    df_Data.dropna(how='all', thresh=2,inplace=True)

    df_Country = pd.read_excel("ClimateChange.xlsx",sheetname='Country')   
    df_Country.drop(labels=['Capital city', 'Region', 'Lending category'], axis=1, inplace=True)    
    df_Country.set_index('Country code', inplace=True)

    data = pd.concat([df_Data,df_Country],axis=1,join_axes=[df_Data.index])
    data['Sum emissions'] = data.sum(axis=1)

    results = pd.DataFrame(columns=Columns_list)
    for i in Income_group:
        total_list = []
        re = data[data["Income group"]==i]
        su = data.groupby('Income group').sum() 
        Columns_list[0] = su.loc[i,"Sum emissions"]
        Columns_list[1] = re.max()['Country name']
        Columns_list[2] = re.max()['Sum emissions']
        Columns_list[3] = re.min()['Country name']
        Columns_list[4] = re.min()['Sum emissions']

        total_list = [Columns_list[0], Columns_list[1], Columns_list[2], Columns_list[3], Columns_list[4]]
        results.loc[i] = np.array(total_list) 
    return results
    
if __name__ == '__main__':
    co2()
