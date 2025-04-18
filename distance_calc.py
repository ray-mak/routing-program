import csv

#load distance and address data from csv files
with open('distance.csv') as f:
    distance = csv.reader(f, delimiter=',')
    distance_list = list(distance)

with open('addresses.csv') as f:
    address = csv.reader(f, delimiter=',')
    address_list = list(address)
    print(address_list)

    # Get the addresses
    def get_address():
        return address_list

    # Calculate the total distance
    def total_distance(row, col, total):
        dist = distance_list[row][col]
        if dist == "":
            dist = distance_list[col][row]
        total += float(dist)
        return total
    
    # Calculate the distance between two addresses
    def distance_between(row, col):
        dist = distance_list[row][col]
        if dist == "":
            dist = distance_list[col][row]
        return float(dist)
    
    # Function to get the total distance travelled by a truck
    def truck_distance(truck_items):
        total_distance = 0
        
        for i in range(len(truck_items)):
            current_address = truck_items[i].address

            if i < len(truck_items) - 1:
                next_address = truck_items[i + 1].address
            else:
                next_address = address_list[0][1]
            
            current_id = None
            next_id = None

            for idx, row in enumerate(address_list):
                if row[1] == current_address:
                    current_id = idx
                if row[1] == next_address:
                    next_id = idx

            distance = distance_list[current_id][next_id]

            if distance == "":
                distance = distance_list[next_id][current_id]

            total_distance += float(distance)

        return total_distance
    