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
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('POKEMON/pokemon.csv')
df.head()

df['height_m']*100


def filtraNome (df,nome):
    return df[df['name']==nome]


df['defense']

Charmander = filtraNome(df,'Charmander')
Bulbasaur = filtraNome(df,'Bulbasaur')
Squirtle = filtraNome(df,'Squirtle') 
Pikachu = filtraNome(df,'Pikachu') 


# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Pikachu",
                r = [Pikachu["attack"].values[0],
                     Pikachu["defense"].values[0],
                     Pikachu["weight_kg"].values[0]*10,
                     Pikachu["height_m"].values[0]*100,
                     Pikachu["hp"].values[0],
                     Pikachu["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor = "rgba(237, 252, 23,.3)",
                line_color="rgba(237, 252, 23,.7)"
               ))
#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range=[0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

char = pd.Series([Charmander["attack"].values[0],
                     Charmander["defense"].values[0],
                     Charmander["weight_kg"].values[0]*10,
                     Charmander["height_m"].values[0]*100,
                     Charmander["hp"].values[0],
                     Charmander["attack"].values[0]])

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Charmander",
                r = char,
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(252, 94, 45,.3)", 
                line_color="rgba(252, 94, 45,.7)"
               ))

#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range=[0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

bulb = pd.Series([Bulbasaur["attack"].values[0],
                     Bulbasaur["defense"].values[0],
                     Bulbasaur["weight_kg"].values[0]*10,
                     Bulbasaur["height_m"].values[0]*100,
                     Bulbasaur["hp"].values[0],
                     Bulbasaur["attack"].values[0]])

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Bulbasaur",
                r = bulb,
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(76, 245, 54,.3)",
                line_color="rgba(76, 245, 54,.7)"
               ))

#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,       
        range=[0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Squirtle",
                r = [Squirtle["attack"].values[0],
                     Squirtle["defense"].values[0],
                     Squirtle["weight_kg"].values[0]*10,
                     Squirtle["height_m"].values[0]*100,
                     Squirtle["hp"].values[0],
                     Squirtle["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(62, 127, 247,.3)",
                line_color="rgba(62, 127, 247,.7)"
               ))

#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'polar'}]*2]*2)

fig.add_trace(go.Scatterpolar(name = "Charmander",
                r = [Charmander["attack"].values[0],
                     Charmander["defense"].values[0],
                     Charmander["weight_kg"].values[0]*10,
                     Charmander["height_m"].values[0]*100,
                     Charmander["hp"].values[0],
                     Charmander["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(252, 94, 45,.7)"
               ),1,1)

fig.add_trace(go.Scatterpolar(name = "Bulbasaur",
                r = [Bulbasaur["attack"].values[0],
                     Bulbasaur["defense"].values[0],
                     Bulbasaur["weight_kg"].values[0]*10,
                     Bulbasaur["height_m"].values[0]*100,
                     Bulbasaur["hp"].values[0],
                     Bulbasaur["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(76, 245, 54,.7)"
               ),1,2)

fig.add_trace(go.Scatterpolar(name = "Squirtle",
                r = [Squirtle["attack"].values[0],
                     Squirtle["defense"].values[0],
                     Squirtle["weight_kg"].values[0]*10,
                     Squirtle["height_m"].values[0]*100,
                     Squirtle["hp"].values[0],
                     Squirtle["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(62, 127, 247,.7)"
               ),2,1)

fig.add_trace(go.Scatterpolar(name = "Pikachu",
                r = [Pikachu["attack"].values[0],
                     Pikachu["defense"].values[0],
                     Pikachu["weight_kg"].values[0]*10,
                     Pikachu["height_m"].values[0]*100,
                     Pikachu["hp"].values[0],
                     Pikachu["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(237, 252, 23,.7)"
               ),2,2)
#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Charmander",
                r = [Charmander["attack"].values[0],
                     Charmander["defense"].values[0],
                     Charmander["weight_kg"].values[0]*10,
                     Charmander["height_m"].values[0]*100,
                     Charmander["hp"].values[0],
                     Charmander["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(252, 94, 45,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Bulbasaur",
                r = [Bulbasaur["attack"].values[0],
                     Bulbasaur["defense"].values[0],
                     Bulbasaur["weight_kg"].values[0]*10,
                     Bulbasaur["height_m"].values[0]*100,
                     Bulbasaur["hp"].values[0],
                     Bulbasaur["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(76, 245, 54,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Squirtle",
                r = [Squirtle["attack"].values[0],
                     Squirtle["defense"].values[0],
                     Squirtle["weight_kg"].values[0]*10,
                     Squirtle["height_m"].values[0]*100,
                     Squirtle["hp"].values[0],
                     Squirtle["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Pikachu",
                r = [Pikachu["attack"].values[0],
                     Pikachu["defense"].values[0],
                     Pikachu["weight_kg"].values[0]*10,
                     Pikachu["height_m"].values[0]*100,
                     Pikachu["hp"].values[0],
                     Pikachu["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(237, 252, 23,.7)"
               ))
#colore griglia #e3e7f0
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

Cyndaquil = filtraNome(df,'Cyndaquil')
Chikorita = filtraNome(df,'Chikorita')
Totodile = filtraNome(df,'Totodile') 

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Cyndaquil",
                r = [Cyndaquil["attack"].values[0],
                     Cyndaquil["defense"].values[0],
                     Cyndaquil["weight_kg"].values[0]*10,
                     Cyndaquil["height_m"].values[0]*100,
                     Cyndaquil["hp"].values[0],
                     Cyndaquil["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(252, 94, 45,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Chikorita",
                r = [Chikorita["attack"].values[0],
                     Chikorita["defense"].values[0],
                     Chikorita["weight_kg"].values[0]*10,
                     Chikorita["height_m"].values[0]*100,
                     Chikorita["hp"].values[0],
                     Chikorita["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(76, 245, 54,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Totodile",
                r = [Totodile["attack"].values[0],
                     Totodile["defense"].values[0],
                     Totodile["weight_kg"].values[0]*10,
                     Totodile["height_m"].values[0]*100,
                     Totodile["hp"].values[0],
                     Totodile["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Cyndaquil",
                r = [Cyndaquil["attack"].values[0],
                     Cyndaquil["defense"].values[0],
                     Cyndaquil["weight_kg"].values[0]*10,
                     Cyndaquil["height_m"].values[0]*100,
                     Cyndaquil["hp"].values[0],
                     Cyndaquil["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(252, 94, 45,.3)",
                line_color="rgba(252, 94, 45,.7)"
               ))
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)
fig.show()
fig = go.Figure()
fig.add_trace(go.Scatterpolar(name = "Chikorita",
                r = [Chikorita["attack"].values[0],
                     Chikorita["defense"].values[0],
                     Chikorita["weight_kg"].values[0]*10,
                     Chikorita["height_m"].values[0]*100,
                     Chikorita["hp"].values[0],
                     Chikorita["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(76, 245, 54,.3)",
                line_color="rgba(76, 245, 54,.7)"
               ))
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)
fig.show()
fig = go.Figure()
fig.add_trace(go.Scatterpolar(name = "Totodile",
                r = [Totodile["attack"].values[0],
                     Totodile["defense"].values[0],
                     Totodile["weight_kg"].values[0]*10,
                     Totodile["height_m"].values[0]*100,
                     Totodile["hp"].values[0],
                     Totodile["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(62, 127, 247,.3)",
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

Chimchar = filtraNome(df,'Chimchar')
Turtwig = filtraNome(df,'Turtwig')
Piplup = filtraNome(df,'Piplup') 

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Chimchar",
                r = [Chimchar["attack"].values[0],
                     Chimchar["defense"].values[0],
                     Chimchar["weight_kg"].values[0]*10,
                     Chimchar["height_m"].values[0]*100,
                     Chimchar["hp"].values[0],
                     Chimchar["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(252, 94, 45,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Turtwig",
                r = [Turtwig["attack"].values[0],
                     Turtwig["defense"].values[0],
                     Turtwig["weight_kg"].values[0]*10,
                     Turtwig["height_m"].values[0]*100,
                     Turtwig["hp"].values[0],
                     Turtwig["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(76, 245, 54,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Piplup",
                r = [Piplup["attack"].values[0],
                     Piplup["defense"].values[0],
                     Piplup["weight_kg"].values[0]*10,
                     Piplup["height_m"].values[0]*100,
                     Piplup["hp"].values[0],
                     Piplup["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Chimchar",
                r = [Chimchar["attack"].values[0],
                     Chimchar["defense"].values[0],
                     Chimchar["weight_kg"].values[0]*10,
                     Chimchar["height_m"].values[0]*100,
                     Chimchar["hp"].values[0],
                     Chimchar["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(252, 94, 45,.3)",
                line_color="rgba(252, 94, 45,.7)"
               ))
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatterpolar(name = "Turtwig",
                r = [Turtwig["attack"].values[0],
                     Turtwig["defense"].values[0],
                     Turtwig["weight_kg"].values[0]*10,
                     Turtwig["height_m"].values[0]*100,
                     Turtwig["hp"].values[0],
                     Turtwig["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(76, 245, 54,.3)",
                line_color="rgba(76, 245, 54,.7)"
               ))
fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatterpolar(name = "Piplup",
                r = [Piplup["attack"].values[0],
                     Piplup["defense"].values[0],
                     Piplup["weight_kg"].values[0]*10,
                     Piplup["height_m"].values[0]*100,
                     Piplup["hp"].values[0],
                     Piplup["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(62, 127, 247,.3)",
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

Tepig = filtraNome(df,'Tepig')
Snivy = filtraNome(df,'Snivy')
Oshawott = filtraNome(df,'Oshawott') 

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Tepig",
                r = [Tepig["attack"].values[0],
                     Tepig["defense"].values[0],
                     Tepig["weight_kg"].values[0]*10,
                     Tepig["height_m"].values[0]*100,
                     Tepig["hp"].values[0],
                     Tepig["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(252, 94, 45,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Snivy",
                r = [Snivy["attack"].values[0],
                     Snivy["defense"].values[0],
                     Snivy["weight_kg"].values[0]*10,
                     Snivy["height_m"].values[0]*100,
                     Snivy["hp"].values[0],
                     Snivy["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(76, 245, 54,.7)"
               ))

fig.add_trace(go.Scatterpolar(name = "Oshawott",
                r = [Oshawott["attack"].values[0],
                     Oshawott["defense"].values[0],
                     Oshawott["weight_kg"].values[0]*10,
                     Oshawott["height_m"].values[0]*100,
                     Oshawott["hp"].values[0],
                     Oshawott["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

# +
fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Tepig",
                r = [Tepig["attack"].values[0],
                     Tepig["defense"].values[0],
                     Tepig["weight_kg"].values[0]*10,
                     Tepig["height_m"].values[0]*100,
                     Tepig["hp"].values[0],
                     Tepig["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(252, 94, 45,.3)",
                line_color="rgba(252, 94, 45,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Snivy",
                r = [Snivy["attack"].values[0],
                     Snivy["defense"].values[0],
                     Snivy["weight_kg"].values[0]*10,
                     Snivy["height_m"].values[0]*100,
                     Snivy["hp"].values[0],
                     Snivy["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(76, 245, 54,.3)",
                line_color="rgba(76, 245, 54,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()

fig = go.Figure()

fig.add_trace(go.Scatterpolar(name = "Oshawott",
                r = [Oshawott["attack"].values[0],
                     Oshawott["defense"].values[0],
                     Oshawott["weight_kg"].values[0]*10,
                     Oshawott["height_m"].values[0]*100,
                     Oshawott["hp"].values[0],
                     Oshawott["attack"].values[0]],
                theta = ["Attack","Defense","Weight","Height","Health","Attack"],
                fill="toself",
                fillcolor="rgba(62, 127, 247,.3)",
                line_color="rgba(62, 127, 247,.7)"
               ))

fig.update_layout(
    #title = "Confronto pokemon",
    #font_size = 11,
    showlegend = True,
    polar = dict(
      bgcolor = "white",
      angularaxis = dict(
        linewidth = 2,
        showline=True,
        linecolor='lightgrey',  # Colore delle linee angolari
        gridcolor='lightgrey',    # Colore della griglia angolare
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = False,
        linewidth = 2,
        gridcolor = "lightgrey",
        gridwidth = 2,
        range = [0,110]
      )
    ),
    paper_bgcolor = "white"
)

fig.show()
# -

t1 = pd.read_csv('POKEMON/TrendGeneration/trend1gen.csv', index_col=0)
t1

plt.plot(t1['Bulbasaur'], color = '#7dfa89')
plt.plot(t1['Charmander'], color = 'red', alpha=.6)
plt.plot(t1['Squirtle'], color = '#4fdce0')
plt.plot(t1['Pikachu'], color = '#d6d30b', alpha=.5)
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.yticks(np.arange(0,121,20))
plt.xlabel('Anno')
plt.ylabel('Popolarità')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()

t2 = pd.read_csv('POKEMON/TrendGeneration/trend2gen.csv', index_col=0)
t4 = pd.read_csv('POKEMON/TrendGeneration/trend4gen.csv')
t5 = pd.read_csv('POKEMON/TrendGeneration/trend5gen.csv', index_col=0)

plt.plot(t2['Chikorita'], color = '#7dfa89')
plt.plot(t2['Cyndaquil'], color = 'red', alpha=.6)
plt.plot(t2['Totodile'], color = '#4fdce0')
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.yticks(np.arange(0,121,20))
plt.xlabel('Anno')
plt.ylabel('Popolarità')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()

plt.plot(t4['Turtwig'], color = '#7dfa89')
plt.plot(t4['Chimchar'], color = 'red', alpha=.6)
plt.plot(t4['Piplup'], color = '#4fdce0')
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.yticks(np.arange(0,121,20))
plt.xlabel('Anno')
plt.ylabel('Popolarità')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()

plt.plot(t5['Snivy'], color = '#7dfa89')
plt.plot(t5['Tepig'], color = 'red', alpha=.6)
plt.plot(t5['Oshawott'], color = '#4fdce0')
indici = [0,11,23,35,47,59,71,83,95,107,119]
valori = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
plt.xticks(indici,valori)
plt.yticks(np.arange(0,121,20))
plt.xlabel('Anno')
plt.ylabel('Popolarità')
plt.gcf().set_facecolor('#e3e7f0')
plt.show()


