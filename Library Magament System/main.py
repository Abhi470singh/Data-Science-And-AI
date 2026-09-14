from library import Library

library = Library()

while True:

    print("""
========== Library Management System ================

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

====================================================
""")

    choice = input("Enter Choice : ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")