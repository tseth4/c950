from src.data_loader import load_packages, load_distances
from src.truck import Truck
from src.package import Package
from data_structures.nearest_neighbor import nearest_neighbor
from src.process_deliveries import process_deliveries
from datetime import datetime, timedelta


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
# print(distances)

# populate package.address_index
# print("PRINTING: ")

for p in packages.values():
    p.set_address_index(addresses.index(p.get_address()))

# print("END PRINTING")


# Truck class
truck1 = Truck(id=1, addresses=addresses, capacity=16)
truck2 = Truck(id=2, addresses=addresses, capacity=16)

trucks = [truck1, truck2]
sorted_packages = packages.get_sorted_packages_by_deadline()
for i, package in enumerate(sorted_packages):
    trucks[i % len(trucks)].assign_package(package)


# assign_packages_to_trucks(packages, [truck1, truck2], distances, addresses)

# Optimize routes
# print(distances.matrix)
truck1.optimize_route(distances.matrix)
truck2.optimize_route(distances.matrix)

process_deliveries(truck1, distances.matrix, datetime.strptime("9:00:00", "%H:%M:%S"))
process_deliveries(truck2, distances.matrix, datetime.strptime("9:00:00", "%H:%M:%S"))

# for p in truck1.packages:
#     print(p.id)
# Print package details
for package in packages.values():
    print(package)
