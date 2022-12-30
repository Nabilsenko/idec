import pandas as pd
import math

# Chargement du jeu de données dans un dataframe
dataframe = pd.read_csv('donnees-defi-egc.csv')

# Remettre des valeurs des colonne ANNEETRAVAUXPRECONISESDIAG, ANNEEDEPLANTATION et ANNEEREALISATIONDIAGNOSTIC qui ont '?' à 0
dataframe['ANNEETRAVAUXPRECONISESDIAG'] = dataframe['ANNEETRAVAUXPRECONISESDIAG'].replace(
    '?', 0)
dataframe['ANNEEDEPLANTATION'] = dataframe['ANNEEDEPLANTATION'].replace('?', 0)
dataframe['ANNEEREALISATIONDIAGNOSTIC'] = dataframe['ANNEEREALISATIONDIAGNOSTIC'].replace(
    '?', 0)

# Conversion de ces colonnes en un entier
dataframe['ANNEETRAVAUXPRECONISESDIAG'] = dataframe['ANNEETRAVAUXPRECONISESDIAG'].astype(
    int)
dataframe['ANNEEDEPLANTATION'] = dataframe['ANNEEDEPLANTATION'].astype(int)
dataframe['ANNEEREALISATIONDIAGNOSTIC'] = dataframe['ANNEEREALISATIONDIAGNOSTIC'].astype(
    int)

# Calcul des cellulles ou y a pas 0
valid_years_1 = [
    year for year in dataframe['ANNEETRAVAUXPRECONISESDIAG'] if year != 0]
valid_years_2 = [year for year in dataframe['ANNEEDEPLANTATION'] if year != 0]
valid_years_3 = [
    year for year in dataframe['ANNEEREALISATIONDIAGNOSTIC'] if year != 0]

# Calcul des moyennes des années 
mean_year_1 = math.trunc(
    sum(dataframe['ANNEETRAVAUXPRECONISESDIAG']) / len(valid_years_1))
mean_year_2 = math.trunc(
    sum(dataframe['ANNEEDEPLANTATION']) / len(valid_years_2))
mean_year_3 = math.trunc(
    sum(dataframe['ANNEEREALISATIONDIAGNOSTIC']) / len(valid_years_3))

# Remplacement des valeurs 0 par la moyenne des années
dataframe['ANNEETRAVAUXPRECONISESDIAG'] = dataframe['ANNEETRAVAUXPRECONISESDIAG'].replace(
    0, mean_year_1)
dataframe['ANNEEDEPLANTATION'] = dataframe['ANNEEDEPLANTATION'].replace(
    0, mean_year_2)
dataframe['ANNEEREALISATIONDIAGNOSTIC'] = dataframe['ANNEEREALISATIONDIAGNOSTIC'].replace(
    0, mean_year_3)

# Sauvegarde dans un nouveau fichier CSV
dataframe.to_csv('donnees-defi-egc.csv', index=False)
# dataframe.to_csv('modified_dataset.csv', index=False)
