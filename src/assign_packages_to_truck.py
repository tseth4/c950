from data_structures.hashmap import HashMap
from datetime import datetime, timedelta
import math


def handle_edge_cases(package):
    if package.notes.startswith("Can only be on truck"):
        # Extract the truck number by splitting the string
        truck_number = int(package.notes.split()[-1])
        # print(f"The package {package.id} can only be on truck {truck_number}")
        return ["TRUCK_ASSIGNMENT", truck_number]
    elif package.notes.startswith("Delayed on flight---will not arrive to depot until"):
        time_str = package.notes.split(
            "Delayed on flight---will not arrive to depot until")[-1].strip()
        delay_time = datetime.strptime(time_str, "%I:%M %p")
        # print(f"The package {package.id} will be delayed until {delay_time.strftime('%I:%M %p')}")
        return ["DELAYED ARRIVAL", delay_time.strftime('%I:%M %p')]
    elif package.notes.startswith("Must be delivered with"):
        # Extract the package IDs by splitting the string
        package_ids_str = package.notes.split(
            "Must be delivered with")[-1].strip()
        package_ids = [int(pkg_id.strip())
                       for pkg_id in package_ids_str.split(",")]
        # print(f"Package {package.id} must be delivered with: {package_ids}")
        return ["DELIVERED WITH", package_ids]
    # elif package.notes.startswith("Wrong address listed -- updated at"):
    #     parts = package.notes.split("updated at")[-1].strip()
    #     time_part, address_part = parts.split("to", 1)
    #     update_time = datetime.strptime(time_part.strip(), "%I:%M %p")
    #     updated_address = address_part.strip()
    #     # print(f"package {package.id}, Address update at {update_time.strftime('%I:%M %p')} to: {updated_address}")
    #     return ["ADDRESS DELAYED UPDATE", update_time.strftime('%I:%M %p'), updated_address]


def assign_packages_to_truck(trucks, packages, capacity=16):
    """
    Assign packages to trucks, handling edge cases like specific truck assignments,
    grouped deliveries, delayed arrivals, and address updates.

    :param trucks: List of Truck objects.
    :param packages: List of all packages to assign.
    :param capacity: Truck capacity (default 16).
    """
    truck_count = len(trucks)
    package_count = len(packages)
    truck_capacity = capacity
    # Each truck has multiple trips
    # [[HashMap, HashMap][HashMap, HashMap]]
    truck_trips = [[] for _ in range(truck_count)]

    # Calculate the number of trips needed per truck
    # packets per truck 40 / 2 = 20
    packets_per_truck = math.ceil(package_count / truck_count)
    # 20 / 16 = 2
    trips_per_truck = math.ceil(packets_per_truck / truck_capacity)

    # Initialize trips for each truck
    for i in range(truck_count):
        truck_trips[i] = [HashMap(truck_capacity)
                          for _ in range(trips_per_truck)]

    # Handle edge cases and distribute packages
    delayed_packages = []  # Packages delayed on arrival
    grouped_package_ids = []  # Packages grouped for delivery
    grouped_packages = []  # Store grouped package objects for processing
    noteless_packages = []  # Packages without notes

    for package in packages:
        edge_case = handle_edge_cases(package)
        if edge_case:
            # Handle "Can only be on truck X"
            if edge_case[0] == "TRUCK_ASSIGNMENT":
                # Assuming truck IDs are 1-indexed
                truck_index = edge_case[1] - 1
                for trip in truck_trips[truck_index]:
                    if trip.count < capacity:
                        trip.merge_add(package.get_address_index(), package)
                        break
                continue

            # Handle "Delayed on flight"
            elif edge_case[0] == "DELAYED ARRIVAL":
                delayed_packages.append(package)
                # for truck in truck_trips:
                #     # if the last trip is not full: merge add
                #     if truck[-1].count < capacity:
                #         truck[-1].merge_add(package.get_address_index(), package)
                #         break
                # continue

            # Handle "Must be delivered with"
            elif edge_case[0] == "DELIVERED WITH":
                grouped_ids = edge_case[1]
                grouped_ids.append(package.id)  # Add the current package ID
                exists = False
                # Check if package group already exists
                for group in grouped_package_ids:
                    if any(_id in group for _id in grouped_ids):
                        group.update(grouped_ids)  # Add all IDs to the group
                        exists = True
                        break
                if not exists:
                    grouped_package_ids.append(set(grouped_ids))
                continue

        else:
            # Add packages without notes to noteless list for general distribution
            noteless_packages.append(package)

    # Handle grouped packages
    for group in grouped_package_ids:
        group_packages = [pkg for pkg in packages if pkg.id in group]
        for truck_trip in truck_trips:
            for trip in truck_trip:
                if trip.count + len(group_packages) <= capacity:
                    for group_pkg in group_packages:
                        trip.merge_add(
                            group_pkg.get_address_index(), group_pkg)
                    break
            else:
                continue
            break

    # print("delayed_packages: ", delayed_packages)
    # Assign delayed packages in round-robin fashion across last trips of trucks
    truck_index = 0
    for package in delayed_packages:
        # Get the last trip for the current truck
        truck_trip = truck_trips[truck_index]
        last_trip = truck_trip[-1]
        if last_trip.count < capacity:
            last_trip.merge_add(package.get_address_index(), package)
            # If this trip wasn't in the truck_trip list, append it
            if truck_trip and last_trip not in truck_trip:
                truck_trip.append(last_trip)
        # Move to the next truck (round-robin)
        truck_index = (truck_index + 1) % len(truck_trips)

    # Add delayed packages to the last trip of each truck
    # for package in delayed_packages:
    #     for truck in truck_trips:
    #         last_trip = truck[-1]  # Get the last trip for this truck
    #         if last_trip.count < capacity:
    #             last_trip.merge_add(package.get_address_index(), package)
    #             break

    # Distribute noteless packages evenly across trucks and trips
    truck_index = 0  # Start with the first truck
    trip_index = 0   # Start with the first trip for each truck

    for package in noteless_packages:
        assigned = False  # Flag to track if the package has been assigned

        for _ in range(len(truck_trips) * len(truck_trips[0])):  # Ensure all trucks and trips are checked
            # Get the current truck's trips
            truck_trip = truck_trips[truck_index]

            # Get the current trip in the current truck
            current_trip = truck_trip[trip_index]

            # Check if the current trip has capacity
            if current_trip.count < capacity:
                current_trip.merge_add(package.get_address_index(), package)
                assigned = True
                break  # Exit once the package is assigned

            # Move to the next trip (round-robin)
            trip_index = (trip_index + 1) % len(truck_trip)

            # If we've cycled through all trips in the current truck, move to the next truck
            if trip_index == 0:
                truck_index = (truck_index + 1) % len(truck_trips)

        # If no trips have space, skip the package (optional logging for debugging)
        if not assigned:
            print(f"Unable to assign package {package.id}. All trips are full.")

        # Assign trips to trucks
        for i, truck in enumerate(trucks):
            truck.trips = truck_trips[i]


# def assign_packages_to_truck(trucks, packages, capacity=16):
#     """
#     Assign packages to trucks, handling edge cases like specific truck assignments,
#     grouped deliveries, delayed arrivals, and address updates.

#     :param trucks: List of Truck objects.
#     :param packages: List of all packages to assign.
#     :param capacity: Truck capacity (default 16).
#     """
#     truck_count = len
#     truck_count = len(trucks)
#     package_count = len(packages)
#     truck_capacity = capacity
#     truck_trips = [[]] * truck_count

#     # Calculate the number of trips needed per truck
#     packets_per_truck = package_count / len(truck_trips)
#     trips_per_truck = math.ceil(packets_per_truck / truck_capacity)
#     # Initialize trips for each truck
#     for i, _ in enumerate(truck_trips):
#         truck_trips[i] = [HashMap(truck_capacity)] * trips_per_truck

#     # Handle edge cases and distribute packages
#     delayed_packages = []
#     grouped_package_ids = []
#     grouped_packages = HashMap()
#     noteless_packages = []

#     for package in packages:
#         edge_case = handle_edge_cases(package)
#         if edge_case:
#             # Handle "Can only be on truck X"
#             if edge_case[0] == "TRUCK_ASSIGNMENT":
#                 # Assuming truck IDs are 1-indexed
#                 truck_number = edge_case[1] - 1
#                 for trip in truck_trips[truck_number]:
#                     if trip.count < capacity:
#                         trip.merge_add(package.get_address_index(), package)
#                         break
#                 continue

#             # Handle "Delayed on flight"
#             elif edge_case[0] == "DELAYED ARRIVAL":
#                 for truck in truck_trips:
#                     last_trip = truck[len(truck) - 1]
#                     if last_trip.count < capacity:
#                         last_trip.merge_add(
#                             package.get_address_index(), package)
#                         break
#                 continue
#                 # Handle "Must be delivered with"
#             elif edge_case[0] == "DELIVERED WITH":
#                 grouped_ids = edge_case[1]
#                 grouped_ids.append(package.id)
#                 exists = False
#                 for group in grouped_package_ids:
#                     for _id in grouped_ids:
#                         if group.index(_id):
#                             group.add(_id)
#                             exists = True
#                 if not exists:
#                     grouped_package_ids.push(set(grouped_ids))

#                 # grouped_packages.append([grouped_ids])

#             # Handle "Address delayed update"
#             # elif edge_case[0] == "ADDRESS DELAYED UPDATE":
#             #     truck_trips[0][0].merge_add(
#             #         package.get_address_index(), package)

#     #push the res t
