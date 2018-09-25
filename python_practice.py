from bank import *
from accounts import *
from atm import *

def main():
    atm = ATM()
    return atm.processing()

main()

# bank = Bank()
#
# account = bank._checkingAccounts.get("2750283571", None)
# print(account._pinNumber)
