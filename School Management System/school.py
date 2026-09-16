from utils import *
from database import Database

class School:

    def __init__(self):
        
        self.db = Database()
         
        self.student_file = "data/students.json"
        self.teacher_file = "data/teachers.json"
        self.course_file = "data/courses.json"

        self.students = load_json(self.student_file)
        self.teachers = load_json(self.teacher_file)
        self.courses = load_json(self.course_file)

    # ==============================
    # Student Functions
    # ==============================

    def add_student(self):

        title("ADD NEW STUDENT")

        student = {
            "id": generate_id(self.students, "S"),
            "name": input_string("Enter Name : "),
            "age": input_age(),
            "class": input_string("Enter Class : "),
            "section": input_string("Enter Section : "),
            "phone": input_phone(),
            "attendance": 0,
            "marks": {},
            "fee": 0
        }

        self.students.append(student)
        save_json(self.student_file, self.students)

        print("\nStudent Added Successfully.")
        print("Student ID :", student["id"])

    def display_students(self):

        title("ALL STUDENTS")

        if not self.students:
            print("No Student Found.")
            return

        for student in self.students:

            print(f"""
            ID         : {student['id']}
            Name       : {student['name']}
            Age        : {student['age']}
            Class      : {student['class']}
            Section    : {student['section']}
            Phone      : {student['phone']}
            Attendance : {student['attendance']}%
            Fee        : {student['fee']}
            """)
            line()

    def search_student(self):

        title("SEARCH STUDENT")

        student_id = input("Enter Student ID : ").upper()

        student = search_by_id(self.students, student_id)

        if student:

            print("\nStudent Found\n")

            for key, value in student.items():
                print(f"{key} : {value}")

        else:
            print("Student Not Found.")

    def delete_student(self):

        title("DELETE STUDENT")

        student_id = input("Enter Student ID : ").upper()

        student = search_by_id(self.students, student_id)

        if student:

            self.students.remove(student)
            save_json(self.student_file, self.students)

            print("Student Deleted Successfully.")

        else:
            print("Student Not Found.")

    def update_student(self):

        title("UPDATE STUDENT")

        student_id = input("Enter Student ID : ").upper()

        student = search_by_id(self.students, student_id)

        if student:

            student["name"] = input_string("Enter New Name : ")
            student["age"] = input_age()
            student["class"] = input_string("Enter Class : ")
            student["section"] = input_string("Enter Section : ")
            student["phone"] = input_phone()

            save_json(self.student_file, self.students)

            print("Student Updated Successfully.")

        else:
            print("Student Not Found.")

    # ==============================
    # Teacher Functions
    # ==============================

    def add_teacher(self):

        title("ADD TEACHER")

        teacher = {

            "id": generate_id(self.teachers, "T"),
            "name": input_string("Enter Name : "),
            "subject": input_string("Enter Subject : "),
            "qualification": input_string("Qualification : "),
            "experience": input_int("Experience (Years) : "),
            "salary": input_float("Salary : "),
            "phone": input_phone()

        }

        self.teachers.append(teacher)
        save_json(self.teacher_file, self.teachers)

        print("Teacher Added Successfully.")

    def display_teachers(self):

        title("ALL TEACHERS")

        if not self.teachers:
            print("No Teacher Found.")
            return

        for teacher in self.teachers:

            print(f"""
            ID            : {teacher['id']}
            Name          : {teacher['name']}
            Subject       : {teacher['subject']}
            Qualification : {teacher['qualification']}
            Experience    : {teacher['experience']}
            Salary        : {teacher['salary']}
            Phone         : {teacher['phone']}
            """)
            line()

    # ==============================
    # Course Functions
    # ==============================

    def add_course(self):

        title("ADD COURSE")

        course = {

            "id": generate_id(self.courses, "C"),
            "course_name": input_string("Course Name : "),
            "teacher": "",
            "duration": input_string("Duration : "),
            "fee": input_float("Course Fee : ")

        }

        self.courses.append(course)

        save_json(self.course_file, self.courses)

        print("Course Added Successfully.")

    def display_courses(self):

        title("ALL COURSES")

        if not self.courses:
            print("No Course Found.")
            return

        for course in self.courses:

            print(f"""
            Course ID   : {course['id']}
            Course Name : {course['course_name']}
            Teacher     : {course['teacher']}
            Duration    : {course['duration']}
            Fee         : {course['fee']}
            """)
            line()

    # ==============================
    # Assign Teacher
    # ==============================

    def assign_teacher(self):

        title("ASSIGN TEACHER")

        course_id = input("Enter Course ID : ").upper()

        course = search_by_id(self.courses, course_id)

        if not course:
            print("Course Not Found.")
            return

        teacher_id = input("Enter Teacher ID : ").upper()

        teacher = search_by_id(self.teachers, teacher_id)

        if not teacher:
            print("Teacher Not Found.")
            return

        course["teacher"] = teacher["name"]

        save_json(self.course_file, self.courses)

        print("Teacher Assigned Successfully.")

    # ==============================
    # School Summary
    # ==============================

    def school_summary(self):

        title("SCHOOL SUMMARY")

        print("Total Students :", len(self.students))
        print("Total Teachers :", len(self.teachers))
        print("Total Courses  :", len(self.courses))
        