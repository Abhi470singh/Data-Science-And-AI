import json
import os

from employee import FullTimeEmployee, PartTimeEmployee

class Database:
    
    def __init__(self, filename="employees.json"):
        self.filename = filename
        
    # ----------------------
    # Save Employees
    # ---------------------
    def save_data(self, employees):
        
        data = []
        
        for employee in employees:
            data.append(employee.to_dict())
            
        with open(self.filename, "w") as file:
            json.dump(data, file, indent = 4)
            
        print("\nEmployee data saved successfully.")
        
    # ------------------------------
    # Load Employees
    #------------------------------
    def load_data(self):
        
        employees = []
        
        if not os.path.exists(self.filename):
            return employees
        
        if os.path.getsize(self.filename) == 0:
            return employees
        
        with open(self.filename, "r") as file:
            data = json.load(file)

        for emp in data:
            
            if emp["type"] == "FullTimeEmployee":
                
                employee = FullTimeEmployee(
                    emp["emp_id"],
                    emp["name"],
                    emp["department"],
                    emp["designation"],
                    emp["basic_salary"],
                    emp["hra"],
                    emp["da"],
                    emp["bonus"],
                    emp["tax"]
                )
                
            elif emp["type"] == PartTimeEmployee:
                employee = PartTimeEmployee(
                    emp["emp_id"],
                    emp["name"],
                    emp["department"],
                    emp["designation"],
                    emp["hours_worked"],
                    emp["hourly_rate"]
                )
                
            else:
                continue
            
            employees.append(employee)
            
        return employees
    
    # --------------------------
    # Create File 
    # -----------------------------
    def create_database(self):
        
        if not os.path.exists(self.filename):
            
            with open(self.filename, "w") as file:
                json.dump([], file)
                
                print("Database Created Successfully.")
                
    # ---------------------------
    # Clear Database
    # -----------------------------
    def clear_database(self):
        
        with open(self.filename, "w") as file:
            json.dump([], file)
            
        print("database Cleared Successfully.")



