import json
import os

from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount

class Bank:
    
    def __init__(self):
        self.accounts = []
        self.filename = "accounts.json"
        self.load_accounts()
    
    
    # -------------------
    # Load
    # -------------------
    def load_accounts(self):
        
        if os.path.exists(self.filename):
            
            with open(self.filename, "r") as file:
                data = json.load(file)
                
            self.accounts = [
                Account.from_dict(acc)
                for acc in data
            ]

    # --------------------
    # Save
    # --------------------
    def save_accounts(self):
        
        with open(self.filename, "w") as file:
            json.dump(
                [acc.to_dict() for acc in self.accounts],
                file,
                indent=4
            )
    #---------------------
    # Create Account
    # ---------------------
    def create_account(self):
           
        acc_no = input("Account Number :")
        
        if self.search_account(acc_no):
            print("Account Already Exists.")
            return
        
        name = input("Customer Name :")
        
        balance = float(input("Opening Balance :"))
        
        print("1. Savings")
        print("2. Current")
        
        choice = input("Choose Account Type : ")
        
        if choice == "1":
            account = SavingsAccount(acc_no, name, balance)
        else:
            account = CurrentAccount(acc_no, name, balance)
            
        self.accounts.append(account)
        
        self.save_accounts()
        
        print("Account Created Successfully.")
        
    # --------------------
    # Search
    # -------------------
    def search_account(self, acc_no):
        
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
            
        return None
    
    # ----------------
    # Deposit
    # ----------------
    
    def deposit(self):
        
        acc = input("Account Number : ")
        
        account = self.search_account(acc)
    
    
        if account:
            amount = float(input("Amount : "))
            account.deposit(amount)
            self.save_accounts()
            
        else:
            print("Account Not Found")
            
    # ---------------
    # Withdraw
    # ---------------
    def withdraw(self):
        
        acc = input("Account Number :" )
        
        account = self.search_account(acc)
        
        if account:
            amount = float(input("Amount : "))
            account.withdraw(amount)
            self.save_accounts()
            
        else:
            print("Account Not Found.")
    # -----------------
    # Display
    # ------------------
    def display_account(self):
        
        acc = input("Account number :")
        
        account = self.search_account(acc)
        
        if account:
            account.display()
            
        else:
            print("Account Not Found.")
                   
    # -----------------
    # Display All
    # -----------------
    def display_all(self):
        
        if not self.accounts:
            print("No Account Available.")
            return
        
        for acc in self.accounts:
            acc.display()
            
    # -----------------
    # Delete
    # -----------------
    def delete_accounts(self):
        
        acc = input("Account Number : ")
        
        account = self.search_account(acc)
        
        if account:
            self.accounts.remove(account)
            self.save_accounts()
            print("Account Deleted Successfull.")
        else:
            print("Account Not Found.")
            
            
            
                   
            
    