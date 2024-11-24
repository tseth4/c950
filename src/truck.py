from src.package_status import PackageStatus
from data_structures.hashmap import HashMap
from datetime import datetime, timedelta


class Truck:
    def __init__(self, id, capacity, speed=18, start_time="08:00:00"):
        self.id = id
        self.capacity = capacity
        self.speed = speed
        self.start_time = datetime.strptime(start_time, "%H:%M:%S")
        self.current_time = self.start_time
        self.current_location_index = 0  # Starting at hub
        self.total_distance = 0
        self.trips = []  # List of HashMaps for trips
        self.route = []  # 2D array of routes for each trip

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

    def get_capacity(self):
        return self.capacity

    def set_route(self, route):
        """Set the truck's delivery route."""
        self.route = route

    def __str__(self):
        """Return a human-readable string representation of the truck."""
        return f"Truck ID: {self.id}, Total Distance: {self.total_distance:.2f} miles, Current Time: {self.current_time.strftime('%H:%M:%S')}"

    def add_trip(self, packages):
        """Add a new trip to the truck."""
        if len(packages) > self.capacity:
            raise ValueError("Trip exceeds truck capacity.")
        self.trips.append(packages)

    def _nearest_neighbor_for_trip(self, address_indices, adjacency_matrix, hub_index=0):
        """
        Optimize a single trip using the Nearest Neighbor algorithm.

        :param address_indices: List of address indices to visit in this trip.
        :param adjacency_matrix: 2D list representing distances between addresses.
        :param hub_index: Index of the hub in the adjacency matrix.
        :return: Tuple of (optimized route as list of indices, total distance).
        """
        if not address_indices:
            return [hub_index], 0  # If no addresses, return only the hub

        current_index = hub_index
        visited = set()
        route = [hub_index]
        # total_distance = 0

        while address_indices:
            nearest_distance = float('inf')
            nearest_index = None

            # Find the nearest unvisited address
            for address_index in address_indices:
                if address_index not in visited:
                    current_distance = float(
                        adjacency_matrix[current_index][address_index])
                    if current_distance < nearest_distance:
                        nearest_distance = current_distance
                        nearest_index = address_index
            if nearest_index is not None:
                route.append(nearest_index)
                # total_distance += nearest_distance
                visited.add(nearest_index)
                current_index = nearest_index
                # Remove from the list to avoid revisiting
                address_indices.remove(nearest_index)

        # Return to the hub
        distance_to_hub = float(adjacency_matrix[current_index][hub_index])
        # total_distance += distance_to_hub
        route.append(hub_index)
        print(f"route from nna, truck id: {self.id} : {route}")

        # return route, total_distance
        return route

    def optimize_route(self, adjacency_matrix):
        # 2d array with routes
        self.route = []
        # Remeber we prepopoluate this considering edge cases
        for trip in self.trips:
            # Get all address indices in the trip
            trip_addresses = list(trip.keys())
            trip_route = self._nearest_neighbor_for_trip(trip_addresses, adjacency_matrix)

            self.route.append(trip_route)
            # self.total_distance += trip_distance

    def process_deliveries(self, adjacency_matrix, cutoff_time=None):
        if cutoff_time is None:
            # Default to EOD
            cutoff_time = datetime.strptime("17:00:00", "%H:%M:%S")  
        # trip index is the hashmap index, trip is the HashMap
        for trip_index, trip in enumerate(self.trips):
            trip_route = self.route[trip_index]
            current_time = self.current_time
            # start delivering skip hub
            for i in range(1, len(trip_route)):
                prev_index = trip_route[i - 1]
                # Address_index to deliver too
                current_index = trip_route[i]

                # Calculate travel time
                # print("prev_index: ", prev_index)
                # print("current_index: ", current_index)
                # print("trip_route: ", trip_route)
                # print("len(trip_route)): ", self.route)
                distance = float(adjacency_matrix[prev_index][current_index])
                travel_time = (distance / self.speed) * 60  # Convert hours to minutes
                current_time += timedelta(minutes=travel_time)
                self.total_distance += distance

                # Check if cutoff time is exceeded
                if current_time > cutoff_time:
                    print(f"Cutoff time reached. Returning to hub.")
                    return

                # Retrieve all packages for this address. Trip <HashMap>.get(current_index<CurentaddresstoDeliver>)
                packages_at_address = trip.get(current_index)
                if packages_at_address:
                    # For each package at the address mark as delivered
                    for package in packages_at_address:
                        package.mark_delivered(self.id, current_time.strftime("%H:%M:%S"))
                        # print(f"Delivered package {package.id} at {current_time.strftime('%H:%M:%S')}")

                    # Remove delivered packages from the trip. Remove elemnt given address key
                    trip.delete(current_index)

            # Update truck's current time
            self.current_time = current_time
            # print(f"Trip {trip_index + 1} completed. Returned to hub at {self.current_time.strftime('%H:%M:%S')}.")
