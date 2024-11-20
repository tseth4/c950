class Truck:
    def __init__(self, id, capacity):
        """
        Initialize the Truck object.
        
        :param id: Unique identifier for the truck.
        :param capacity: Maximum number of packages the truck can carry.
        """
        self.id = id
        self.capacity = capacity
        self.current_location = None  # Starting location (e.g., hub)
        self.route = []  # List of addresses/nodes to visit
        self.packages = []  # List of Package objects
        self.total_distance = 0  # Total distance traveled

    def assign_package(self, package):
        """Assign a package to the truck."""
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        return False

    def set_route(self, route):
        """Set the truck's delivery route."""
        self.route = route

    def deliver_package(self, address):
        """Simulate delivering a package."""
        self.packages = [pkg for pkg in self.packages if pkg.address != address]

    def update_location(self, new_location, distance):
        """Move the truck to a new location and update distance."""
        self.current_location = new_location
        self.total_distance += distance

    def reset(self):
        """Reset the truck for a new simulation."""
        self.current_location = None
        self.route = []
        self.packages = []
        self.total_distance = 0
        
    def __str__(self):
        """Return a human-readable string representation of the truck."""
        package_ids = [pkg.id for pkg in self.packages]
        route_str = " -> ".join(self.route) if self.route else "No route assigned"
        return (
            f"Truck ID: {self.id}\n"
            f"Capacity: {self.capacity}\n"
            f"Current Location: {self.current_location}\n"
            f"Total Distance Traveled: {self.total_distance} miles\n"
            f"Route: {route_str}\n"
            f"Assigned Packages: {package_ids}"
        )