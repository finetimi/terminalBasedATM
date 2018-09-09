from bank import *
from accounts import *
from atm import *

def main():
    atm = ATM()
    return atm.processing()

main()

# bank = Bank()
#
# account = bank._checkingAccounts.get("2775046230", None)
# if account._block == True:
#     print("Blocked")
# elif account._block == False:
#     print("Unblocked")
