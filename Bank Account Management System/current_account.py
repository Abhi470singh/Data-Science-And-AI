from account import Account

class CurrentAccount(Account):
    
    def account_type(self):
        return "Current"