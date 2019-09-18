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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance= 0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"Successfully transfered {amount} into {other_user.name}")

user1 = User("Chuy", "chuy96@gmail.com")

user1.make_deposit(100).display_user_balance().make_withdraw(80).display_user_balance()

# user1.display_user_balance()
# account1 = BankAccount(int_rate = 0.03, balance=0)
# user1.account = account1






