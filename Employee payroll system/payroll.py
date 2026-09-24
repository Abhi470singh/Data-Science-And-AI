from employee import FullTimeEmployee, PartTimeEmployee

class PayrollSystem:
    
    def __init__(self):
        
        self.employee = []
        
    # ----------------------
    # Add Employee
    #-----------------------
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print("\nEmployee Added Successfully!")
        
        
    # -----------------------
    # Display AAll Employees
    # -----------------------
    
    def display_all_employees(self):
        
        if len(self.employees) == 0:
            print("\nNo Employee Found.")
            return
        
        print("\n=========Employee List =========")
    
        for emp in self.employees:
            emp.display()
            print("-" * 50)
        
        
    # ------------------------------
    # search Employee
    #-------------------------------
    def search_employee(self, emp_id):
        
        for emp in self.employees:
            
            if emp.emp_id == emp_id:
                return emp
            
        return None
    
    # ----------------------------
    # Delete Employee
    # ----------------------------
    def delete_employee(self, emp_id):
        
        employee = self.search_employee(emp_id)
        
        if employee:
            
            self.employees.remove(employee)
            print("\nEmployee Deleted Successfully!")
            
        else:
            
            print("\nEmployee Not Found")
            
            
    # -------------------------------
    # Update Employee
    # -------------------------------
    def update_employee(self, emp_id):
        
        employee = self.search_employee(emp_id)
        
        if employee is None:
            print("\nEmployee Not Found!")
            return
        print("\nLeave blank to keep old value. ")
        
        name = input(f"Name ({employee.name}) : ")
        
        department = input(
            f"Department ({employee.department}) :" 
        )
        
        designation = input(
            f"Designation ({employee.designation}) :"
        )
        
        if name:
            employee.name = name
            
        if department:
            employee.department = department
            
        if designation:
            employee.designation = designation
            
        if isinstance(employee, FullTimeEmployee):
            
            value = input(
                f"Basic Salary ({employee.basic_salary}) :"
            )    
        
            if value:
                employee.basic_salary = float(value)
            
            value = input(
            f"HRA ({employee.hra}) : "
            )  
        
            if value:
                employee.hra = float(value)
            
            value = input(
                f"DA ({employee.da}) : "
            )
            
            if value:
                employee.da = float(value)
                
            value = input(
                f"Bonus ({employee.bonus}) : "
            )
            
            if value:
                employee.bouns = float(value)
                
            value = input(
                f"tax ({employee.tax}) : "
            )
            
            if value:
                employee.tax = float(value)
                
        elif isinstance(employee, PartTimeEmployee):
            
            value = input(
                f"Hours Worked ({employee.hours_worked}) : "
            )
            
            if value:
                employee.hours_worked = float(value)
                
            value = input(
                f"Hourly Rate ({employee.hourly_rate}) : "
            )
            
            if value:
                employee.hourly_rate = float(value)
                
        print("\nEmployee Updated Successfully!")
        
    # -----------------------------
    # Generate Payslip
    # ------------------------------
    def generate_payslip(self, emp_id):
        
        employee = self.search_employee(emp_id)
        
        if employee is None:
            print("\nEmployee Not Found!")
            return
        
        print("\n")
        print("=" * 45)
        print("        EMPLOYEE PAYSLIP")
        print("=" * 45)
        
        print(f"Employee ID : {employee.emp_id}")
        print(f"Name        : {employee.name}" )
        print(f"Department  : {employee.department}")
        print(f"Designation : {employee.designation}")
    
    
        if isinstance(employee, FullTimeEmployee):
            
            gross, net = employee.calculate_salary()
            
            print(f"Basic Salary : {employee.basic_salary}")
            print(f"HRA          : {employee.hra}")
            print(f"DA           : {employee.da}")
            print(f"Bonus        : {employee.bonus}")
            print(f"Tax          : {employee.tax}")
            print(f"Gross Salary : {gross}")
            print(f"Net Salary   : {net}")
            
        elif isinstance(employee, PartTimeEmployee):
            
            salary = employee.calculate_salary()
            
            print(f"Hours Worked : {employee.hours_worked}")
            print(f"Hourly Rate  : {employee.hourly_rate}")
            print(f"Salary       : {salary}")
            
        print("=" * 45)
        
    # ---------------------
    # Total Payroll
    # ------------------
    def total_payroll(self):
        
        total = 0 
        
        for emp in self.employees:
            
            if isinstance(emp, FullTimeEmployee):
                
                gross, net = emp.calculate_salary()
                total += net
                
            elif isinstance(emp, PartTimeEmployee):
                total += emp.calculate_salary()
                
        return total
    
    # --------------------------
    # Employee Count
    # --------------------------
    def employee_count(self):
        
        return len(self.employee)         
            
            
        