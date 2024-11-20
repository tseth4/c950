from src.data_loader import load_packages, load_distances
from src.truck import Truck
from src.package import Package
from data_structures.nearest_neighbor import nearest_neighbor

"""
Deliver 40 packages using 3 trucks under 140 miles total.

Meet package-specific constraints (deadlines, delivery address corrections).

Output delivery progress for packages (time delivered, status, etc.).

Write clean, modular, and maintainable code.
"""

# packages as HashMap
packages = load_packages()

# distances as AdjacencyMatrix
addresses, distances = load_distances()

# print("addressses: ", addresses)
for i, ad in enumerate(addresses):
  print(i)
  print(ad)
  print("  ")
# print("     ")
# print("distances: ", distances)
# print("     ")

# International Peace Gardens
#  1060 Dalton Ave S


# Truck class
truck1 = Truck(id=1, capacity=16)
truck2 = Truck(id=2, capacity=16)


# Assign packages to trucks based on capacity
print("PACK ADD    ")

print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
for key in packages.keys():
    package = packages.get(key)
    print(addresses.index(package.get_address()))
    print("      ")
    # if not truck1.assign_package(package):  # Try to assign to Truck 1
    #     truck2.assign_package(package)      # If Truck 1 is full, assign to Truck 2

# print(truck1)

# 1060 Dalton Ave S

# 3575 W Valley Central Station bus Loop