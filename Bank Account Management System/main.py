from bank import Bank

bank = Bank()


while True:
    
    print("\n======BANK MANAGEMENT SYSTEM =======")
    
    print("1. create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Search Account")
    print("5. Display All Accounts")
    print("6. Delete Account")
    print("7. Exit")
    
    
    choice = input("Enter Choice : ")
    
    if choice == "1":
        bank.create_account()
        
    elif choice == "2":
        bank.deposit()
        
    elif choice == "3":
        bank.withdraw()
        
    elif choice == "4":
        bank.display_account()
        
    elif choice == "5":
        bank.display_all()    
            
    elif choice =="6":
        bank.delete_account()
     
    elif choice == "7":
        print("Thank You!")
        break
    
    else:
        print("Invalid Choice")    
        
        