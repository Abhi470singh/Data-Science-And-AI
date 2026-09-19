import json
import os
from product import Product

class FileManager:
    
    FILE_NAME = "data.json"
    
    @ staticmethod
    def save_product(products):
        """
        Save all products to data.json
        """
        
        try:
            data = [product.to_dict() for product in products]
            
            with open(FileManager.FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
                
            print("✅ Products saved successfully.")
            
        except Exception as e:
            print("Error while saving data:", e)
            
    @staticmethod
    def load_products():
        
        """Load all products from data.json
        """
        products = []
        
        if not os.path.exists(FileManager.FILE_NAME):
            return products
        
        try:
            with open(FileManager.FILE_NEME, "r") as file:
                data = json.load(file)
                
                for item in data:
                    products.append(Product.from_dict(item))
            
        except Exception as e:
            print("Error while loading data:", e)
            
        return products       