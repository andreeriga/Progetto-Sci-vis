# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: .env
#     language: python
#     name: python3
# ---

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

df = pd.read_csv('POKEMON/Pokemon-Database.csv',index_col=0)
df

df.columns

df['Game(s) of Origin']

t = [x[1:len(x)-1] for x in df['Primary Type'].values]
tipi = pd.Series(t,df['Primary Type'].index)
tipi

sec = df['Secondary Type'].dropna()
t2 = [x[1:len(x)-1] for x in sec.values]
tipi2 = pd.Series(t2,sec.index)
tipi2

print('CALCOLIAMO LE FREQUENZE DEI VARI TIPI DI POKEMON')

ax = tipi.value_counts().sort_index().plot.barh(
    color= '#446cc2',
           alpha = .6
)
plt.title('Frequenze dei Tipi primari dei Pokemon')
ax.invert_xaxis()
ax.yaxis.tick_right()
plt.gcf().set_facecolor('#e3e7f0')
plt.xticks(np.arange(0,181,20))
plt.show()

print('aqua','darkgrey','green','lime','pink','red','chocolate','yellow','purple','khaki','black',
           'saddlebrown','violet','purple','grey','lightblue','magenta','blue')

tipi.value_counts().index

tipi.value_counts().sort_index().index

labels = tipi.value_counts().index
values = tipi.value_counts().values
pulls = [0.1,0.1,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,opacity=.7, pull=pulls,marker=dict(colors = [
    '#6390F0','#A8A77A','#7AC74C','#F95587','#A6B91A','#F7D02C','#EE8130','#B6A136','#705746','#C22E28','#D685AD','#735797','#E2BF65','#B7B7CE',
    '#A33EA1','#6F35FC','#96D9D6','#A98FF3'
]))])
fig.update_traces(textposition='inside')
fig.update_layout(
    paper_bgcolor = "#e3e7f0",
    uniformtext_minsize=12, 
    uniformtext_mode='hide'
)
fig.show()

counts = tipi2.value_counts().sort_index()
ax = counts.plot.barh(
    color='#e89e1e',
    alpha=0.6
)
plt.title('Frequenze dei Tipi secondari dei Pokemon')
plt.gcf().set_facecolor('#e3e7f0')
plt.xticks(np.arange(0,181,20))
plt.show()

confronto_tipi = pd.DataFrame(
    {
        'Primary Freq': tipi.value_counts().sort_index().values,
        'Secondary Freq': tipi2.value_counts().sort_index().values
    },
    index = tipi.value_counts().sort_index().index
)
confronto_tipi

confronto_tipi.plot.barh(color=['#446cc2','#e89e1e'], alpha = .6)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.title('Confronto frequenze tipo primario e tipo secondario')
plt.show()

df['Primary Type'].unique()

tipi_principali = [
    ('"Grass"','#009300','#02f702'),('"Water"','#015691','#007DD4'),('"Fire"','#911201','#FF2E12'),('"Electric"','y','#F3DF15')
    ]
for x in tipi_principali : 
    data = df[df['Primary Type'] == x[0]]['Attack Stat']
    data2 = df[df['Primary Type'] == x[0]]['Defense Stat']
    sns.kdeplot(data2, color='blue',alpha=0.5, label='Difesa', fill=False)
    sns.kdeplot(data, color='red', alpha=0.5, label='Attacco', fill=False)
    plt.legend()
    plt.xlabel('valori')
    plt.ylabel('Densità')
    plt.gcf().set_facecolor('#e3e7f0')
    plt.xticks(np.arange(-50, 251, 50))
    plt.yticks(np.arange(0, 0.020, 0.002))
    plt.show()

principal_types = [('"Grass"','g'),('"Fire"','r'),('"Electric"','y'),('"Water"','b')]
for s in principal_types :
    data = df[df['Primary Type'] == s[0]]['Attack Stat']
    sns.kdeplot(data, color=s[1])
    plt.gcf().set_facecolor('#e3e7f0')
    plt.xlabel('Attacco')
    plt.ylabel('Densità')
plt.show()


