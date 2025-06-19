class GroceryStore:
    def __init__(self):
        self.inventory ={}
        
    def add_item(self,item,price,quantity):
        if item in self.inventory:
            self.inventory[item]['quantity']+= quantity
        else:
            self.inventory[item]={'price':price,'quantity':quantity}
        print(f"{item} added succesfully")
        
    def display_inventory(self):
        if not self.inventory:
            print("inventory is empty")
        else:
            print("/n---inventory---")
            for item,info in self.inventory.items():
                print(f"{item} -{info['price']}-qty:{info['quantity']}")
                
    def update_item(self,item,price=None,quantity= None):
        if item in self.inventory:
            if price is not None:
                self.inventory[item]['price']=price
            if quantity is not None:
                self.inventory[item]['quantity']=quantity
                
            print(f"{item} updated succesfully")
                
        else:
            print(f"{item} not found in inventory")
            
    def delete_item(self,item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"{item} removed from inventory")
        else:
            print(f"{item} not found ")
            
    def generate_bill(self,cart):
        print("/n---bill---")
        total=0
        for item, qty in cart.items():
            if item in self.inventory and self.inventory[item]['quantity']>= qty:
                price= self.inventory[item]['price']
                total_price= price*qty
                print(f"{item}*{qty}={total_price}")
                total+= total_price
                self.inventory[item]['quantity']= qty
                
            else:
                print(f"{item} not available in stock")
        print(f"total bill: {total}")
        
store= GroceryStore()                
 
while True:
    print("\n Grocery Store")
    print("1. Add Item")
    print("2. Display Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Generate Bill")
    print("6. Exit")        
    
    choice= input(" enter choice:")
    
    if choice=='1':
        item = input("item name:")
        price= float(input("price:"))
        qty= int(input("quantity:"))
        store.add_item(item,price,qty)
        
    elif choice=='2':
        store.display_inventory()
        
    elif choice=='3':
        item = input("item name to update:")
        price= float(input("new price(press enter to skip):"))
        price= float(price) if price else None
        qty= int(input("new quantity(press enter to skip):"))
        qty= int(qty) if qty else None
        store.update_item(item,price,qty)
        
    elif choice=='4':
        item = input("item to delete:")
        store.delete_item(item)
        
    elif choice=='5':
        cart= {}
        while True:
            item = input(" enter item(or 'done' to finish):")
            if item.lower()== 'done':
                break
            qty= int(input("quantity:"))
            cart[item]= qty
        store.generate_bill(cart)
    elif choice =='6':
        print(" existing ...  thank you ")
        break
    else:
        print(" invalid choice. try again ")    
        