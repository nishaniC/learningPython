class AccountError(Exception):
    pass


class Account:
    def __init__(self, AccNumber):
        self.__AccNumber = AccNumber
        self.__balance = 0
        
    @property
    def balance(self):
        return self.__balance
        
    @property
    def AccNumber(self):
        return self.__AccNumber
        
    @AccNumber.setter
    def AccNumber(self, number):
        raise AccountError('Not possible to change  the acount number')

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            raise AccountError('Not possible to set negative balance')
            
    def deposit(self,amount):
        if amount > 100000:
            print("depositing more than 100000")
        self.__balance += amount
        
    def withdrawal(self,amount):
        if amount > 100000:
            print("withdrawing more than 100000")
        self.__balance -= amount
        
    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            print('It is good to remember to delete the account!')
            self.__balance = 0
            self.__AccNumber = None
            
        else:
            raise AccountError('Not possible to delete as account with a positive value')

# our_tank object has a capacity of 20 units
our_tank = Account("AC20")

# our_tank's current liquid level is set to 10 units
our_tank.balance = 1000
print('Current balance:', our_tank.balance)

try:
    our_tank.balance = -200
except AccountError as e:
     print('Trying to set balance to -200, result:', e)
print('Current balance:', our_tank.balance)

try:
    our_tank.AccNumber = "AC33"
except AccountError as e:
     print('Trying to set AccNumber to AC33, result:', e)
print('Current AccNumber:', our_tank.AccNumber)

our_tank.deposit(1000000)
print('Current balance:', our_tank.balance)

try:
    del our_tank.balance
except AccountError as e:
     print('Trying to delete the account attribute containing a non-zero balance, result:', e)
print('Current AccNumber:', our_tank.AccNumber)
print('Current balance:', our_tank.balance)
