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
# acctnum = str(input("Enter Account Number: "))
# bank.removeSavings(acctnum)
# print(bank)
acctNum = str(input("Enter account number: "))
print(bank.getSavingsAccountInfo(acctNum))
