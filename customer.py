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
        else:
            print(f"Could not add {item_name} to the cart.")

    def view_cart(self):
      
        print(f"{self.name}'s Cart: {self.cart}")

    def __str__(self):
        return f"Customer(name={self.name})"