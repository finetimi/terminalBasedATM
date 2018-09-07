from bank import *
from accounts import *
from atm import *

# def main():
#     manager = ManagerPanel()
#     return manager.processing()
#
# main()

bank = Bank()
for keys in bank._savingsAccounts.keys():
    print (keys)
