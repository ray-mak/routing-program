# Package class to store package information
class Package:
    def __init__(self, package_id, address, weight, deadline, city, zip_code, status="At the hub", delivery_time=None):
        self.package_id = package_id
        self.address = address
        self.weight = weight
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.status = status
        self.delivery_time = delivery_time

    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, "
                f"City: {self.city}, Zip: {self.zip_code}, Weight: {self.weight}, "
                f"Status: {self.status}, Delivered At: {self.delivery_time}")