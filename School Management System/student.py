class Student:
    
    def __init__(
        self,
        student_id,
        name,
        age,
        student_class,
        section,
        phone,
        attendance = 0,
        marks=None,
        fee=0
    ):
        
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.section = section
        self.phone = phone
        self.attendance = attendance
        self.marks = marks if marks is not None else {}
        self.fee = fee
        
        
    # ------------------------------
    # Convert Object to Dictionary
    # ------------------------------
    def to_dict(self):
        
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "class": self.student_class,
            "section": self.section,
            "phone": self.phone,
            "attendance": self.attendance,
            "marks": self.marks,
            "fee": self.fee
        }
        
    # ----------------------------
    # Display Student Details
    # ----------------------------
    def display(self):
        
        print(f"""
        ===========================
        Student ID : {self.student_id}
        Name       : {self.name}
        Age        : {self.age}
        Class      : {self.student_class}
        Section    : {self.section}
        Phone      : {self.phone}
        Attendance : {self.attendance}
        Fee        : {self.fee}
        """)
        
    # -----------------------
    # Add \ Update marks
    # ----------------------
    def add_marks(self, subject, marks):
        
        self.marks[subject] = marks
        
    # -----------------------------
    # Calculate Grade
    # ------------------------------
    def calculate_grade(self):
        
        percentage = self.calculate_percentage()
        
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >=70:
            return "B"
        elif percentage >=60:
            return "C"
        elif percentage >=50:
            return "D"
        else:
            return "Fail"
        
    # ---------------------------
    # Update Attendance
    # ----------------------------
    def update_attendance(self, attendance):
        
        if 0 <= attendance <= 100:
            self.attendance = attendance
            
    # ------------------------------
    # Fee
    # ---------------------------
    def pay_fee(self, amount):
        
        self.fee += amount
            



