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
        self.truck_id = None
        self.address_index = None

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_address_index(self, index):
        self.address_index = index

    def get_address_index(self):
        return self.address_index

    def mark_delivered(self, truck_id, delivery_time):
        """
        Update the package status to Delivered.
        """
        self.status = PackageStatus.DELIVERED
        self.truck_id = truck_id
        self.delivery_time = delivery_time

    def meets_deadline(self):
        """
        Check if the package was delivered on or before its deadline.

        :return: True if the package meets the deadline, False otherwise.
        """
        if self.deadline == "EOD" and self.status == PackageStatus.DELIVERED:
          # End of day deadlines are always met
            return True

        if self.delivery_time is None:
            return False  # If no delivery time, it doesn't meet the deadline
        if self.deadline == "EOD":
            deadline_dt = datetime.strptime("17:00:00", "%H:%M:%S")
        else:
            # Parse the deadline into a datetime object
            deadline_dt = datetime.strptime(self.deadline, "%I:%M %p")

        # deadline_dt = datetime.strptime(self.deadline, "%I:%M %p")
        delivery_dt = datetime.strptime(self.delivery_time, "%H:%M:%S")

        # Meets deadline if delivered on or before deadline
        return delivery_dt <= deadline_dt

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

    def __str__(self):
        """
        Return a formatted string with package details.
        """
        meets_deadline_status = "Yes" if self.meets_deadline() else "No"

        return (
            f"id: {self.id}   address: {self.address} | "
            f"Deadline: {self.deadline}| Status: {self.status.value} |  "
            f"by Truck-{self.truck_id} | Delivery time: {
                self.delivery_time if self.delivery_time else 'Pending'}| Meets Deadline: {meets_deadline_status}"
            # f"| notes: {self.notes}"

        )

    def get_address(self):
        return f"{self.address}"


