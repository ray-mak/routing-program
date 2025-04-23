from datetime import datetime, timedelta
import distance_calc


# Function to assign delivery time for each package in each truck
def assign_delivery_times(truck_route, departure_time):
    current_time = departure_time

    for i in range(len(truck_route)):
        package = truck_route[i]
        if i == 0:
            previous_location = 0
        else:
            previous_location = int(truck_route[i - 1].location)

        current_location = int(package.location)
        distance = distance_calc.distance_between(previous_location, current_location)
        travel_time = timedelta(hours=distance / 18)
        current_time += travel_time

        package.delivery_time = current_time
        package.status = "Delivered"

# Function to update the status of each package
def update_status(truck_route, departure_time, current_time):

    for package in truck_route:
        # Update the address of package 9 if it is after 10:20
        if package.package_id == 9 and current_time > datetime.strptime("10:20", "%H:%M"):
            package.address = "410 S State St"
            package.zip_code = "84111"
    
        if current_time < departure_time:
            package.status = "At the hub"
        elif departure_time <= current_time < package.delivery_time:
            package.status = "En Route"
        else:
            package.status = "Delivered"