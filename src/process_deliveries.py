from datetime import datetime, timedelta


def process_deliveries(truck, adjacency_matrix):
    # print("addresses: ")
    # print(addresses)
    """
    Simulate deliveries for a truck and update package information.

    :param truck: The Truck object to process.
    :param adjacency_matrix: 2D list of distances between addresses.
    :param addresses: List of address names corresponding to adjacency matrix indices.
    """
    if not truck.route:
        print(f"Truck {truck.id} has no route assigned.")
        return

    # Start at 8:00 a.m.
    current_time = truck.get_current_time()
    speed_mph = truck.get_speed()
    
    # TODO: Use truck.current_location
    # TODO: As you are delivering pop off the packaged
    # TODO: Handle routing back to the hiub
    # TODO: Idea? for truck route add the package id along with location index for easier updates
    
    # This is basically taking the opimized truck route index addresses in the array
    # and adding the distance to get from current location to the next

    for i in range(1, len(truck.route)):  # Skip the hub
        # Get distance from the previous stop to the current stop
        prev_address_index = truck.get_current_location_index()
        current_address_index = truck.route[i]
        truck.current_location_index = current_address_index
        # prev_index = addresses.index(prev_address)
        # current_index = addresses.index(current_address)
        
        # Get distance to current location location
        distance = float(adjacency_matrix[prev_address_index][current_address_index])

        # Calculate travel time
        travel_time = (distance / speed_mph) * 60  # Convert hours to minutes
        # adding travel time to the current time
        current_time += timedelta(minutes=travel_time)
        truck.current_time = current_time

        # Mark packages as delivered that their address matches the current address
        for package in truck.packages:

            if package.get_address_index() == current_address_index:
                # Deliver
                package.mark_delivered(truck.id, current_time.strftime("%H:%M:%S"))

                
    
    
