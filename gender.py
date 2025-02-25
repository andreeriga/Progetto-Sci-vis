# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Statistica
#     language: python
#     name: python3
# ---

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('POKEMON/Pokemon-Database.csv')
df

df2 = pd.read_csv

f = df['Primary Type'].value_counts()
lista_m = []
for x in f.index:
    lista_m.append((x,df[df['Primary Type']==x]['Male Ratio'].mean()))
lista_m

f = df['Primary Type'].value_counts()
lista_f = []
for x in f.index:
    lista_f.append((x,df[df['Primary Type']==x]['Female Ratio'].mean()))
lista_f


comparazione_gender = pd.DataFrame(
    {
        'Maschio': [m[1] for m in lista_m],
        'Femmina': [f[1] for f in lista_f]
    },
    index = [i[0][1:len(i[0])-1] for i in lista_m]
)
comparazione_gender

comparazione_gender.plot.barh(color=['#6ab1f7','#f07daf'], alpha=.7)
plt.gcf().set_facecolor('#e3e7f0')
plt.show()
