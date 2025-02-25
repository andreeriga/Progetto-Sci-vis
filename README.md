# Progetto Visualizzazione Scientifica

Progetto di visualizzazione scientifica svolto da: 

 - Rigamonti Eleonora : 989483 - eleonora.rigamonti@studenti.unimi.it
 - Rigamonti Andrea : 984745 - andrea.rigamonti11@studenti.unimi.it

Il progetto da noi svolto tratta il tema dei Pokémon, andando verso una tematica più generale, ovvero i videogames, confrontando questi ultimi 
sia con la Nintendo(azienda di videogiochi famosa anche per aver prodotto i giochi Pokémon) che con i giochi Pokémon
> [!NOTE]
> - Il file PowerPoint si trova all'interno della cartella <a href="https://github.com/AndreaRigamontiUnimi/Progetto-Sci-vis/tree/main/PRESENTAZIONE"> PRESENTAZIONE </a>
> - I file relativi ai Dataset si trovano nelle cartelle <a href="https://github.com/AndreaRigamontiUnimi/Progetto-Sci-vis/tree/main/POKEMON">POKEMON</a> e <a href='https://github.com/AndreaRigamontiUnimi/Progetto-Sci-vis/tree/main/VIDEOGAMES'>VIDEOGAMES</a>
## Guida rapida all'uso di virtual environment

I Virtual Environment (venv) permettono di creare ambienti isolati per i progetti Python, evitando conflitti tra librerie.

### Creazione di un Virtual Environment

1. **Creare un nuovo ambiente:**
   ```bash
   python -m venv nome_ambiente
   ```

2. **Attivare l'ambiente:**
   - Su **Windows**:
     ```bash
     nome_ambiente\Scripts\activate
     ```
   - Su **Mac/Linux**:
     ```bash
     source nome_ambiente/bin/activate
     ```

### Installare pacchetti

Con l'ambiente attivo, installa pacchetti con:
```bash
pip install nome_pacchetto
```
Per salvare le dipendenze:
```bash
pip freeze > requirements.txt
```

### Disattivare il Virtual Environment

Per uscire dall'ambiente virtuale, esegui:
```bash
deactivate
```

### Eliminare un Virtual Environment

Basta rimuovere la cartella `nome_ambiente` con:
```bash
rm -rf nome_ambiente  # Mac/Linux
rd /s /q nome_ambiente  # Windows
```

Per maggiori dettagli, consulta la [documentazione ufficiale](https://docs.python.org/3/library/venv.html).

## Guida rapida a Jupytext

[Jupytext](https://github.com/mwouts/jupytext) permette di salvare i notebook Jupyter in formati leggibili come Markdown o Python script. È utile per il versionamento con Git e la collaborazione.

### Installazione

Installa Jupytext con:
```bash
pip install jupytext
```

### Configurazione

Per salvare automaticamente i notebook in un formato testuale, esegui:
```bash
jupytext --set-formats ipynb,py
```

### Utilizzo

- **Convertire un notebook in Python:**
  ```bash
  jupytext --to py notebook.ipynb
  ```
- **Convertire uno script Python in notebook:**
  ```bash
  jupytext --to ipynb script.py
  ```
- **Sincronizzare notebook e script:**
  ```bash
  jupytext --sync notebook.ipynb
  ```

Ora puoi aprire i file `.py` o `.md` direttamente in Jupyter Notebook.

Per maggiori dettagli, consulta la [documentazione ufficiale](https://jupytext.readthedocs.io/).

