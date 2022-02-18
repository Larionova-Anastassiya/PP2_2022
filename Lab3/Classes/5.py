#Create a bank account class that has attributes ownerbalance,
# and two methods depositwithdraw and .
# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def depositwithdraw(self, deposit):

        self.balance = self.balance + deposit
        print(f'Your balance has changed {self.balance}, you have deposited to the account {deposit} ')

    def Withdrawals(self, withdraw):

        if withdraw > self.balance:
            print(f'You have only {self.balance} in your account')
        else:
            self.balance = self.balance - withdraw
            print(f'Your balance has changed {self.balance}')


print("What is you name?")
name = input()
print("Your balance:")
balance = int(input())
ans = Account(name, balance)

while ans != 0:
    print("\n What operation? \n"
        "№ deposit \n"
        "№ withdraw \n")
    operation = input()
    if operation == "deposit":
        print("Enter the amount to top up:")
        deposit = int(input())
        ans.depositwithdraw(deposit)
    elif operation == "withdraw":
        print("Enter the amount to withdraw from the account: ")
        withdraw = int(input())
        ans.Withdrawals(withdraw)

#бесконечно можно вводить операции ввода и вывода средств