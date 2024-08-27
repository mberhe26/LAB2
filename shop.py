class Shop:
    def __init__(self):
        self.inventory = {}

    def add_item_to_inventory(self, item_name, quantity):
      
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def decrease_item_quantity(self, item_name, quantity):
      
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            return True
        else:
            print(f"Cannot add {item_name} to cart: Not enough in inventory.")
            return False

    def get_inventory(self):
        
        return self.inventory