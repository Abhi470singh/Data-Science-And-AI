from hospital import Hospital


def main():
    hospital = Hospital()

    while True:
        print('\\n===== HOSPITAL MANAGEMENT SYSTEM =====')
        print('1. Add Patient')
        print('2. View Patients')
        print('3. Search Patient')
        print('4. Delete Patient')
        print('5. Add Doctor')
        print('6. View Doctors')
        print('7. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            hospital.add_patient()

        elif choice == '2':
            hospital.view_patients()

        elif choice == '3':
            hospital.search_patient()

        elif choice == '4':
            hospital.delete_patient()

        elif choice == '5':
            hospital.add_doctor()

        elif choice == '6':
            hospital.view_doctors()

        elif choice == '7':
            print('Thank you for using the system!')
            break

        else:
            print('Invalid choice! Please try again.')


if __name__ == '__main__':
    main()