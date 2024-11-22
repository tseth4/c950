from datetime import datetime, timedelta


def process_deliveries(truck, adjacency_matrix, cutoff_time=None):
    """
    Simulate deliveries for a truck and update package information.

    :param truck: The Truck object to process.
    :param adjacency_matrix: 2D list of distances between addresses.
    """
    # Set default cutoff time to 5:00 PM if not provided
    if cutoff_time is None:
        cutoff_time = datetime.strptime("17:00:00", "%H:%M:%S")
  
    while truck.packages:  # Process deliveries while there are packages to deliver
        # Select up to the truck's capacity for this trip <16>
        print("truck.packages length: ", len(truck.packages))
        trip_packages = truck.packages[:truck.get_capacity()]
        truck.route = [0] + [p.get_address_index() for p in trip_packages]  # Hub is index 0
        # Optimize the route for this trip
        truck.optimize_route(adjacency_matrix)

        print(f"Truck-{truck.id} is starting a trip with {len(trip_packages)} packages.")

        # Simulate the delivery of this trip's packages
        current_time = truck.get_current_time()
        speed_mph = truck.get_speed()

        for i in range(1, len(truck.route)):  # Skip the hub
            # Get distance from the previous stop to the current stop
            prev_address_index = truck.get_current_location_index()
            current_address_index = truck.route[i]
            truck.current_location_index = current_address_index

            # Calculate distance and travel time
            distance = float(
                adjacency_matrix[prev_address_index][current_address_index])
            travel_time = (distance / speed_mph) * 60  # Convert hours to minutes
            current_time += timedelta(minutes=travel_time)
            
            # Check if current time exceeds the cutoff
            if current_time > cutoff_time:
                print(f"Truck-{truck.id} has reached the cutoff time ({cutoff_time.strftime('%H:%M:%S')}).")
                truck.current_time = current_time
                truck.current_location_index = current_address_index
                return  # Stop the delivery process
                        
            # Update the truck's current time
            truck.current_time = current_time

            # Deliver packages for the current stop
            for package in trip_packages:
                if package.get_address_index() == current_address_index:
                    package.mark_delivered(
                        truck.id, current_time.strftime("%H:%M:%S"))

        # Return to the hub
        distance_to_hub = float(adjacency_matrix[truck.get_current_location_index()][0])
        travel_time_to_hub = (distance_to_hub / speed_mph) * 60
        current_time += timedelta(minutes=travel_time_to_hub)
       
       
       
        truck.current_time = current_time
        truck.current_location_index = 0  # Back to hub

        print(f"Truck-{truck.id} has returned to the hub at {
              truck.current_time.strftime('%H:%M:%S')}.")

        # Remove delivered packages from the truck's package list
        # Remove the delivered packages
        truck.packages = truck.packages[len(trip_packages):]
