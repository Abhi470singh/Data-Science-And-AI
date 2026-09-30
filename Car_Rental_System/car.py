class Car:
    def __init__(self, car_id, brand, model, rent_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.is_available = True
        
    def display_car(self):
        status = "Available" if self.is_available else "Rented"
        
        print(f"Car ID      : {self.car_id}")
        print(f"Brand        : {self.brand}")
        print(f"Model       : {self.model}")
        print(f"Rent/Day     : ₹{self.rent_per_day}")
        print(f"Status      : {status}")
        print("-" * 30)
        
    def rent_car(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
        
    def return_car(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False














