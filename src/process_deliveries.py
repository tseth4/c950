from datetime import datetime, timedelta


def process_deliveries(truck, adjacency_matrix, addresses):
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
    current_time = datetime.strptime("08:00:00", "%H:%M:%S")
    speed_mph = 18

    for i in range(1, len(truck.route)):  # Skip the hub
        # Get distance from the previous stop to the current stop
        prev_address = truck.route[i - 1]
        current_address = truck.route[i]
        prev_index = addresses.index(prev_address)
        current_index = addresses.index(current_address)
        distance = float(adjacency_matrix[prev_index][current_index])

        # Calculate travel time
        travel_time = (distance / speed_mph) * 60  # Convert hours to minutes
        current_time += timedelta(minutes=travel_time)

        # Mark packages as delivered
        for package in truck.packages:
            if package.address == current_address:
                package.mark_delivered(
                    truck.id, current_time.strftime("%H:%M:%S"))
