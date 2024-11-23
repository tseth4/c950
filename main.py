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


def handle_edge_cases(package):
    if package.notes.startswith("Can only be on truck"):
        # Extract the truck number by splitting the string
        truck_number = int(package.notes.split()[-1])
        print(f"The package {package.id} can only be on truck {truck_number}")
        # return ["TRUCK_ASSIGNMENT", truck_number]
    elif package.notes.startswith("Delayed on flight---will not arrive to depot until"):
        time_str = package.notes.split(
            "Delayed on flight---will not arrive to depot until")[-1].strip()
        delay_time = datetime.strptime(time_str, "%I:%M %p")
        print(f"The package {package.id} will be delayed until {delay_time.strftime('%I:%M %p')}")
    elif package.notes.startswith("Must be delivered with"):
        # Extract the package IDs by splitting the string
        package_ids_str = package.notes.split(
            "Must be delivered with")[-1].strip()
        package_ids = [int(pkg_id.strip())
                       for pkg_id in package_ids_str.split(",")]
        print(f"Package {package.id} must be delivered with: {package_ids}")
    elif package.notes.startswith("Wrong address listed -- updated at"):
        parts = package.notes.split("updated at")[-1].strip()
        time_part, address_part = parts.split("to", 1)
        update_time = datetime.strptime(time_part.strip(), "%I:%M %p")
        updated_address = address_part.strip()
        print(f"package {package.id}, Address update at {update_time.strftime(
            '%I:%M %p')} to: {updated_address}")


# packages as HashMap
packages = load_packages()
# packages.print()

# distances as AdjacencyMatrix
addresses, distances = load_distances()

# Set package address_index's
for p in packages.values():
    handle_edge_cases(p)
    p.set_address_index(addresses.index(p.get_address()))

# Truck classes
truck1 = Truck(id=1, addresses=addresses, capacity=16)
truck2 = Truck(id=2, addresses=addresses, capacity=16)

# Truck array
trucks = [truck1, truck2]

# Sort all packages by deadline
sorted_packages = packages.sort_packages_by_deadline_and_proximity(
    distances.matrix, addresses)

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
