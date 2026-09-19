class Product:
    
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        
# Display product details:

    def display(self):
        print("-" *40)
        print(f"Product_ID: {self.product_id}")
        print(f"Name      : {self.name}")
        print(f"Price   : {self.price}")
        print(f"Quantity   : {self.quantity}")
        print("_" * 40)
        
# Add stock to the product:

    def add_stock(self, qty):
        if qty > 0:
            self.quantity += qty
            print(f"{qty} units added successfully.")
        else:
            print("Invalid quantity.")
            
# Sell Product

    def sell_product(self, qty):
        if qty <=0:
            print("Invalid Quantity.")
        elif qty > self.quantity:
            print("Insufficent stock available.")
        else:
            self.quantity -= qty
            total = qty * self.price
            print(f"{qty} units sold successfully.")
            print(f"Total Bill : ₹{total:.2f}")
            
# Update product Details:

    def update_product(self, name=None, price=None, quantity=None):
        if name:
            self.name = name
        if price is not None and price > 0:
            self.price = float(price)
        if quantity:
            self.quantity = quantity
            
# Convert object to dictionary (for json)
  
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
        
# Create Product object from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["quantity"]
        )
        
# String representation

    def __str__(self):
        return (
            f"ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Price: ₹{self.price:.2f} | "
            f"Stock: {self.quantity}"
        )