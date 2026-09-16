from school import School
from utils import clear_screen, pause


def student_menu(school):

    while True:

        clear_screen()

        print("=" * 50)
        print("         STUDENT MANAGEMENT")
        print("=" * 50)

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            school.add_student()
            pause()

        elif choice == "2":
            school.display_students()
            pause()

        elif choice == "3":
            school.search_student()
            pause()

        elif choice == "4":
            school.update_student()
            pause()

        elif choice == "5":
            school.delete_student()
            pause()

        elif choice == "6":
            break
        
        else:
            print("Invalid Choice!")
            pause()


def teacher_menu(school):

    while True:

        clear_screen()

        print("=" * 50)
        print("         TEACHER MANAGEMENT")
        print("=" * 50)

        print("1. Add Teacher")
        print("2. Display Teachers")
        print("3. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            school.add_teacher()
            pause()

        elif choice == "2":
            school.display_teachers()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")
            pause()


def course_menu(school):

    while True:

        clear_screen()

        print("=" * 50)
        print("          COURSE MANAGEMENT")
        print("=" * 50)

        print("1. Add Course")
        print("2. Display Courses")
        print("3. Assign Teacher")
        print("4. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            school.add_course()
            pause()

        elif choice == "2":
            school.display_courses()
            pause()

        elif choice == "3":
            school.assign_teacher()
            pause()

        elif choice == "4":
            break

        else:
            print("Invalid Choice!")
            pause()


def report_menu(school):

    while True:

        clear_screen()

        print("=" * 50)
        print("             REPORTS")
        print("=" * 50)

        print("1. School Summary")
        print("2. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            school.school_summary()
            pause()

        elif choice == "2":
            break

        else:
            print("Invalid Choice!")
            pause()


def main():

    school = School()

    while True:

        clear_screen()

        print("=" * 60)
        print("        SCHOOL MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Course Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            student_menu(school)

        elif choice == "2":
            teacher_menu(school)

        elif choice == "3":
            course_menu(school)

        elif choice == "4":
            report_menu(school)

        elif choice == "5":

            print("\nThank You for Using School Management System.")
            break

        else:
            print("Invalid Choice!")
            pause()


if __name__ == "__main__":
    main()