import pandas as pd

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

# Supression des colonnes
dataframe = dataframe.drop(columns=['CODE', 'CODE_PARENT', 'CODE_PARENT_DESC', 'SOUS_CATEGORIE'])

# Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
