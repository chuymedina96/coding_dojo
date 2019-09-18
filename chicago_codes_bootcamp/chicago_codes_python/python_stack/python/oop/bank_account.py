class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.account_balance = balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance > 0:
            self.account_balance -= amount
        else:
            self.account_balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info(self):
        print("Hello there, your current balance is:" ,self.account_balance)
        print("Hello, you're interest rate is:", self.int_rate)

    def yield_interest(self):
        if self.account_balance > 0:
            stuff = self.account_balance + self.account_balance * self.int_rate
            self.account_balance = stuff

        return self

account1 = BankAccount(0.04, 0)
account2 = BankAccount(0.02, 0)

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

account2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(40).yield_interest().display_account_info()



        