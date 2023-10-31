import json


# Function to load the menu from a JSON file.
def load_menu():
    try:
        with open("menu.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Function to save the menu to a JSON file.
def save_menu(menu):
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=4)


# Function to load the order from a JSON file.
def load_orders():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Function to save the order to a JSON file.
def save_orders(orders):
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=4)


# Function to display the menu.
def display_menu():

    menu = load_menu()

    print("\nZesty Zomato Menu:\n")
    if not menu:
        print("\nThe menu is empty. Add some delicious dishes!")
    else:
        for dish_id, dish_info in menu.items():
            availability = "Available" if dish_info["available"] else "Not Available"
            print(
                f"{dish_id}. {dish_info['name']} - Rs.{dish_info['price']} - {availability}")


# Function to add a new dish to the menu.
def add_dish():

    menu = load_menu()

    dish_id = len(menu) + 1
    name = input("\nEnter the name of the new dish: ")
    price = float(input("\nEnter the price of the new dish: "))
    available = True

    menu[dish_id] = {"name": name, "price": price, "available": available}
    save_menu(menu)  # Save the updated menu to the JSON file.
    print(f"\n{name} has been added to the menu with dish ID {dish_id}.")


# Function to remove a dish from the menu.
def remove_dish():

    menu = load_menu()

    display_menu()  # Display the current menu for reference.

    dish_id = input("\nEnter the ID of the dish you want to remove: ")

    if dish_id in menu:
        removed_dish = menu.pop(dish_id)
        print(f"\n{removed_dish['name']} has been removed from the menu.")
        save_menu(menu)  # Save the updated menu to the JSON file.
    else:
        print("\nInvalid dish ID. The dish does not exist in the menu.")


# Function to update the availability of a dish.
def update_availability():

    menu = load_menu()

    display_menu()  # Display the current menu for reference.

    dish_id = input("\nEnter the ID of the dish you want to update: ")

    if dish_id in menu:
        availability = input(
            f"\nSet availability for {menu[dish_id]['name']} (Available/Not Available): ").strip().lower()
        if availability == "available":
            menu[dish_id]['available'] = True
        elif availability == "not available":
            menu[dish_id]['available'] = False
        else:
            print("\nInvalid availability. Please enter 'Available' or 'Not Available'.")
            return
        save_menu(menu)  # Save the updated menu to the JSON file.
        print(f"\n{menu[dish_id]['name']} availability updated.")
    else:
        print("\nInvalid dish ID. The dish does not exist in the menu.")


# Function to take an order from a customer.
def take_order():

    menu = load_menu()
    orders = load_orders()

    customer_name = input("\nEnter the customer's name: ")
    display_menu()  # Display the current menu for reference.

    order_items = []
    while True:
        dish_id = input(
            "\nEnter the ID of the dish to add to the order (or 'done' to finish the order): ")

        if dish_id.lower() == 'done':
            break

        try:
            if dish_id in menu and menu[dish_id]['available']:
                order_items.append(dish_id)
                print(f"\n{menu[dish_id]['name']} added to the order.")
            else:
                print("\nInvalid dish ID. The dish is not available.")
        except ValueError:
            print(
                "\nInvalid input. Please enter a valid dish ID or 'done' to finish the order.")

    if order_items:
        # Generate a unique order ID.
        order_id = len(orders) + 1
        order = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "received"
        }
        orders[order_id] = order
        save_orders(orders)  # Save the updated orders to the JSON file.
        print(
            f"\nOrder for {customer_name} (Order ID: {order_id}) has been received.")
    else:
        print("\nNo items added to the order. Order not placed.")


# Function to update the status of an order.
def update_order_status():

    orders = load_orders()

    display_orders()  # Display the list of orders for reference.

    order_id = input("\nEnter the Order ID you want to update: ")

    if order_id in orders:
        new_status = input(
            "\nEnter the new status (received/preparing/ready for pickup/delivered): ").strip().lower()
        if new_status in ["received", "preparing", "ready for pickup", "delivered"]:
            orders[order_id]['status'] = new_status
            save_orders(orders)  # Save the updated orders to the JSON file.
            print(f"\nOrder {order_id} status updated to '{new_status}'.")
        else:
            print("\nInvalid status. Please enter one of the valid statuses.")
    else:
        print("\nInvalid Order ID. The order does not exist.")


# Function to display the list of orders.
def display_orders():

    menu = load_menu()
    orders = load_orders()

    print("\nZesty Zomato Orders:")
    if not orders:
        print("\nNo orders placed yet.")
    else:
        for order_id, order_info in orders.items():
            customer_name = order_info["customer_name"]
            status = order_info["status"]
            order_items = ", ".join([menu[dish_id]["name"]
                                    for dish_id in order_info["order_items"]])
            print(
                f"\nOrder ID: {order_id} - Customer: {customer_name} - Status: {status}")
            print(f"Order Items: {order_items}")


# Function to generate total bill of an order.
def generate_bill():

    menu = load_menu()
    orders = load_orders()

    display_orders()

    order_id = input("\nEnter the Order ID to generate bill: ")
    order_info = orders.get(order_id)

    if order_info:
        customer_name = order_info["customer_name"]
        status = order_info["status"]
        order_items = order_info["order_items"]
        total_price = sum([menu[dish_id]["price"] for dish_id in order_items])

        print(
            f"\nOrder ID: {order_id} - Customer: {customer_name} - Status: {status}")
        print("\nOrder Items:")
        for dish_id in order_items:
            dish_info = menu[dish_id]
            print(f"- {dish_info['name']} - Rs.{dish_info['price']:.2f}")
        print(f"\nTotal Bill: Rs.{total_price:.2f}")
    else:
        print(f"\nOrder with Order ID {order_id} does not exist.")


# Main function to run the application
def main():

    while True:
        print("\n ==== Zesty Zomato Food Delivery System ====")
        print("\n1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Generate Bill of an order")
        print("9. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            update_availability()
        elif choice == "5":
            take_order()
        elif choice == "6":
            update_order_status()
        elif choice == "7":
            display_orders()
        elif choice == "8":
            generate_bill()
        elif choice == "9":
            print("\nGoodbye! Thank you for using Zesty Zomato.")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")


# Run the main function
if __name__ == "__main__":
    main()
