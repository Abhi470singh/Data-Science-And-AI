from account import Account


class SavingsAccount(Account):
    
    def account_type(self):
        return "Savings"