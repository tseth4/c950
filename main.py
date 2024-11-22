from src.data_loader import load_packages, load_distances
from src.truck import Truck
from src.package import Package
from data_structures.nearest_neighbor import nearest_neighbor
from src.process_deliveries import process_deliveries
from datetime import datetime, timedelta

# TODO:Work on edge cases
# "Can only be on truck <x>"
# "Delayed on flight---will not arrive to depot until <9:05 am>"
# 


"""
Deliver 40 packages using 3 trucks under 140 miles total.
Meet package-specific constraints (deadlines, delivery address corrections).
Output delivery progress for packages (time delivered, status, etc.).
Write clean, modular, and maintainable code.
"""

# packages as HashMap
packages = load_packages()
# packages.print()

# distances as AdjacencyMatrix
addresses, distances = load_distances()

for p in packages.values():
    p.set_address_index(addresses.index(p.get_address()))

# Truck class
truck1 = Truck(id=1, addresses=addresses, capacity=16)
truck2 = Truck(id=2, addresses=addresses, capacity=16)

trucks = [truck1, truck2]
sorted_packages = packages.get_sorted_packages_by_deadline()

for i, package in enumerate(sorted_packages):
    trucks[i % len(trucks)].assign_package(package)


for truck in trucks:
  truck.process_deliveries(distances.matrix, datetime.strptime("9:00:00", "%H:%M:%S"))


for package in packages.values():
    print(package)
