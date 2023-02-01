import pandas as pd

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

dataframe['ESPECE'].replace('?', 'inconnu', inplace=True)
dataframe['FREQUENTATIONCIBLE'].replace('?', 'inconnu', inplace=True)
dataframe['GENRE_BOTA'].replace('?', 'inconnu', inplace=True)
dataframe['NOTEDIAGNOSTIC'].replace('?', 'inconnu', inplace=True)
dataframe['TRAVAUXPRECONISESDIAG'].replace('?', 'inconnu', inplace=True)
dataframe['STADEDEVELOPPEMENTDIAG'].replace('?', 'inconnu', inplace=True)
dataframe['STADEDEDEVELOPPEMENT'].replace('?', 'inconnu', inplace=True)
dataframe['SOUS_CATEGORIE_DESC'].replace('?', 'inconnu', inplace=True)
dataframe['VIGUEUR'].replace('?', 'inconnu', inplace=True)
dataframe['ADR_SECTEUR'].replace('?', 'inconnu', inplace=True)
dataframe['VARIETE'].replace('?', 'inconnu', inplace=True)

# Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
