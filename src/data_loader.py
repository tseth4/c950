import csv
from src.package import Package
from data_structures.hashmap import HashMap
from data_structures.adjacency_matrix import AdjacencyMatrix

distances_file_path = "./data/distances.csv"
packages_file_path = "./data/packages.csv"

# import sys
# print(sys.path)

# #  "Package
# ID",Address,City ,State,Zip,"Delivery
# Deadline","Weight
# KILO",page 1 of 1PageSpecial Notes


def load_packages():
    packages = HashMap()
    with open(packages_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[0])
            package = Package.from_csv_row(row)
            packages.add(int(row[0]), package)
        return packages


def load_distances():
    distances = AdjacencyMatrix(27)
    with open(distances_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    # Extract address names (header row)
    # rows[0] first row
    # rows[1:] slive all starting at 1
    addresses = rows[0][1:]
    # print("addresses: ")
    # for i, el in enumerate(addresses):
    #   print(i, el)
    #   print("    ")
    # Build Matrix
    distance_matrix = AdjacencyMatrix(len(addresses))
    print(distance_matrix)
    # print(addresses)

    # Build adjacency matrix
    for i, row in enumerate(rows[1:]):
        row_distances = row[1:]
        print("row: ", i)
        for j, dist in enumerate(row_distances):
            print("column: ", j, " dist: ", dist)
            if (is_number(dist)):
              print("setting distance.", " i: ", i, " j: ", j, " dist: ", dist)
              distance_matrix.set_distance(i, j, dist)

    print(distance_matrix)
    # Build adjacency matrix
    # matrix = []
    # for row in rows[1:]:
    #     distances = list(map(int, row[1:]))
    #     matrix.append(distances)

    return addresses, distance_matrix
    # with open(distances_file_path, mode='r', encoding='utf-8-sig') as file:
    #   csv_reader = csv.reader(file)
    #   for row in csv_reader:
    #     print(row)
    

def is_number(value):
    try:
        float(value)  # Attempt to convert the string to a float
        return True
    except ValueError:
        return False