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
        print(self.account_balance)
        return self
    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= self.account_balance - amount
    #     self.other_user = self.other_user + amount


michael = User("michael", "michael96@gmail.com")

michael.make_deposit(100)
michael.make_deposit(100)
michael.make_deposit(100)
michael.make_withdrawl(50)
michael.display_user_balance()


chuy = User("chuy", "chuymedina96@gmail.com")


chuy.make_deposit(20)
chuy.make_deposit(20)
chuy.make_withdrawl(10)
chuy.display_user_balance()


jovanny = User("jovanny", "test96@gmail.com")

jovanny.make_deposit(100)
jovanny.make_withdrawl(10)
jovanny.make_withdrawl(10)
jovanny.make_withdrawl(70)
jovanny.display_user_balance()

# michael.transfer_money(chuy, 100)





