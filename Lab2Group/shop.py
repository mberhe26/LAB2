# Mastewal Berhe, Sumeyya Sherief, & Rebecca Rogovich
class Shop:
    def __init__(self):
        self.inventory = {}

    def apply_discount(self, item_name, amount, discount):
       
        if item_name not in self.inventory:
            print(f"Item {item_name} not found in inventory.")
            return False
        
   
        amount = float(self.inventory[item_name])

        discount_amount = amount * discount / 100
        
   
        self.inventory[item_name] = amount - discount_amount
        return True
    

    def add_item_to_inventory(self, item_name, quantity):
       
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        return "Item added to inventory"

    def decrease_item_quantity(self, item_name, quantity):
        
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            resu