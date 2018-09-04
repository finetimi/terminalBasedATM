from bank import *
# from atm import ATM
#
# atm = ATM()
#
# print(atm)
from accounts import *

bank = Bank()
bank.addSavings(SavingsAccount("Cristiano", 4000))
bank.addChecking(Account("Kiesse", 5000))
print(bank)
