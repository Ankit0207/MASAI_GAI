inventory = {}

def add_snack(snack_id, name, price):
    if snack_id in inventory:
        print("Snack already exists in the inventory.")
    else:
        snack = {
            "name": name,
            "price": price,
            "available": True,
            "sales": 0
        }
        inventory[snack_id] = snack
        print(f"{name} added to the inventory.")

def remove_snack(snack_id):
    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from the inventory.")
    else:
        print("Snack not found in the inventory.")

def update_availability(snack_id, available):
    if snack_id in inventory:
        inventory[snack_id]["available"] = available
        print("Availability updated.")
    else:
        print("Snack not found in the inventory.")

def sell_snack(snack_id):
    if snack_id in inventory:
        snack = inventory[snack_id]
        if snack["available"]:
            snack["sales"] += 1
            snack["available"] = False
            print(f"Sold 1 {snack['name']}. Total Sales: {snack['sales']}")
        else:
            print("This snack is not available for sale.")
    else:
        print("Snack not found in the inventory.")

def display_inventory():
    print("Inventory:")
    for snack_id, snack in inventory.items():
        availability = "Available" if snack["available"] else "Not Available"
        print(f"ID: {snack_id}, Name: {snack['name']}, Price: {snack['price']}, Availability: {availability}, Sales: {snack['sales']}")

def main():
    while True:
        print("\n==== Canteen Inventory Management ====")
        print("1. Add a snack to the inventory")
        print("2. Remove a snack from the inventory")
        print("3. Update snack availability")
        print("4. Sell Snack")
        print("5. Display Inventory")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            snack_id = input("Enter Snack ID: ")
            name = input("Enter Snack Name: ")
            price = float(input("Enter Snack Price: "))
            add_snack(snack_id, name, price)

        elif choice == '2':
            snack_id = input("Enter Snack ID: ")
            remove_snack(snack_id)

        elif choice == '3':
            snack_id = input("Enter Snack ID: ")
            available = input("Is the snack available? (yes/no): ").lower()
            update_availability(snack_id, available == 'yes')

        elif choice == '4':
            snack_id = input("Enter Snack ID: ")
            sell_snack(snack_id)

        elif choice == '5':
            display_inventory()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
