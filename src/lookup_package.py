def lookup_package(package_id, package_map):

    package = package_map.get(package_id)
    if not package:
        return f"Package with ID {package_id} not found."

    # Extract package details
    details = {
        "Package ID": package.id,
        "Delivery Address": package.address,
        "Delivery Deadline": package.deadline,
        "City": package.city,
        "ZIP Code": package.zipcode,
        "Weight": f"{package.weight_in_kilo} kg",
        "Delivery Status": f"{package.status.value} (Delivered at {package.delivery_time})" 
                            if package.delivery_time else package.status.value,
    }

    # Format details as a string
    details_str = "\n".join(f"{key}: {value}" for key, value in details.items())
    return details_str