###########################################################################################################################################
# PYTHON BANK APP (OOP)
###########################################################################################################################################

# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod


# Class Bank (Abstract Bank Class)
class Bank(ABC):

    def basicinfo(self):
        print('This is a generic bank')
        return 'Generic bank: 0'

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


# Class Swiss (A specific type of bank than derives from class Bank)
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1_000

    def basicinfo(self):
        print('\n')
        print('This is your current Swiss Bank account')
        return f'Swiss Bank Amount: ${self.bal}'

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Withdrawn amount: ${amount}')
            print(f'New balance: ${self.bal}')
        else:
            print('Insufficient funds! Please try again.')
        return self.bal

    def deposit(self, amount):
        self.bal += amount
        print(f'Deposited amount: ${amount}')
        print(f'New Balance: ${self.bal}')
        return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), 'Bank must derive from class ABC'
    s = Swiss()
    print(s.basicinfo())

    while True:
        print('\n')
        transaction = input(
            'Do you want to make a transaction? (Y/N): ')
        if transaction.lower() == 'n':
            break
        elif transaction.lower() != 'y':
            print('Invalid input. Please type Y or N.')
            continue

        mode = input('Please type W for Withdrawal and D for Deposit: ')
        amount_input = input('Please enter the amount: ')
        if not amount_input.isdigit():
            print('Please input a valid amount!')
            continue
        amount = int(amount_input)
        if mode == 'w' or mode == 'W':
            s.withdraw(amount)
        elif mode == 'd' or mode == 'D':
            s.deposit(amount)
        else:
            print('Error! Please type W for Withdrawal and D for Deposit')


if __name__ == '__main__':
    main()
