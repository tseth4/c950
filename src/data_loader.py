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

    temp_addresses = rows[0][1:]
    addresses = []
    for addr in temp_addresses:
        addresses.append(extract_address(addr))

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


def extract_address(full_text):
    """
    Extract the address from a full string, ignoring the first line.

    :param full_text: A multi-line string with a location name and address.
    :return: The address portion of the string.
    """
    lines = full_text.splitlines()  # Split the input into

    # print("lines: ", lines)
    return_string = " ".join(lines[1:]).strip()
    return return_string
    # if len(lines) > 1:
    #     return " ".join(lines[1:]).strip()  # Join lines after the first one
    # return full_text.strip()  # Return as is if only one line
