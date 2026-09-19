class Supplier:
    def __init__(self, supplier_id, name, phone, email, address):
        self.supplier_id = supplier_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
# Display Supplier Details:

    def display(self):
        print("_" * 40)
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Name       : {self.name}")
        print(f"Phone      : {self.phone}")
        print(f"Email      : {self.email}")
        print(f"Address     : {self.address}")
        print("-" *50)
        
# Update supplier Datails:

    def update_supplier(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone 
        if email:
            self.email = email
        if address:
            self.address = address
            
# Convert Object ti dictionary (for JSON)
 
    def to_dict(self):
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }
        
# Create Supplier object from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["supplier_id"],
            data["name"],
            data["phone"],
            data["email"],
            data["address"]
        )
        
# String representation of the Supplier object

    def __str__(self):
        return (
            f"ID: {self.supplier_id} | "
            f"Name: {self.name} | "
            f"Phone: {self.phone}"
        )