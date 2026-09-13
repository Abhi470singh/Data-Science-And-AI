class Student:
    def __init__(self, roll_no, name, age, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
        
        # roll_no → temporary input parameter.
        # self.roll_no → permanent attribute stored in the object.
    def display(self):
        print("_" * 40)
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        
    def to_dict(self):
        
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
            }    
    
        
        


















