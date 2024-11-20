import csv
from src.package import Package
from data_structures.hashmap import HashMap

distances_file_path = "../data/distances.csv"
packages_file_path = "./data/packages.csv"

# import sys
# print(sys.path)

# #  "Package
# ID",Address,City ,State,Zip,"Delivery
# Deadline","Weight
# KILO",page 1 of 1PageSpecial Notes

def load_data():
    packages = HashMap(40)
    with open(packages_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[0])
            package = Package.from_csv_row(row)
            packages.add(int(row[0]), package)
        return packages
