import csv
from hashtable import HashTable
from package import Package

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
        status = "At the hub"

        package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes, status) 

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


