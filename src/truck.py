from src.package_status import PackageStatus
from data_structures.hashmap import HashMap
from datetime import datetime, timedelta


class Truck:
    def __init__(self, id, addresses, capacity, start_time="08:00:00"):
        self.id = id
        self.capacity = capacity
        self.current_location_index = 0  # Starting location (e.g., hub)
        self.route = []  # List of addresses/nodes to visit
        self.assigned_packages = []  # List of Package objects
        self.current_trip = HashMap(initial_size=capacity)
        self.total_distance = 0  # Total distance traveled
        self.address_mapping = addresses
        self.current_time = datetime.strptime(start_time, "%H:%M:%S")
        self.speed = 18

    def get_current_trip(self):
        return self.current_trip

    # def set_current_trip(self, trip):
    #     self.current_trip = trip

    def get_current_location_index(self):
        return self.current_location_index

    def set_current_location_index(self, index):
        self.current_location_index = index

    def get_speed(self):
        return self.speed

    def set_current_time(self, time):
        self.current_time = time

    def get_current_time(self):
        return self.current_time

    def assign_package(self, package):
        """Assign a package to the truck."""
        self.assigned_packages.append(package)

    def get_capacity(self):
        return self.capacity

    def set_route(self, route):
        """Set the truck's delivery route."""
        self.route = route

    def deliver_package(self, address):
        """Simulate delivering a package."""
        self.assigned_packages = [
            pkg for pkg in self.assigned_packages if pkg.address != address]

    def update_location(self, new_location, distance):
        """Move the truck to a new location and update distance."""
        self.current_location_index = new_location
        self.total_distance += distance

    def reset(self):
        """Reset the truck for a new simulation."""
        self.current_location = None
        self.route = []
        self.assigned_packages = []
        self.total_distance = 0

    def __str__(self):
        """Return a human-readable string representation of the truck."""
        package_ids = [pkg.id for pkg in self.assigned_packages]
        route_str = " -> ".join(self.route) if self.route else "No route assigned"
        return (
            f"Truck ID: {self.id}\n"
            f"Capacity: {self.capacity}\n"
            f"Current Location: {
                self.address_mapping[self.current_location_index]}\n"
            f"Total Distance Traveled: {self.total_distance} miles\n"
            f"Route: {route_str}\n"
            f"Assigned Packages: {package_ids}"
        )

    def nearest_neighbor_with_packages(self, matrix, packages, hub_index=0, ):

        if not packages:
            print(f"Truck {self.id} has no packages to deliver.")
            return

        # Initialize variables
        current_index = hub_index
        visited = set()
        route = [hub_index]
        total_distance = 0

        # Create a set of package indices to visit
        package_indices = {package.get_address_index() for package in packages}

        # Visit all package indices
        while package_indices:
            nearest_distance = float('inf')
            nearest_index = None

            # Find the nearest unvisited package address
            for address_index in package_indices:
                current_distance = float(matrix[current_index][address_index])
                if current_distance < nearest_distance:
                    nearest_distance = current_distance
                    nearest_index = address_index

            if nearest_index is not None:
                # Move to the nearest location
                route.append(nearest_index)
                total_distance += nearest_distance
                visited.add(nearest_index)
                current_index = nearest_index

                # Remove from package_indices as it's now visited
                package_indices.remove(nearest_index)

        # Return to the hub
        distance_to_hub = float(matrix[current_index][hub_index])
        total_distance += distance_to_hub
        route.append(hub_index)

        # Update the truck's route and total distance
        self.route = route
        self.total_distance = total_distance

    def optimize_route(self, matrix):

        if not self.current_trip or self.current_trip.count == 0:
            print(
                f"Truck {self.id} has no packages to deliver in the current trip.")
            return

        # Extract all packages from the HashMap
        packages = []
        for package_list in self.current_trip.values():
            packages.extend(package_list)
        print("optimizing: ", len(packages))
        # Pass the extracted packages to nearest_neighbor_with_packages
        self.nearest_neighbor_with_packages(matrix, packages=packages)

    def process_deliveries(self, adjacency_matrix, cutoff_time=None):

        if not self.assigned_packages:
            print(f"Truck {self.id} has no packages to deliver.")
            return

        # Default cutoff time to EOD (5:00 PM)
        if cutoff_time is None:
            cutoff_time = datetime.strptime("17:00:00", "%H:%M:%S")

        # Track undelivered packages in this truck's assigned set
        undelivered_packages = [
            pkg for pkg in self.assigned_packages if pkg.status == PackageStatus.AT_HUB]

        while undelivered_packages:
            # Load the truck with up to its capacity
            self.current_trip = HashMap(
                initial_size=self.capacity)  # Reset current trip
            for _ in range(self.capacity):
                if undelivered_packages:
                    package = undelivered_packages.pop(0)
                    package.set_status(PackageStatus.EN_ROUTE)
                    address_index = package.get_address_index()

                    # Add to current_trip using merge_add
                    self.current_trip.merge_add(address_index, package)


            # Optimize the route for the current trip
            self.optimize_route(adjacency_matrix)

            print(f"Truck-{self.id} is starting a trip with {self.current_trip.count} packages.")

            # Start delivery simulation for this trip
            current_time = self.get_current_time()
            speed_mph = self.get_speed()

            for i in range(1, len(self.route)):  # Skip hub (index 0)
                prev_index = self.get_current_location_index()
                current_index = self.route[i]
                self.current_location_index = current_index

                # Calculate travel time
                distance = float(adjacency_matrix[prev_index][current_index])
                travel_time = (distance / speed_mph) * \
                    60  # Convert hours to minutes
                current_time += timedelta(minutes=travel_time)

                # Check if cutoff time is exceeded
                if current_time > cutoff_time:
                    print(
                        f"Truck-{self.id} reached the cutoff time. Returning to hub.")
                    return

                self.current_time = current_time

                # Deliver packages at the current location
                packages_at_address = self.current_trip.get(current_index)
                if packages_at_address:
                    for package in packages_at_address:
                        package.mark_delivered(
                            self.id, current_time.strftime("%H:%M:%S"))
                    # Remove the delivered packages from current_trip
                    self.current_trip.delete(current_index)

            # Return to the hub
            # distance_to_hub = float(adjacency_matrix[self.get_current_location_index()][0])
            # travel_time_to_hub = (distance_to_hub / speed_mph) * 60
            # current_time += timedelta(minutes=travel_time_to_hub)
            # self.current_time = current_time
            # self.current_location_index = 0

            print(
                f"Truck-{self.id} returned to the hub at {self.current_time.strftime('%H:%M:%S')}.")

            # Update undelivered packages (filter remaining at hub)
            undelivered_packages = [
                pkg for pkg in self.assigned_packages if pkg.status == PackageStatus.AT_HUB]
