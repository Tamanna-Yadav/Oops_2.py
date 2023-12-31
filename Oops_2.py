# 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Ashish", 5000, 5)
print("Account title:",account1.title)  
print("Account balance:",account1.balance)  
print("Account interest:",account1.interestRate)  

# output  # Ashish is the title and 5000 is the balance and 5 is the interestRate.
#Ashish
#5000
#5

# 5: Handling a Bank Account

class account:
    def __init__(self, balance):
        self.balance = balance
        
    def getbalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount

class savingsaccount(account):
    def __init__(self, balance, interestrate):
        super().__init__(balance)
        self.interestrate = interestrate
    
    def interestAmount(self):
        interest = self.balance * (self.interestrate/100)
        self.balance += interest
        return interest

balance_1 = int(input("Enter initial balance for account 1: "))
deposit = int(input("Enter deposit amount: "))
balance_2 = int(input("Enter initial balance for account 2: "))
withdrawal = int(input("Enter withdrawal amount: "))
interest_rate = int(input("Enter interest rate: "))

account_1 = account(balance_1)
account_1.deposit(deposit)
print("Balance for account 1 after deposit:", account_1.getbalance())

account_2 = account(balance_2)
account_2.withdrawal(withdrawal)
print("Balance for account 2 after withdrawal:", account_2.getbalance())

savings_account = savingsaccount(balance_1, interest_rate)
interest_earned = savings_account.interestAmount()
print("Total interest:", interest_earned)