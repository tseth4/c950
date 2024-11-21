from enum import Enum
from src.package_status import PackageStatus
from datetime import datetime


class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight_in_kilo, notes, status=PackageStatus.AT_HUB):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight_in_kilo = weight_in_kilo
        self.notes = notes
        self.status = status
        self.delivery_time = None  # To be updated when delivered

    def set_status(self, status):
        self.status = status

    def mark_delivered(self, truck_id, delivery_time):
        """
        Update the package status to Delivered.
        """
        self.status = PackageStatus.DELIVERED
        self.truck_id = truck_id
        self.delivery_time = delivery_time

    @staticmethod
    def parse_deadline(p):
        if p[1].deadline == "EOD":
            # Assign a large value to ensure EOD comes last
            return datetime.max
        else:
            # Convert deadline to a datetime object for comparison
            return datetime.strptime(p[1].deadline, "%I:%M %p")

    @classmethod
    def from_csv_row(cls, row):
        """Create a Package instance from a CSV row (positional)."""
        return cls(
            id=row[0],
            address=row[1],
            city=row[2],
            state=row[3],
            zipcode=row[4],
            deadline=row[5],
            weight_in_kilo=row[6],
            notes=row[7] if len(row) > 7 else None  # Handle missing notes
        )

    # def __str__(self):
    #     """
    #     Return a human-readable string representation of the package.
    #     """
    #     return (
    #         f"Package ID: {self.id}\n"
    #         f"Address: {self.address}, {self.city}, {
    #             self.state} {self.zipcode}\n"
    #         f"Deadline: {self.deadline}\n"
    #         f"Weight: {self.weight_in_kilo} kg\n"
    #         f"Notes: {self.notes or 'None'}\n"
    #         f"Status: {self.status.value}\n"
    #         f"Delivery Time: {self.delivery_time or 'Pending'}"
    #     )
    def __str__(self):
        """
        Return a formatted string with package details.
        """
        return (
            f"id: {self.id}   address: {self.address} {self.city}, {
                self.state}, {self.zipcode}, "
            f"{self.deadline}, {self.weight_in_kilo}, {self.notes}, ... {self.status.value} "
            f"by Truck-{self.truck_id}, {self.delivery_time if self.delivery_time else 'Pending'}"
        )

    def get_address(self):
        return f"{self.address}"


# "Package
# ID",	Address,	City, 	State,	Zip,	"Delivery Deadline,	Weight KILO,	Special notes
