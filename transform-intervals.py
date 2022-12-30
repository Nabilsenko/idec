import pandas as pd
import math

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

means = []

# Parcourir la colonne DIAMETREARBREAUNMETRE
for x in dataframe['DIAMETREARBREAUNMETRE']:
    # Séparation des valeurs entières à l'aide de l'espace et du caractère "à"
    values = x.split(" à ")
    # Conversion de chaque valeur en entier et suppression de la chaîne " cm"
    for i in range(len(values)):
        try:
            values[i] = int(values[i].strip(" cm"))
        except:
            values [i] = 0
            
    # Calcul de la moyenne des valeurs
    mean = math.trunc(sum(values) / len(values))
    # Ajout de la moyenne à la liste
    means.append(mean)

# Mettre à jour notre colonne
dataframe['DIAMETREARBREAUNMETRE'] = means

# # Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
