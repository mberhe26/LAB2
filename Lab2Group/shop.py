# Mastewal Berhe, Sumeyya Sherief, & Rebecca Rogovich
class Shop:
    def __init__(self):
        self.inventory = {}

    def add_item_to_inventory(self, item_name, quantity):
      
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        return "Item added to inventory"

    def decrease_item_quantity(self, item_name, quantity):
      
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            result = True
        
        else:
            print(f"Cannot add {item_name} to cart: Not enough in inventory.")
            result = False
        
        print(result)  
        return result

    def get_inventory(self):
        
        return self.inventory