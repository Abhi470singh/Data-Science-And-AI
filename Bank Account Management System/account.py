from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print("Amount Deposited Successfully.")
        else:
            print("Invalid Ammount")
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
            
        else:
            print("Insufficient Balance.")
            
    def display(self):
        print("\n------------------")
        print("Account No :", self.acc_no)
        print("Name       :", self.name)
        print("Balance    :",self.balance)
        
    @abstractmethod
    def account_type(self):
        pass
    
    def to_dict(self):
        return {
            "type": self.account_type(),
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance
        }
        
    @staticmethod
    def from_dict(data):
        from savings_account import SavingsAccount
        from current_account import CurrentAccount
        
        if data["type"] == "Savings":
            return SavingsAccount(
                data["acc_no"],
                data["name"],
                data["balance"]
            )
            
        return CurrentAccount(
            data["acc_no"],
            data["name"],
            data["balance"]
        )
        















