from employee import FullTimeEmployee, PartTimeEmployee
from payroll import PayrollSystem
from database import Database


def main():

    payroll = PayrollSystem()
    db = Database()

    # Create database file if it doesn't exist
    db.create_database()

    # Load saved employees
    payroll.employees = db.load_data()

    while True:

        print("\n" + "=" * 50)
        print("       EMPLOYEE PAYROLL SYSTEM")
        print("=" * 50)

        print("1. Add Full-Time Employee")
        print("2. Add Part-Time Employee")
        print("3. Display All Employees")
        print("4. Search Employee")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Generate Payslip")
        print("8. Total Payroll")
        print("9. Employee Count")
        print("10. Save Data")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        # -----------------------------------------
        # Add Full-Time Employee
        # -----------------------------------------
        if choice == "1":

            emp_id = input("Employee ID: ")
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")

            basic_salary = float(input("Basic Salary: "))
            hra = float(input("HRA: "))
            da = float(input("DA: "))
            bonus = float(input("Bonus: "))
            tax = float(input("Tax: "))

            employee = FullTimeEmployee(
                emp_id,
                name,
                department,
                designation,
                basic_salary,
                hra,
                da,
                bonus,
                tax
            )

            payroll.add_employee(employee)

        # -----------------------------------------
        # Add Part-Time Employee
        # -----------------------------------------
        elif choice == "2":

            emp_id = input("Employee ID: ")
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")

            hours = float(input("Hours Worked: "))
            rate = float(input("Hourly Rate: "))

            employee = PartTimeEmployee(
                emp_id,
                name,
                department,
                designation,
                hours,
                rate
            )

            payroll.add_employee(employee)

        # -----------------------------------------
        # Display Employees
        # -----------------------------------------
        elif choice == "3":

            payroll.display_all_employees()

        # -----------------------------------------
        # Search Employee
        # -----------------------------------------
        elif choice == "4":

            emp_id = input("Enter Employee ID: ")

            employee = payroll.search_employee(emp_id)

            if employee:
                employee.display()
            else:
                print("\nEmployee Not Found.")

        # -----------------------------------------
        # Update Employee
        # -----------------------------------------
        elif choice == "5":

            emp_id = input("Enter Employee ID: ")

            payroll.update_employee(emp_id)

        # -----------------------------------------
        # Delete Employee
        # -----------------------------------------
        elif choice == "6":

            emp_id = input("Enter Employee ID: ")

            payroll.delete_employee(emp_id)

        # -----------------------------------------
        # Generate Payslip
        # -----------------------------------------
        elif choice == "7":

            emp_id = input("Enter Employee ID: ")

            payroll.generate_payslip(emp_id)

        # -----------------------------------------
        # Total Payroll
        # -----------------------------------------
        elif choice == "8":

            total = payroll.total_payroll()

            print(f"\nTotal Payroll = {total}")

        # -----------------------------------------
        # Employee Count
        # -----------------------------------------
        elif choice == "9":

            print(f"\nTotal Employees = {payroll.employee_count()}")

        # -----------------------------------------
        # Save Data
        # -----------------------------------------
        elif choice == "10":

            db.save_data(payroll.employees)

        # -----------------------------------------
        # Exit
        # -----------------------------------------
        elif choice == "11":

            db.save_data(payroll.employees)

            print("\nData Saved Successfully.")
            print("Thank You for using Employee Payroll System.")

            break

        else:
            print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()