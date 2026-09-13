import json
import os
from student import Student

class StudentManager:
    
    def __init__(self):
        self.filename = "students.json"
        self.students = []
        self.load_students()
        
    def load_students(self): # file read 
        
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for s in data:
                    self.students.append(Student(**s))
                    
    def save_students(self): # save the file in json format
         
         with open(self.filename, "w") as file:
             json.dump([s.to_dict() for s in self.students], file , indent = 4)
    
    def add_student(self):  # Add the student Details
        
        roll = input("Roll No:")  # Add the user input roll no
        
        for student in self.students:
            if student.roll_no == roll:
                print("Roll No Already Exists")
                return
            
        name = input("Name :")
        age = input("Age :")
        course = input("Course : ")
        marks = input("Marks :")
        
        student = Student(roll, name, age, course, marks)
        
        # self → Refers to the current object.
        # self.students → A list store inside the object.
        # .append()  A Python list method that adds an item to the end of the list.
        # student   The object(or value) you want to add.
        
        self.students.append(student)       
                 
        self.save_students() # Save the student details in json file line 20
        
        print("Student Added Successfully.")
        
    
    def view_students(self): # View the student details
        
        if not self.students:
            print(" No Students Found.")
            return
        
        for  student in self.students:
            student.display()
            
    def search_student(self): # Search the student details byRoll No
        
        roll = input("Enter Roll Number :")
        
        for  student in self.students:
            if student.roll_no == roll: # Match the user roll to database roll_no
                student.display()
                return
            
        print("Student Not Found") # Not Match the user roll to database roll_no then print Not Found
        
    def update_student(self): # Update the student details by Roll No By chance Change the course ya any thing
        
        roll = input("Enter Roll Number :")
        
        for  student in self.students:
            
            if student.roll_no == roll:
                
                student.name = input("new Nmae :")
                student.age = int(input("New Age :"))
                student.course = input("New Course :")
                student.marks = float(input("New Marks :"))
                
                self.save_students()
                
                print("Update Successfully")
                
                return
        print("student Not Found") 
        
        def delete_student(self):
            
            roll = input("Enter the Roll No :")
            
            for student in self.students:
                
                 if student.roll_no == roll:
                    self.students.remove(student)
                    self.save_students() 
                    
                    print("Delete Successfully")
                    return
                
            print("student Not Found") 
                      








