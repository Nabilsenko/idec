import pandas as pd
import pyproj

# Charger les données depuis le fichier CSV dans un DataFrame
df = pd.read_csv("donnees-defi-egc.csv")

# Définir le CRS source (RGF93)
src_crs = pyproj.CRS.from_epsg(3945)

# Définir le CRS cible (WGS 84)
dst_crs = pyproj.CRS.from_epsg(4326)

# Créer l'objet de transformation
transformer = pyproj.Transformer.from_crs(src_crs, dst_crs, always_xy=True)

# Convertir les coordonnées et les ajouter au DataFrame
df["longitude"], df["latitude"] = transformer.transform(df["coord_x"], df["coord_y"])

# Enregistrer le résultat dans un fichier CSV
df.to_csv("result.csv", index=False)

