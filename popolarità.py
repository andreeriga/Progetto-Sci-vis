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

pop_ita = pd.read_csv("POKEMON/Popolarità/popolaritaITA.csv", index_col=0)
pop_ita

print('Popolarità in italia')

pop_ita.plot.area(legend = False, color = '#E41F25', alpha = .5)
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.xlabel('Anno')
plt.ylabel('Popolarità in Italia')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()

print('Popolarità nel mondo')

pop_mondo = pd.read_csv('POKEMON/Popolarità/popolaritaMONDO.csv',index_col=0)
pop_mondo

pop_mondo.plot.area(legend = False, color = '#23b84a', alpha = .5)
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.xlabel('Anno')
plt.ylabel('Popolarità nel Mondo')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()

print('Confronto i due grafici')

confronto_popolarita = pd.DataFrame({
    'Mondo': [x[0] for x in pop_mondo.values],
    'Italia': [x[0] for x in pop_ita.values]},
    index = pop_ita.index
)
confronto_popolarita

#confronto_popolarita.plot.area(color=['#23b84a','#E41F25'], alpha = .5)
plt.plot(confronto_popolarita['Italia'], color='#E41F25', alpha = .65,label="Italia")
plt.plot(confronto_popolarita['Mondo'], color='#23b84a', alpha = .5,label="Mondo")
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.xlabel('Anno')
plt.ylabel('Popolarità a confronto')
plt.gcf().set_facecolor('#e3e7f0')
plt.legend()
plt.show()


