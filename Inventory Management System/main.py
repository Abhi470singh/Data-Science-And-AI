from inventory import Inventory
from product import Product

def menu():
    print("\n" + "=" * 50)
    print("📦 Inventory Management System")
    print("=" * 50)
    print("1. Add Product: ")
    print("2. Display products: ")
    print("3. Search Product:")
    print("4. Update product: ")
    print("5. Delete Product: ")
    print("6. Sell Product: ")
    print("7. Add Stock: ")
    print("8. Low stock Report: ")
    print("9. Inventory Value: ")
    print("10. Total Products:")
    print("11. Save Data:")
    print("12. Exits: ")
    print("=" * 50)
    
    
def main():
    inventory = Inventory()
        
    while True:
        menu()
            
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                
                product = Product(product_id, name,price, quantity)
                inventory.add_product(product)
                
            elif choice == 2:
                inventory.display_products()
                
            elif choice ==3:
                product_id = int(input("Enter Product ID: "))
                product = inventory.search_product(product_id)
                
                if product:
                    product.display()
                    
                else:
                    print("❌ Product not found.")
                    
            elif choice == 4:
                product_id = int(input("Enter Product ID: "))
                inventory.update_product(product_id)
            
            elif choice == 5:
                product_id = int(input("Enter Product ID: "))
                inventory.delete_product(product_id)
              
            elif choice == 6:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity to sell: "))
                inventory.sell_product(product_id, quantity)  
                
            elif choice == 7: 
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity to Add: "))
                inventory.add_stock(product_id, quantity)
                
            elif choice == 8:
                inventory.low_stock()
                
            elif choice == 9:
                inventory.inventory_value()
                
            elif choice == 10:
                inventory.total_products()
            
            elif choice == 11:
                inventory.save_data()
            
            elif choice == 12:
                inventory.save_data()
                print("\n ✅ Data saved successfully.")
                print("Thank you for using Inventory Management System!")
            
            else:
                print(" ❌ Invalid Choice.")
                
        except ValueError:
            print(" ❌ Please enter a valid number.")
            
        except Exception as e:
            print("error", e)
            
if __name__ == "__main__":
    main()   
        
                              