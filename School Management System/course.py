class Course:
    
    def __init__(
        self, 
        course_id,
        course_name,
        duration,
        fee,
        teacher = "Not Assigned",
        students = None
    ):
        
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
        self.teacher = teacher
        self.students = students if students is not None else []
        
    # ----------------------------------
    # Convert Object to Dictionary
    # -----------------------------------
    def to_dict(self):
        
        return{
            "id": self.course_id,
            "course_name": self.course_name,
            "duration": self.duration,
            "fee": self.fee,
            "teacher": self.teacher,
            "students": self.students
        }
        
    # -----------------------------
    # Display Course Details
    # --------------------------------
    def display(self):
        
        print(f"""
        ==============================
        Course ID      : {self.course_id}
        Course Name    : {self.course_name}
        Duration       : {self.duration}
        Course Fee     : {self.fee}
        Teacher        : {self.teacher}
        Students Count : {len(self.students)}
        ==============================
        """)

    # --------------------
    # Assign Teacher
    # --------------------
    def assign_teacher(self, teacher_name):
        
        self.teacher = teacher_name
        
    # --------------------------
    # Enroll Student
    # ------------------------------
    def enroll_student(self, student_id):
        
        if student_id not in self.students:
            self.students.append(student_id)
            print("Student enrolled successfully,")
        else:
            print("Student is already enrolled.")
            
    # ----------------------------
    # Remove Student
    # ------------------------------
    def remove_student(self, student_id):
        
        if student_id in self.students:
            self.students.remove(student_id)
            print("Student remove successfully.")
            
        else:
            print("Student not found in this course.")
            
    # -----------------------------
    # Total Enrolled Students
    #------------------------
    def total_students(self):
        
        return len(self.students)
    



