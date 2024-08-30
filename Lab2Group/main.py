#main.py
from customer import Customer

if __name__ == "__main__":
    customer1 = Customer("May")
    customer1.add_item_to_inventory("Shoes", 10)
    customer1.add_item_to_inventory("Hat", 5)

    customer1.add_to_cart("Shoes", 2)
    customer1.add_to_cart("Hat", 1)

    customer1.view_cart()


    print("Remaining Inventory:", customer1.get_inventory())