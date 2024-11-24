# C950 WGUPS ROUTING
# By: Tristan Setha
# Student ID: 012068201


from src.data_loader import load_packages, load_distances
from src.truck import Truck
from src.package import Package
from data_structures.hashmap import HashMap
from src.process_deliveries import process_deliveries
from datetime import datetime, timedelta
from src.assign_packages_to_truck import assign_packages_to_truck

# from src.lookup_package import lookup_package

# TODO:Work on edge cases
# Can only be on truck 2: Can use a method during package assignment
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
truck1 = Truck(id=1, capacity=16, address_mapping=addresses)
truck2 = Truck(id=2, capacity=16, address_mapping=addresses)

# Truck array
trucks = [truck1, truck2]

# Sort all packages by deadline
sorted_packages = packages.get_sorted_packages_by_deadline()

# Assign packages to trucks
assign_packages_to_truck(trucks, sorted_packages)

# Optimize routes for each truck
for truck in trucks:
    truck.optimize_route(distances.matrix)


# for truck in trucks:
#     print(f"truck {truck.id} route: ", truck.route)
#     truck.trips = [trip for trip in truck.trips if trip.count > 0]
# # Process deliveries for each truck
for truck in trucks:
    truck.process_deliveries(distances.matrix)


# Print delivery data
for package in packages.values():
    print(package)
