class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self, balance):
            self.account_balance = balance


michael = User("michael", "michael96@gmail.com")

michael.make_deposit(100)
michael.make_deposit(100)
michael.make_deposit(100)
michael.make_withdrawl(50)
print(michael.account_balance)


chuy = User("chuy", "chuymedina96@gmail.com")

print(chuy.account_balance)
chuy.make_deposit(20)
chuy.make_deposit(20)
chuy.make_withdrawl(10)
print(chuy.account_balance)


jovanny = User("jovanny", "test96@gmail.com")

jovanny.make_deposit(100)
jovanny.make_withdrawl(10)
jovanny.make_withdrawl(10)
jovanny.make_withdrawl(70)
print(jovanny.account_balance)



