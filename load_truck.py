import csv
from hashtable import HashTable
from package import Package
import distance_calc
from route_algo import create_route

# Function to set the location of each package
def set_location(truck_items):
    for package in truck_items:
        for address in distance_calc.get_address():
            if package.address == address[1]:
                package.location = address[0]

# Load packages from a CSV file
with open('packages.csv') as f:
    packages = csv.reader(f, delimiter=',')

    hashtable = HashTable()
    truck1 = []
    truck2 = []
    truck3 = []

    for package in packages:
        package_id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zip_code = package[4]
        deadline = package[5]
        weight = package[6]
        special_notes = package[7]
        location = ""
        status = "At the hub"

        package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes, location, status) 

        print(f"Loaded package ID: {package.package_id}") 
        
        # Packages that must be in truck 2 or are delayed are assigned to truck 2
        if special_notes == "Can only be on truck 2" or special_notes == "Delayed on flight---will not arrive to depot until 9:05 am":
            truck2.append(package)

        # Package with wrong address assigned to truck 3 to wait for updated address
        elif package_id == 9:
            truck3.append(package)

        # Packages that do not have EOD deadline and need to be together are assigned to truck 1
        elif deadline != "EOD" or package_id == 1:
            truck1.append(package)
        
        # Package 19 has EOD deadline, but must be delivered with 14 and 16 which do not
        elif package_id == 19:
            truck1.append(package)

        # Add remaining packages to the trucks
        if package not in truck1 and package not in truck2 and package not in truck3:
            if len(truck3) < 16:
                truck3.append(package)
            elif len(truck2) < 16:
                truck2.append(package)
            else:
                truck1.append(package)
        
        # Insert packages into hash table
        hashtable.insert(package.package_id, package)

    set_location(truck1)
    set_location(truck2)
    set_location(truck3)       

    # Call create_route function to get the best route for each truck
    truck1_routes = create_route(truck1, 0, [], [0])
    truck2_routes = create_route(truck2, 0, [], [0])
    truck3_routes = create_route(truck3, 0, [], [0])      


    # Print truck routes (to test above function)
    truck1_order, truck1_locations = truck1_routes
    truck2_order, truck2_locations = truck2_routes
    truck3_order, truck3_locations = truck3_routes

    # Call truck_distance to calculate the total distance for each truck
    truck1_distance = distance_calc.truck_distance(truck1_order)
    truck2_distance = distance_calc.truck_distance(truck2_order)
    truck3_distance = distance_calc.truck_distance(truck3_order)

    total_mileage = truck1_distance + truck2_distance + truck3_distance
        
    print(f"Truck 1 Distance: {truck1_distance:.2f} miles")
    print(f"Truck 2 Distance: {truck2_distance:.2f} miles")
    print(f"Truck 3 Distance: {truck3_distance:.2f} miles")
    print(f"Total Distance: {total_mileage:.2f} miles")

    # # Print Truck 1
    # print("\n--- Truck 1 Route ---")
    # for pkg in truck1_order:
    #     print(f"Package ID: {pkg.package_id}, Address: {pkg.address}")

    # # Print Truck 2
    # print("\n--- Truck 2 Route ---")
    # for pkg in truck2_order:
    #     print(f"Package ID: {pkg.package_id}, Address: {pkg.address}")

    # # Print Truck 3
    # print("\n--- Truck 3 Route ---")
    # for pkg in truck3_order:
    #     print(f"Package ID: {pkg.package_id}, Address: {pkg.address}")

