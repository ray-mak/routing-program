import csv

#load distance and address data from csv files
with open('distance.csv') as f:
    distance = csv.reader(f, delimiter=',')
    distance_list = list(distance)

with open('addresses.csv') as f:
    address = csv.reader(f, delimiter=',')
    address_list = list(address)

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
    