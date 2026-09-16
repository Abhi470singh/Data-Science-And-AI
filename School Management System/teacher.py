class Teacher:
    
    def __init__(
        self,
        teacher_id,
        name,
        subject,
        qualification,
        experience,
        salary,
        phone
        ):
        
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.qualification = qualification
        self.experience = experience
        self.salary = salary
        self.phone = phone
        
    # -----------------------------
    # Convert object To Dictionary
    #----------------------------------
    def to_dict(self):
        
        return {
            "id": self.teacher_id,
            "name": self.name,
            "subject": self.subject,
            "qualification": self.qualification,
            "experence": self.experence,
            "salary": self.salary,
            "phone": self.phone
        }
    
     # --------------------------
    # Display Teacher Details
    # --------------------------
    def display(self):

        print(f"""
        ==============================
        Teacher ID    : {self.teacher_id}
        Name          : {self.name}
        Subject       : {self.subject}
        Qualification : {self.qualification}
        Experience    : {self.experience} Years
        Salary        : {self.salary}
        Phone         : {self.phone}
        ==============================
        """)
        
        
    # ----------------------------
    # Update Subject
    # ---------------------------
    def update_salary(self, subject):
        
        self.subject = subject
        
    # ---------------------------
    # Update Salary
    # ----------------------------
    def update_salary(self,salary):
        
        self.salary = salary

    # --------------------------------
    # Update Experience
    # ----------------------------
    def update_experience(self,experience):
        
        self.experience = experience
        
    # ---------------------------------
    # Update Phone Number  
    #------------------------------------
    def update_phone(self, phone):
        
        self.phone = phone
        