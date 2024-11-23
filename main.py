# C950 WGUPS ROUTING
# By: Tristan Setha
# Student ID: 012068201


from src.data_loader import load_packages, load_distances
from src.truck import Truck
from src.package import Package
from data_structures.nearest_neighbor import nearest_neighbor
from src.process_deliveries import process_deliveries
from datetime import datetime, timedelta
# from src.lookup_package import lookup_package

# TODO:Work on edge cases
# Can only be on truck <x>: Can use a method during package assignment
# Delayed on flight---will not arrive to depot until <9:05 am>: Will have to be loaded onto truck during second trip. If delayed
# Package 9 Wrong address listed --: Check current_time and update package 9
# Must be delivered with n, n: Still unsure what this means

# TODO:
# D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
# 1.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
# 2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
# 3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.
# E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.


# packages as HashMap
packages = load_packages()
# packages.print()

# distances as AdjacencyMatrix
addresses, distances = load_distances()

# Set package address_index's
for p in packages.values():
    p.set_address_index(addresses.index(p.get_address()))

# Truck classes
truck1 = Truck(id=1, addresses=addresses, capacity=16)
truck2 = Truck(id=2, addresses=addresses, capacity=16)

# Truck array
trucks = [truck1, truck2]

# Sort all packages by deadline
sorted_packages = packages.sort_packages_by_deadline_and_proximity(distances.matrix, addresses)

# Assign packages to each truck
for i, package in enumerate(sorted_packages):
    trucks[i % len(trucks)].assign_package(package)


# Start delivery process
for truck in trucks:
  truck.process_deliveries(distances.matrix
                          #  , datetime.strptime("9:00:00", "%H:%M:%S")
                           )
  
print("Truck 1 total distance: ", truck1.total_distance)
print("Truck 2 total distance: ", truck2.total_distance)


# Print delivery data
# for package in packages.values():
#     print(package)
