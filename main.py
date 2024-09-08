#main.py
from customer import Customer

if __name__ == "__main__":
    customer1 = Customer("May")
    customer1.add_item_to_inventory("Shoes", 10)
    customer1.add_item_to_inventory("Hat", 5)

    customer1.add_to_cart("Shoes", 2)
    customer1.add_to_cart("Hat", 1)

    customer1.view_cart()

    #create and process a new order
    #By Kai Francis
    order = customer1.create_order()
    order.add_item_to_order("Shoes", 2)
    order.add_item_to_order("Hat", 1)

    order.view_order()
    order.checkout()

    print("Remaining Inventory:", customer1.get_inventory())
