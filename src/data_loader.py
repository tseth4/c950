import csv
from src.package import Package
from data_structures.hashmap import HashMap
from data_structures.adjacency_matrix import AdjacencyMatrix

distances_file_path = "./data/distances.csv"
packages_file_path = "./data/packages.csv"



def load_packages():
    packages = HashMap()
    with open(packages_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # print(row)
            package = Package.from_csv_row(row)
            packages.add(int(row[0]), package)
        return packages


def load_distances():
    with open(distances_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    addresses = rows[0][1:]
    # Build Matrix
    distance_matrix = AdjacencyMatrix(len(addresses))
    # print(distance_matrix)

    # Build adjacency matrix
    for i, row in enumerate(rows[1:]):
        row_distances = row[1:]
        for j, dist in enumerate(row_distances):
            if (is_number(dist)):
              distance_matrix.set_distance(i, j, dist)

    return addresses, distance_matrix

    

def is_number(value):
    try:
        float(value)  # Attempt to convert the string to a float
        return True
    except ValueError:
        return False