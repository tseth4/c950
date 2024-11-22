def process_deliveries(self, adjacency_matrix, cutoff_time=None):
    """
    Simulate deliveries for this truck, returning to the hub to pick up more packages as needed.

    :param adjacency_matrix: 2D list of distances between addresses.
    :param cutoff_time: A datetime object representing the cutoff time for deliveries (default: EOD).
    """
    if not self.packages:
        print(f"Truck {self.id} has no packages to deliver.")
        return

    # Default cutoff time to EOD (5:00 PM)
    if cutoff_time is None:
        cutoff_time = datetime.strptime("17:00:00", "%H:%M:%S")

    # Track undelivered packages in this truck's assigned set
    # TODO: questionable - all assigned 16 packages that are at the hub??
    undelivered_packages = [pkg for pkg in self.packages if pkg.status == PackageStatus.AT_HUB]

    while undelivered_packages:
        # Load the truck with up to its capacity
        current_trip = []
        for _ in range(self.capacity):
            if undelivered_packages:
                package = undelivered_packages.pop(0)
                package.set_status(PackageStatus.EN_ROUTE)
                current_trip.append(package)

        # Optimize the route for this trip
        self.route = [0] + [pkg.get_address_index() for pkg in current_trip]
        self.optimize_route(adjacency_matrix)

        print(f"Truck-{self.id} is starting a trip with {len(current_trip)} packages.")

        # Start delivery simulation for this trip
        current_time = self.get_current_time()
        speed_mph = self.get_speed()

        for i in range(1, len(self.route)):  # Skip hub (index 0)
            prev_index = self.get_current_location_index()
            current_index = self.route[i]
            self.current_location_index = current_index

            # Calculate travel time
            distance = float(adjacency_matrix[prev_index][current_index])
            travel_time = (distance / speed_mph) * 60  # Convert hours to minutes
            current_time += timedelta(minutes=travel_time)

            # Check if cutoff time is exceeded
            if current_time > cutoff_time:
                print(f"Truck-{self.id} reached the cutoff time. Returning to hub.")
                return

            self.current_time = current_time

            # Deliver packages at the current location
            for package in current_trip:
                if package.get_address_index() == current_index:
                    package.mark_delivered(self.id, current_time.strftime("%H:%M:%S"))

        # Return to the hub
        distance_to_hub = float(adjacency_matrix[self.get_current_location_index()][0])
        travel_time_to_hub = (distance_to_hub / speed_mph) * 60
        current_time += timedelta(minutes=travel_time_to_hub)
        self.current_time = current_time
        self.current_location_index = 0

        print(f"Truck-{self.id} returned to the hub at {self.current_time.strftime('%H:%M:%S')}.")

        # Update undelivered packages (filter remaining at hub)
        undelivered_packages = [pkg for pkg in self.packages if pkg.status == PackageStatus.AT_HUB]
