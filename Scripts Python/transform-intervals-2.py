import pandas as pd
import math

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

result = []

def plus(x):
    try:
        number = x.strip("plus de ").strip(" ans")
        return " " + number + "-" + "50"
    except:
        print("error")
        
def moins(x):
    try:
        number = x.strip("moins de ").strip(" ans")
        return " " + 1 + "-" + number
    except:
        print("error")
        
def de(x):
    values = x.split(" ")
    try:
        print(values[1] + "-" + values[3])
        return " " + values[1] + "-" + values[3]
    except:
        print("error")
        
        
# Parcourir la colonne PRIORITEDERENOUVELLEMENT
for x in dataframe['PRIORITEDERENOUVELLEMENT']:
    if("plus de" in x):
        result.append(plus(x))
    elif("moins de" in x):
        result.append(moins(x))
    elif("de " in x):
        result.append(de(x))
    else:
        result.append(" " + "0-1")
    

# # Mettre à jour notre colonne
dataframe['PRIORITEDERENOUVELLEMENT'] = result

# # Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
