# Package class to store package information
class Package:
    def __init__(self, package_id, truck_number, address, city, state, zip_code, deadline, weight, special_notes, status, location, delivery_time=None):
        self.package_id = package_id
        self.truck_number = truck_number
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.location = location
        self.status = status
        self.delivery_time = delivery_time 


    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, "
                f"City: {self.city}, State: {self.state}, Zip: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight}, "
                f"Status: {self.status}, Delivered At: {self.delivery_time}")