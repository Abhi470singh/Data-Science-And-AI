import json
import os

class Database:
    
    def __init__(self):
        
        self.student_file = "data/students.json"
        self.teacher_file = "data/teachers.json"
        self.course_file = "data/courses.json"
        
        self.create_database()
        
    # ---------------------------
    # Create Json file if they don't exist
    # ----------------------------
    def create_database(self):
        
        files = [
            self.student_file,
            self.teacher_file,
            self.course_file,
        ]        
        
        # Create data folder
        os.makedirs("data", exist_ok=True)
        
        # create empty JSON files
        for file in files:
            
            if not os.path.exists(file):
                
                with open(file, "w") as f:
                    json.dump([], f, indent=4)
                    
    # ----------------------------
    # load Data
    # ---------------------------
    def load_data(self, filename):
        
        try:
            with open(filename, "r") as file:
                return json.load(file)
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    # ----------------------------
    # Save Data
    # --------------------------
    def seve_data(self, filename, data):
        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
            
    # ------------------------
    # Student data
    # --------------------------
    def load_students(self):
        return self.load_data(self.student.file)
    
    def save_students(self, students):
        self.save_data(self.student_file, students)
        
    # ----------------------------
    # teacher Data
    #------------------------------
    def load_teacher(self):
        return self.load_data(self.teacher_file)
    
    def save_teachers(self, teachers):
        self.save_data(self.teacher_file, teachers)
        
    # -----------------------------
    # Course Data
    # --------------------------
    def load_courses(self):
        return self.load_data(self.course_file)
    
    def save_courses(self, courses):
        self.save_data(self.course_file, courses)
                    