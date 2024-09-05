# Mastewal Berhe, Sumeyya Sherief, & Rebecca Rogovich
from shop import Shop

class Customer(Shop):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.cart = []

    def add_to_cart(self, item_name, quantity):
      
        if self.decrease_item_quantity(item_name, quantity):
            self.cart.append((item_name, quantity))
            print(f"Added {quantity} of {item_name} to {self.name}'s cart.")
            return "item added to cart"  
        else:
            print(f"Could not add {item_name} to the cart.")
            return "Cannot add item to cart"  

    def view_cart(self):
        print(f"{self.name}'s Cart: {self.cart}")

    def unpurchase(self, item_name, quantity):
        # Check if the item is in the cart and there's enough quantity to remove
        if item_name in self.cart and self.cart[item_name] >= quantity:
            self.cart[item_name] -= quantity
            self.shop.add_item_to_inventory(item_name, quantity)
            # If the cart quantity drops to 0, remove the item from the cart
            if self.cart[item_name] == 0:
                del self.cart[item_name]
            return f"Removed {quantity} of {item_name} from {self.name}'s cart."
        else:
            # Debugging output
            print(f"Cannot remove item from cart: {item_name} not found or insufficient quantity.")
            return "Cannot remove item from cart"

        
    def apply_discount(self, item_name, discount):
        return self.shop.apply_discount(item_name, discount)

    def __str__(self):
        return f"Customer(name={self.name})"
