
from src.data_loader import load_packages, load_distances
from src.package_status import PackageStatus
from datetime import datetime
from src.assign_packages_to_truck import assign_packages_to_truck
from src.truck import Truck


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


for truck in trucks:
    truck.process_deliveries(
        distances.matrix
    )


def reset_simulation(trucks, packages):
    """
    Reset the state of all trucks and packages to their initial conditions.
    """
    # Reset all packages
    for package in packages.values():
        package.status = PackageStatus.AT_HUB
        package.delivery_time = None

    # Reset all trucks
    for truck in trucks:
        truck.trips = []  # Clear trips
        truck.route = []  # Clear route
        truck.current_trip = None  # Reset current trip
        truck.total_distance = 0  # Reset distance
        truck.current_time = datetime.strptime(
            "08:00:00", "%H:%M:%S")  # Reset time


def print_main_menu():
    """Print the main menu options."""
    print("\n--- WGUPS Routing Program ---")
    print("1. View delivery status of all packages")
    print("2. Look up a package by ID")
    print("3. View delivery statuses at a specific time")
    print("4. View total mileage traveled by all trucks")
    print("5. Exit")


def get_package_status_at_time(packages, target_time):
    """
    Get the status of all packages at a specific time.
    :param packages: HashMap of packages.
    :param target_time: Time to check statuses.
    """
    target_time = datetime.strptime(target_time, "%H:%M:%S")
    print(f"\nPackage statuses at {target_time.strftime('%I:%M:%S %p')}:")
    # Were pretty much filtering through all dlivered packages?
    for truck in trucks:
        truck.process_deliveries(
            distances.matrix,
            cutoff_time=target_time
        )
    for package in packages.values():
        print(package)


def main():
    """Main function to run the CLI."""
    while True:
        print_main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n--- All Packages ---")
            # Reset state before reprocessing
            reset_simulation(trucks, packages)
            assign_packages_to_truck(
                trucks, sorted_packages)  # Reassign packages
            for truck in trucks:
                truck.optimize_route(distances.matrix)  # Optimize routes
                truck.process_deliveries(
                    distances.matrix)  # Process deliveries
            for package in packages.values():
                print(package)

        elif choice == "2":
            package_id = int(input("\nEnter package ID to look up: "))
            # Reset state before reprocessing
            reset_simulation(trucks, packages)
            assign_packages_to_truck(
                trucks, sorted_packages)  # Reassign packages
            for truck in trucks:
                truck.optimize_route(distances.matrix)  # Optimize routes
                truck.process_deliveries(
                    distances.matrix)  # Process deliveries
            package = packages.get(package_id)
            if package:
                print(package)
            else:
                print(f"Package {package_id} not found.")

        elif choice == "3":
            target_time_input = input(
                "\nEnter time to check statuses (HH:MM:SS): ")
            target_time = datetime.strptime(target_time_input, "%H:%M:%S")

            reset_simulation(trucks, packages)  # Reset state before simulating
            assign_packages_to_truck(
                trucks, sorted_packages)  # Reassign packages
            for truck in trucks:
                truck.optimize_route(distances.matrix)  # Optimize routes
                truck.process_deliveries(
                    distances.matrix, cutoff_time=target_time)

            for truck in trucks:
                truck.process_deliveries(
                    distances.matrix,
                    cutoff_time=target_time
                )
            for package in packages.values():
                print(package)
            # get_package_status_at_time(packages, target_time)

        elif choice == "4":
            # Reset state before reprocessing
            reset_simulation(trucks, packages)
            assign_packages_to_truck(
                trucks, sorted_packages)  # Reassign packages
            for truck in trucks:
                truck.optimize_route(distances.matrix)  # Optimize routes
                truck.process_deliveries(
                    distances.matrix)  # Process deliveries
                print(f"Total distance of Truck {truck.id}: {
                      round(truck.total_distance, 1)} miles")
            total_mileage = sum(truck.total_distance for truck in trucks)
            print(f"\nTotal mileage traveled by all trucks: {
                  total_mileage:.2f} miles")

        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
