# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import time

def climate_plot():

    df_t = pd.read_excel("GlobalTemperature.xlsx")
    df_c= pd.read_excel("ClimateChange.xlsx")
    series_code = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE',
                   'EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE'] 
    columns = ['Land Average Temperature', 'Land Max Temperature',
               'Land Min Temperature', 'Land And Ocean Average Temperature','TotalGHG']               

    # Handle_climate_data
    df_c = df_c.set_index('Series code').iloc[:, 5:].loc[series_code]
    df_c.replace({'..': pd.np.nan}, inplace=True)
    df_c = df_c.fillna(method='bfill', axis=1).fillna(method='ffill', axis=1) 
    df_c.dropna(how='all',thresh=1,inplace=True) 
    data_c = pd.DataFrame(df_c.sum()) 
    data_c.drop(data_c.index[[-1]], inplace=True)   # data of each year for subplot 1 & 2

    # Handle_temperature_data
    df_t['Date'] = pd.to_datetime(df_t['Date'])
    df_t = df_t.set_index('Date')
    data_t = df_t['1990':'2010'].resample('A-DEC').mean() 
    data_t = pd.DataFrame(data_t.iloc[:,:].values,index=data_c.index)

    data_Q =  df_t.resample('Q').mean()     
    data_Q.drop(['Land Max Temperature','Land Min Temperature'], axis=1,inplace=True)   # for ax (3 \ 4)

    # Data of subplot
    data1 = pd.concat([data_t, data_c],axis=1) 
    data1.columns = columns
    data1.drop(['Land Max Temperature','Land Min Temperature'], axis=1,inplace=True)
    data1 = data1.apply(lambda x: (x-x.min())/(x.max()-x.min()))    # for ax (1 \ 2)

    # Draw the picture
    fig, axes = plt.subplots(2,2)
    ax1 = data1.plot(ax=axes[0,0], kind='line',figsize=(16,9))
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')
    
    ax2 = data1.plot(ax=axes[0,1], kind='bar',figsize=(16,9))
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')
    
    ax3 = data_Q.plot(ax=axes[1,0], kind='area',figsize=(16,9))
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')
    
    ax4 = data_Q.plot(ax=axes[1,1], kind='kde',figsize=(16,9))
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')
    fig.subplots_adjust(left=0.05,right=.99,bottom=0.07,top=0.99)
    plt.show()
    time.sleep(5)
    return fig
print(climate_plot())  
