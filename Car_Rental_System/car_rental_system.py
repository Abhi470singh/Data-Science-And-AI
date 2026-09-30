from car import Car
from customer import Customer
from rental import Rental

class CarRentalSystem:
    
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []
        
        
    # --------------------------
    # Car Management
    # --------------------------
    
    def add_car(self, car):
        self.cars.append(car)
        print("car added successfully.")
        
    def show_cars(self):
        print("\n====== Car List ======")
        
        if not self.cars:
            print("No cars available.")
            return
        
        for car in self.cars:
            car.display_car()
            
    def find_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
            
        return None
    
    # -------------------------------
    # Customer Management
    # ------------------------------
    
    def add_customer(self, customer):
        self.customer.append(customer)
        print("Customer added successfully.")
        
    def show_customer(self):
        print("\n===== CUSTOMER LIST ======")
        
        if not self.customers:
            print("No customers found.")
            return
        
        for customer in self.customers:
            customer.display_customer()
            
    def find_customer(self, customer_id):
        for customer in self.custumers:
            if customer.customer_id == customer_id:
                return customer
            
        return None
    
    
    # ------------------------
    # Rental Managemenat
    # -----------------------
    
    def rent_car(self, rental_id, customer_id, car_id, days):
        
        customer = self.find_customer*customer_id
        car  = self.find_car(car_id)
        
        
        # Check customer
        if customer is None:
            print("Customer not found.")
            return
        
        # Check Car
        if car is None:
            print("Car not Found")
            return
        
        # Check Days
        if days<= 0:
            print("Rental days must be greater than 0.")
            return
        
        # MArk car as rented
        car.rent_car()
        
        
        # Create rebtal Object
        rental = Rental(
            rental_id, 
            customer,
            car,
            days
        )
        
        self.rentals.append(rental)

        print("\nCar rented successfully!")
        rental.display_rental()
        
    #  ---------------------------------
    # Return Car
    # ------------------------------------
    
    def return_car(self,car_id):
        
        car = self.find_car(car_id)
        
        
        if car is None:
           print("Car not Found.")
           return
       
       
       
        if car.is_available:
            print("This car is already available.")
            return
        
        car.return_car()
        
        print(
            f"\n{car.brand} {car}"
            "returned successfully."
        )  
        
    # ------------------------
    # Rental REcords
    # -------------------------
    
    def show_rentals(self):
        
        
        print("\n ======== RENTAL RECORDS ======")
        
        if not self.rentals:
            print("No rental records found.")
            return
        
        for rental in self.rentals:
            rental.display_rental()
                   






