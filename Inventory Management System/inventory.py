from product import Product
from file_manager import FileManager

class Inventory:
    def __init__(self):
        self.products = FileManager.load_products()
        
        
# Add Product to Inventory

    def add_product(self, product):
        for p in self.products:
            if p.product_id == product.product_id:
                print(" ❌ Product ID already exists!")
                return
        
        self.products.append(product)
        print("✅ Product  added successfully.") 
        
    def save_data(self):
            FileManager.save_product(self.products)
            
# Display All Products

    def display_products(self):
        if not self.products:
            print("No products available in the inventory.")
            return
        
        print("/n======== PRODUCT LIST ========")
        for product in self.products:
            product.display()
            
# Search product

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
            return None
        
# Update Prodect Details

    def update_product(self, product_id):
        product = self.search_product(product_id)
        
        if product:
            print("\nLeave blank if you don't want to a change the value.")
            
            name = input("Enter New Name:")
            
            price = float(input("Enter New Price:"))
            
            quantity = int(input("Enter New Quantity: "))
            
            if name == "":
                name = None
                
            if price == "":
                price = None
            else:
                price = float(price)
            
            if quantity == "":
                quantity = None
            
                   
            product.update_product(name, price, quantity)
            print("✅ Product details updated successfully.")
            
        else:
            print("❌ Product not found.")
            
# Sell Product

    def sell_product(self, product_id, quantity):
        product = self.search_product(product_id)
        
        if product:
            product.sell_product(quantity)
            
        else:
            print("❌ Product not found.")
            
# Add Stock to product

    def add_stock(self, product_id, quantity):
        product = self.search_product(product_id)
        
        if product:
            product.add_stock(quantity)
        else:
            print("❌ Product not found.")
            
# Total Inventort Value
  
    def inventory_value(self):
        total = 0
        
        for product in self.products:
            total += product.price * product.quantity
            
        print(f"\n====== Total Inventory Value: ₹{total:.2f} ======")
        
# Low Stock Report

    def low_stock(self, limit=5):
        print("\n====== Low STOCK PRODUCTS ======")
        
        found = False
        
        for product in self.products:
            if product.quantity <= limit:
                product.display()
                found = True
                
        if not found:
            print("No low stock products.")
            
# Total Products
    def total_products(self):
        print(f"\nTotal Prodects : {len(self.products)}")

        
        
        
        
        


        
        