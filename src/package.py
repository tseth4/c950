from enum import Enum
from package_status import PackageStatus


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


    def __str__(self):
        """
        Return a human-readable string representation of the package.
        """
        return (
            f"Package ID: {self.id}\n"
            f"Address: {self.address}, {self.city}, {self.state} {self.zipcode}\n"
            f"Deadline: {self.deadline}\n"
            f"Weight: {self.weight_in_kilo} kg\n"
            f"Notes: {self.notes or 'None'}\n"
            f"Status: {self.status.value}\n"
            f"Delivery Time: {self.delivery_time or 'Pending'}"
        )


# "Package
# ID",	Address,	City, 	State,	Zip,	"Delivery Deadline,	Weight KILO,	Special notes
