# Raymond Mak, ID 012483817

from load_truck import *
def main():
    print("Greetings! Please select one of the following options:")
    print("1. Get status of single package at a specific time")
    print("2. Get status of all packages at a specific time")
    print("3. Get total mileage of all trucks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1,2,3 or 4 to exit): ")
        if choice == "1":
            package_id = int(input("Enter the package ID: "))
            time = input("Enter the time in 24-hour format (HH:MM): ")
            get_package_status(package_id, time)
            break
        elif choice == "2":
            time = input("Enter the time in 24-hour format (HH:MM): ")
            get_all_package_status(time)
            break
        elif choice == "3":
            print_total_distance()
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()