from car import Car
from customer import Customer
from car_rental_system import CarRentalSystem

"""class CarRentalSystem:
    
    def __init__(self):
        self.car = []
        self.customers = []
        self.rentals = []
        
        # ------------------------
        # Car Management System
        # ---------------------------
        
    def add_car(self, car):
        self.cars.append(car)
        print("car Added successfully.")
        
    def show_cars(self):
        print("\n==== CAR LIST =====")
        
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
    
    # ----------------------------
    # Customer Management
    # -----------------------------
    
    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer added successfully.")
        
    def show_customers(self):
        print("\n====== CUSTOMER LIST ======")
        
        if not self.customers:
            print("No customers found.")
            return
        
        for customer in self.customers:
            customer.display_customer()
            
    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
            
        return None"""
    
# create Car Rental System object
system =  CarRentalSystem()

# --------------------------
# Add Some Default Cars
# ---------------------------

system.add_car(Car(101, "Toyota", "Fortuner", 3000))
system.add_car(Car(102, "Hyundai", "Creta", 2000))
system.add_car(Car(103, "Tata", "Nexon", 1500))
system.add_car(Car(104, "Mahindra", "Thar", 2500))

# -----------------------------------------------
# Add Same Deafault Customers
# ---------------------------------------

system.add_customer(
    Customer(
        1, 
        "Abhishek Kumar",
        "625988470"
        "abhishek@gmail.com"
    
    )
)   

system.add_customer(
    Customer(
        2, 
        "Rahul Kumar",
        "9430288336",
        "rahulkumar@gmail.com"
        
    )
)     

# -------------------------
# Main Menu
# ---------------------------

while True:
    
    print("\n")
    print("=" * 40)
    print("      CAR RENTAL SYSTEM")
    print("=" * 40)
    
    print("1. Show Cars")
    print("2. Show Customers")
    print("3. Add Customer")
    print("4. Rent Car")
    print("5. Return Car")
    print("6. Show Rental Recodes")
    print("7. Exit")
    
    print("=" * 40)
    
    choice = input("Enter your choice: ")
    
    # --------------
    # Show Car
    # ---------------
    
    if choice == "1":
        
        system.show_cars()
        
    # ---------------------
    # Show Customers
    # -------------------------
    
    elif choice == "2":
        
        system.show_customers()
        
    # ------------------------------
    # Add Customer
    # ------------------------------
    elif choice == "3":
        
        try:
            customer_id = int(
                input("Enter Customer ID:")
            )                 
            
            name = input(
            "Enter Customer Name:"
            )
        
            phone = input(
            "Enter Phone Number:"
            )
                
            email = input(
            "Enter Email:"
            )
        
            customer = Customer(
            customer_id,
            name,
            phone, 
            email
            )
        
            system.add_customer(customer)
            
        except ValueError:
            print("Please enter a valid Customer ID.")
            
    # ---------------------------
    # Rent Car
    # ---------------------------
    
    elif choice =="4":
        
        try:
            rental_id = int(
                input("Enter Rental ID:")
            )    
            
            customer_id = int(
                input("Enter Customer ID:")
            )
            
            car_id = int(
                input("Enter Car ID:")
            )
            
            days = int(
                input("Enter Nubmer Of Days:")
            )
            
            system.rent_car(
                rental_id,
                customer_id,
                car_id,
                days
            )
        
        except ValueError:
            print("Please Enter valid numbers.")
            
    # ------------------------------
    # Return Car
    # --------------------------------
    elif choice =="5":
        
        try:
            car_id = int(
                input("Enter Car ID")
            )
            
            system.return_car(car_id)
            
        except ValueError:
            print("Please entyer a valid Car ID.")
            
    # ------------------------------
    # Show Rental Records
    # -------------------------------
    
    elif choice == "6":
        
        system.show_rentals()
        
    # ---------------
    # Exits
    #--------------------
    
    elif choice == "7":
        
        print("\nthank you for using")
        print("Car Rental System!")
        
        break
    
    # -----------------------
    # Invalid Choice
    # ---------------------
    
    else:
        print(
            "\n Invalid choice!"
            "please Selecet 1-7"
        )
            
        









