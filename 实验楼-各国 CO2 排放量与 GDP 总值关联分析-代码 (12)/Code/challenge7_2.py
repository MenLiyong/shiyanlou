import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def co2_gdp_plot():
    df = pd.read_excel("ClimateChange.xlsx")
    co2 = df[df['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code').iloc[:, 5:]
    gdp = df[df['Series code']=='NY.GDP.MKTP.CD'].set_index('Country code').iloc[:, 5:]
    co2.replace({'..': pd.np.nan}, inplace=True)
    gdp.replace({'..': pd.np.nan}, inplace=True)
    co2 = co2.fillna(method='bfill', axis=1).fillna(method='ffill', axis=1)
    gdp = gdp.fillna(method='bfill', axis=1).fillna(method='ffill', axis=1)
    data = pd.concat([co2.sum(1), gdp.sum(1)], axis=1)
    data.columns = ['CO2-SUM', 'GDP-SUM']
    data.fillna(0, inplace=True)
    data = data.apply(lambda x: (x-x.min())/(x.max()-x.min()))
    label, position = [], []
    for i in range(len(data)):
        if data.index[i] in ['CHN', 'USA', 'RUS', 'FRA', 'GBR']:
            label.append(data.index[i])
            position.append(i)
    fig = plt.subplot()
    data.plot(title='GDP-CO2', ax=fig, kind='line')
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(position, label, rotation='vertical')
    plt.show()
    return fig, np.round(data['CHN':'CHN'].values, 3).tolist()[0]

print(co2_gdp_plot())
'''
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def co2_gdp_plot():
    code_list = ['EN.ATM.CO2E.KT','NY.GDP.MKTP.CD']
    data1 = handle_data(code_list[0])
    data2 = handle_data(code_list[1])  
    data1['sum_co2'] = data1.sum(axis=1)
    data2['sum_gdp'] = data2.sum(axis=1)  
    data = pd.concat([data1, data2],axis=1,join_axes=[data1.index])
    draw(data)

def handle_data(code):
    df = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    data = df[df['Series code']==code].set_index('Country code')
    data.drop(labels=['Country name','Series code', 'Series name', 'SCALE', 'Decimals'], axis=1, inplace=True)
    data.replace({'..':pd.np.NaN},inplace=True)
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill',axis=1)
    data.replace({pd.np.NaN:0},inplace=True)
    return data

def draw(data):
    #data of picture
    max_co2 = data['sum_co2'].max()
    min_co2 = data['sum_co2'].min()
    max_gdp = data['sum_gdp'].max()
    min_gdp = data['sum_gdp'].min()
    num = len(data.index)
    Y, Z = [], []
    for i in data.index:
        y = (data.loc[i,'sum_co2'] - min_co2) / (max_co2 - min_co2)
        z = (data.loc[i,'sum_gdp'] - min_gdp) / (max_gdp - min_gdp)
        Y.append(y)
        Z.append(z)
    #draw the picture
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x = np.linspace(0,num,num)
    ax.set_title('GDP-CO2')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Values')
    ax.plot(x, Y, 'b-', label=r'CO2-SUM')
    ax.plot(x, Z, 'y-',label=r'GDP-SUM')
    ax.legend(['CO2-SUM', 'GDP-SUM'], loc="upper left")    
    labels = ['CHN', 'USA', 'RUS', 'FRA', 'GBR']
    #get_index_of_labels_element
    position_list = []
    for i in labels:
        i_index = np.argwhere(data.index==i)
        position_list.append(i_index)
    plt.xticks(position_list, labels, rotation='vertical')
    fig.show()
    #get_value_of_CHN(china)
    a = (%.3f % Y[int(position_list[0])])
    b = (%.3f % Z[int(position_list[0])])
    china = [a, b]
    return fig, china
    
if __name__ == '__main__':
    co2_gdp_plot()
'''
