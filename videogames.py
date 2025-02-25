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
import plotly.graph_objects as go

vg = pd.read_csv('VIDEOGAMES/vgsales.csv', index_col=0)
vg

pokemon = vg[['Pokemon' in s for s in vg['Name']]]
nintendo = vg[vg['Publisher'] == 'Nintendo']

top_100 = vg[:100]

vg.columns

percentuale_pokemon = len(pokemon)/len(nintendo)
percentuale_non_pokemon = 1 - percentuale_pokemon
(percentuale_pokemon,percentuale_non_pokemon)

labels = ['Pokémon', 'Altri giochi Nintendo']
values = [percentuale_pokemon*100,percentuale_non_pokemon*100]
pulls = [0.1,0]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=pulls,marker_colors=['lightblue','rgba(32, 199, 49,.7)'],textinfo='none')])
fig.update_traces(textposition='inside')
fig.update_layout(
    paper_bgcolor = "#e3e7f0",
    uniformtext_minsize=12, 
    uniformtext_mode='hide'
)
fig.show()

publisher = vg[:100]['Publisher'].unique()
def mean_vendite(df, publishers) :
    res = []
    for publisher in publishers :
        media_vendite = df[df['Publisher'] == publisher]['Global_Sales'].mean()*(10**3)
        res.append((publisher, media_vendite))
    return res
medie = mean_vendite(vg,publisher)
medie

serie_medie_vendite = pd.Series(
    [x[1] for x in medie],
    [x[0] for x in medie]
)
serie_medie_vendite

serie_medie_vendite.plot.barh(
    color='lightgreen',
    alpha=.7
)
plt.gcf().set_facecolor('#e3e7f0')
plt.xlabel('Migliaia di copie vendute')
plt.show()

pokemon_top_100 = top_100[['Pokemon' in s for s in top_100['Name']]]
pokemon_top_100

#prendo tutti i giochi della nintendo che non sono pokemon in top 100
nintendo_top_100 = top_100[top_100['Publisher'] == 'Nintendo']
nintendo_top_100.head()

#tutti gli altri "giochi/publisher" in top 100
altri_top_100 = top_100[top_100['Publisher'] != 'Nintendo']
altri_top_100


def diversi_publ(df, nomi):
    res = []
    for nome in nomi:
        res.append((nome,len(df[df['Publisher'] == nome])))
    return res
els = []
for x in diversi_publ(altri_top_100, altri_top_100['Publisher'].unique()) : 
    els.append(x)
els.append(('Pokémon', len(pokemon_top_100)))
els.append(('Nintendo', len(nintendo_top_100)))
els 

labels = [x[0] for x in els]
values = [x[1] for x in els]
colors = [
    'rgba(255, 99, 132, .7)',  # Rosso
    'rgba(117, 112, 111, .7)',  # Blu
    'rgba(255, 206, 86, .7)',  # Giallo
    'rgba(75, 192, 192, .7)',  # Verde acqua
    'rgba(153, 102, 255, .8)', # Viola
    'rgba(255, 159, 64, .7)',  # Arancione
    'rgba(255, 99, 71, .7)',   # Rosso pomodoro
    'rgba(60, 179, 113, .7)',  # Verde medio
    'rgba(129, 181, 9, .7)',  # Viola medio
    'rgba(161, 5, 116, .7)',   # Azzurro profondo
    'rgba(255, 140, 0, .7)',   # Arancione scuro
    'rgba(144, 238, 144, .7)'  # Verde chiaro
]
pulls = [0,0,0,0,0,0,0,0,0,0,0.1,0]
fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker_colors=colors,pull=pulls)])
fig.update_traces(textposition='inside')
fig.update_layout(
    paper_bgcolor = "#e3e7f0",
    uniformtext_minsize=12, 
    uniformtext_mode='hide'
)
fig.show()

#differenza vendite nei vari posti del mondo tra top pokemon e top gioco
migliore_mondo = vg[:1]
migliore_pokemon = pokemon[:1]

# +
primo = pd.DataFrame(
    [migliore_mondo['NA_Sales'], migliore_mondo['JP_Sales'], migliore_mondo['EU_Sales'], migliore_mondo['Global_Sales'], migliore_mondo['Other_Sales']],
)

primo_pokemon = pd.DataFrame(
    [migliore_pokemon['NA_Sales'], migliore_pokemon['JP_Sales'], migliore_pokemon['EU_Sales'], migliore_pokemon['Global_Sales'], migliore_pokemon['Other_Sales']],
)

comparazione = pd.DataFrame(
    {
        'Top videogame' : [x[0] for x in primo.values],
        'Pokémon' :[x[0] for x in primo_pokemon.values]
    },
    primo.index
)
comparazione
# -

comparazione.plot.barh(
    color=['lightblue', 'blue'],
    alpha=.6
)
plt.gcf().set_facecolor('#e3e7f0')
plt.yticks([0,1,2,3,4],['Nord America', 'Giappone', 'Europa', 'Mondo', 'Altri'])
plt.xlabel('Milioni di vendite')
plt.show()


