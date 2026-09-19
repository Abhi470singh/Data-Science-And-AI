class Customer:
    def __init__(self,customer_id, name, phone, email, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
# Display  Customer Details

    def display(self):
        print("-" * 50)
        print(f"Customer ID: {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Phone      : {self.phone}")
        print(f"Email      : {self.email}")
        print(f"Address     : {self.address}")
        print("=" * 50)
        
        
# Update Custumer Datails

    def update_customer(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
            
# Convert Object to Dictinory (for JSON)

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone, 
            "email": self.email,
            "address": self.address
        }
        
# Create Customer object from dictionary
    @classmethod
    def from_dist(cls, data):
        return cls(
            data["custumer_id"],
            data["name"],
            data["phone"],
            data["email"],
            data["address"]
        )
        
# String Representation

    def __str__(self):
        return (
            f"ID: {self.custumer_id} |"
            f"Name: {self.name} | "
            f"Phone: {self.phone} |"
        )
        