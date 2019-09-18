#UPDATED ASSIGNMENT USING CHAINING

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"Hello, {self.name}! Your balance is: ${self.account_balance}")
        return self
    def transfer_money(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"Successfully transfered ${amount} into {other_user.name}")


michael = User("michael", "michael96@gmail.com")

michael.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()


chuy = User("chuy", "chuymedina96@gmail.com")

chuy.make_deposit(20).make_deposit(20).make_withdrawl(10).display_user_balance()


jovanny = User("jovanny", "test96@gmail.com")

jovanny.make_deposit(100).make_withdrawl(10).make_withdrawl(10).make_withdrawl(70).display_user_balance()

michael.transfer_money(100, chuy)








