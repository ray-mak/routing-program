from distance_calc import *

# Greedy algorithm to determine the order of packages being delivered
def create_route(truck_items, current_location, route_order, location_indexes):
    if not truck_items:
        return truck_items
    
    next_location = 0
    shortest_distance = float('inf')

    # Find the closest package
    for package in truck_items:
        location = int(package.location)
        distance = distance_between(current_location, location)
        if distance < shortest_distance:
            shortest_distance = distance
            next_location = location

    # Find and move the closest package
    for package in truck_items:
        location = int(package.location)
        if distance_between(current_location, location) == shortest_distance:
            route_order.append(package)
            location_indexes.append(location)
            truck_items.pop(truck_items.index(package))
            current_location = next_location
            create_route(truck_items, current_location, route_order, location_indexes)

    return route_order, location_indexes
