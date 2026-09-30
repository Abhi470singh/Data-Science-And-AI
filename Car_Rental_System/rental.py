class Rental:
    
    def __init__(self, rental_id, customer, car, days):
        self.rental_id = rental_id
        self.customer = customer
        self.car = car
        self.days = days
        
        # Calculate total amount
        self.total_amount = self.car.rent_per_day * self.days
        
    def calculate_total(self):
        self.total_amount = self.car.rent_per_day * self.days
        return self.total_amount
    
    
    def display_rental(self):
        print("\n----- Rental Details ------")
        print(f"Rental ID   : {self.rental_id}")
        print(f"Customer     : {self.customer.name}")
        print(f"Car    : {self.car.brand} {self.car.model}")
        print(f"Days     : {self.days}")
        print(f"Rent/Day    : ₹{self.car.rent_per_day}")
        print(f"Total Amount: ₹{self.total_amount}")
        
        
    def update_days(self, new_days):
        if new_days > 0: 
            self.days = new_days 
            self.calculate_total() 
            print("Rental days updated successfully.") 
        else: 
            print("Days must be greater than 0.")









