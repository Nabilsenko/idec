import csv
import pyproj

def convert_to_lat_lon(x, y):
    inProj = pyproj.Proj(proj='utm', zone=33, northern=True, ellps='WGS84')
    outProj = pyproj.Proj(proj='latlong', datum='WGS84')
    return lat, lon

input_file = "donnees-defi-egc.csv"
output_file = "output.csv"

with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.DictReader(input_csv)
    fieldnames = reader.fieldnames
    fieldnames += ['latitude', 'longitude']
    writer = csv.DictWriter(output_csv, fieldnames)
    writer.writeheader()
    for row in reader:
        coord_x = float(row['coord_x'])
        coord_y = float(row['coord_y'])
        lat, lon = convert_to_lat_lon(coord_x, coord_y)
        row['latitude'] = lat
        row['longitude'] = lon
        writer.writerow(row)
