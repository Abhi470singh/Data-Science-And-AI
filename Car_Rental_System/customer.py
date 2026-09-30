class Customer:
    
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        
    def display_customer(self):
        print("\n----- Customer Details -------")
        print(f"Customer Id : {self.customer_id}")
        print(f"Name      : {self.name}")
        print(f"Phone       : {self.phone}")
        print(f"Email      : {self.email}")
        
        
    def update_phone(self, new_phone):
        self.phone = new_phone
        print("Phone number updated successfully.")
        
    def update_email(self, new_email):
        self.email = new_email
        print("Email updated successfully.")









