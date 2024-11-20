import csv

distances_file_path = "../data/distances.csv"
packages_file_path = "./data/packages.csv"


def load_data():
    with open(packages_file_path, mode='r') as file:
      csv_reader = csv.DictReader(file)
      for row in csv_reader:
        package_id = int(row['Package ID'])
        print(package_id)
     

load_data()