import json, os, sys
import pandas as pd
from matplotlib import pyplot as plt

def data_plot():
    df = pd.read_json('user_study.json')
    data = df.groupby('user_id').sum().head()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(data.index, data.minutes)
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()    
    
'''
def data_plot(file):
    df = pd.read_json(file)
    for i in  tuple(df['user_id'].values):
        id_range=len(df[df['user_id']==i])
        id_study_time = df[df['user_id']==i].minutes.sum()
        yield(id_range, id_study_time)
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.set_title('StudyData')
        ax.set_xlabel('User ID')
        ax.set_ylabel('Study Time')
        x = user_id, y = id_study_time
        ax.plot(x,y,'b-',label=r'$ x=x|y= $')
        ax.legend()
        ax.axis([0,id_range,0,1])
        plt.show()
        return ax
'''
