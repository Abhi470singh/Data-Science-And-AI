from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract Base Class for Employee
    """
    
    def __init__(self, emp_id, name, department, designation):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        
    @abstractmethod
    def calculate_salary(self):
        
        pass
    
    def display(self):
        print("\nEmployee Details")
        print("-" * 40)
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Designation : {self.designation}")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
        }
        
        
class FullTimeEmployee(Employee):
    
    def __init__(
        self,
        emp_id,
        name,
        department,
        designation,
        basic_salary,
        hra,
        da,
        bonus,
        tax,
    ):
        super().__init__(emp_id, name, department, designation)
        
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.bonus = bonus
        self.tax = tax
        
        
    def calculate_salary(self):
        gross = (
            self.basic_salary
            + self.hra
            + self.da
            + self.bonus
        )
        
        net = gross - self.tax
        
        return gross, net
    
    def display(self):
        super().display()
        
        
        gross, net = self.calculate_salary()
        
        print(f"Basic Salary : {self.basic_salary}")
        print(f"HRA          : {self.hra}")
        print(f"DA           : {self.da}")
        print(f"Bonus        : {self.bonus}")
        print(f"Tax          : {self.tax}")
        print(f"Gross Salary : {gross}")
        print(f"Net Salary   : {net}")
        
    def to_dict(self):
            
        data = super().to_dict()
            
        data.update(
            {
            "basic_salary": self.basic_salary,
            "hra": self.hra,
            "da": self.da,
            "bonus": self.bonus,
            "tax": self.tax,
            }
        )
        
        
        return data
    
class PartTimeEmployee(Employee):
    
    def __init__(
        self,
        emp_id,
        name,
        department,
        designation,
        hours_worked,
        hourly_rate,
    ):
        
        super().__init__(
            emp_id,
            name,
            department,
            designation,
        )
        
        
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
        
        salary = self.hours_worked * self.hourly_rate
        
        return salary
    
    
    def display(self):
        
        super().display()
        
        print(f"Hours Worked :{self.hours_worked}")
        print(f"Hourly Rate : {self.hourly_rate}")
        print(f"Salary   : {self.calculate_salary()}")
        
        
    def to_dict(self):
        
        data = super(). to_dict()
        
        data.update(
            {
            "hours_worked": self.hours_worked,
            "hourly_rate": self.hourly_rate,
            }
        )
        
        return data





