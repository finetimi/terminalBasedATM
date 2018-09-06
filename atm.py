from accounts import *
from bank import Bank



class ManagerPanel():

    EXIT_KEY = True

    """Manager panel. Has control over different accounts,
    can add, remove, and edit account information"""

    def __init__(self):

        """commands for manager"""

        self._bank = Bank()
        self._checkingAccount = Account
        self._savingsAccount = SavingsAccount
        self._commands = {"1":self.addCheckingAccount, "2":self.addSavingsAccount, "3":self.removeCheckingAccount, "4":self.removeSavingsAccount, "5":self.blockCheckingAccount, "6":self.blockSavingsAccount, "7":self.getCheckingAccount, "8": self.getSavingsAccount, "9": self.getAccounts, "10":self.quit}

    def processing(self):
        while True:
            if ManagerPanel.EXIT_KEY == False:
                print("\nHave a nice day!\n")
                break
            print("1  Add New Checking Account;")
            print("2  Add New Savings Account;")
            print("3  Remove Existing Checking Account;")
            print("4  Remove Existing Savings Account;")
            print("5  Block Checking Account;")
            print("6  Block Savings Account;")
            print("7  Get Costumer Information (Checking);")
            print("8  Get Costumer Information (Savings);")
            print("9  Get All Accounts;")
            print("10 Quit\n")
            command = input("Enter number: ")
            theCommand = self._commands.get(command, None)
            if theCommand == None:
                print("Invalid command. Try again.")
            else:
                theCommand()


    def addCheckingAccount(self):
        name = input("\nEnter costumer full name: ")
        account = self._checkingAccount(name)
        self._bank.addChecking(account)
        self._bank.saveCheking("c_accounts.txt")
        print ("%s is now an active costumer.\n" % name)

    def addSavingsAccount(self):
        name = input("\nEnter costumer full name: ") + "\n"
        account = self._savingsAccount(name)
        self._bank.addSavings(account)
        self._bank.saveSavings("s_accounts.txt")
        print ("%s is now an active costumer.\n" % name)

    def removeCheckingAccount(self):
        acctNum = str(input("\nEnter account number: "))
        self._bank.removeChecking(acctNum)
        self._bank.saveCheking("c_accounts.txt")
        print ("Account %s deleted.\n" % acctNum)

    def removeSavingsAccount(self):
        acctNum = str(input("\nEnter account number: "))
        self._bank.removeSavings(acctNum)
        self._bank.saveSavings("s_accounts.txt")
        print ("Account %s deleted.\n" % acctNum)

    def blockCheckingAccount(self):
        acctNum = str(input("\nEnter account number: "))
        condition = input("Enter 'Blocked' to freeze account or 'Not blocked' to unfreeze account: ")
        self._bank.blockChecking(acctNum, condition)
        if condition == "Blocked":
            print ("Account blocked.\n")
        elif condition == "Unblocked":
            print ("Account unblocked.\n")

    def blockSavingsAccount(self):
        acctNum = str(input("\nEnter account number: "))
        condition = input("Enter 'Blocked' to freeze account or 'Unblocked' to unfreeze account: ")
        self._bank.blockSavings(acctNum, condition)
        if condition == "Block":
            print ("Account blocked.\n")
        elif condition == "Unblocked":
            print ("Account unblocked.\n")

    def getCheckingAccount(self):
        acctNum = input('\nEnter account number:')
        account = self._bank.getCheckingAccountInfo(acctNum)
        print(account + "\n")

    def getSavingsAccount(self):
        acctNum = input('\nEnter account number:')
        account = self._bank.getSavingsAccountInfo(acctNum)
        print(account + "\n")

    def quit(self):
        ManagerPanel.EXIT_KEY = False

    def getAccounts(self):
        if self._bank._checkingAccounts == {}:
            print("\nNo Checking Accounts.")
        else:
            for key, value in self._bank._checkingAccounts.items():
                print (str(value) + "\n")
        if self._bank._savingsAccounts == {}:
            print("\nNo Savings Accounts.\n")
        else:
            for key, value in self._bank._savingsAccounts.items():
                print (str(value) + "\n")


# class ATM():
#
#     """Terminal based ATM. Client will be able to perform
#     basic transactions."""
#
#     def __init__(self):
#         """List of commands for the ATM, it should also load
#         some accounts in order to be able to function"""
