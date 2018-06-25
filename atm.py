class Atm:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.transactions = []

    def check_balance(self):
        print(f'Your account balance is ${self.balance}.')

    def deposit(self, amt):
        self.balance += amt
        self.transactions.append('User deposited ${}.'.format(amt))

    def check_withdrawl(self, amt):
        if amt < self.balance:
            return True
        else:
            print(f'Insufficient funds: ${self.balance}.')

    def withdrawl(self, amt):
        self.balance -= amt
        self.transactions.append('User withdrew ${}.'.format(amt))

    def calc_interest(self):
        print(
            f'Total accrued from interest: ${self.balance * self.interest_rate}.')

    def print_transactions(self):
        print('List of User Transactions:')
        for transaction in self.transactions:
            print(transaction)


cody = Atm()
cody.check_balance()
cody.deposit(500)
cody.deposit(150)
cody.withdrawl(200)
cody.check_withdrawl(500)
cody.deposit(300)
cody.withdrawl(200)
cody.calc_interest()
cody.print_transactions()
