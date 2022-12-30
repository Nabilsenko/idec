import pandas as pd

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

# Remplacement des valeurs 1 par "oui" et 0 par "non"
dataframe['DEFAUT'] = dataframe['DEFAUT'].replace(1, 'oui').replace(0, 'non')
dataframe['Collet'] = dataframe['Collet'].replace(1, 'oui').replace(0, 'non')
dataframe['Houppier'] = dataframe['Houppier'].replace(1, 'oui').replace(0, 'non')
dataframe['Racine'] = dataframe['Racine'].replace(1, 'oui').replace(0, 'non')
dataframe['Tronc'] = dataframe['Tronc'].replace(1, 'oui').replace(0, 'non')

# Concatenation de region avec le numero de la region
dataframe['ADR_SECTEUR'] = dataframe['ADR_SECTEUR'].apply(lambda x: "region{}".format(x))


# Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
