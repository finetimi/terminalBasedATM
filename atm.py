from accounts import *
from bank import Bank



class ManagerPanel():

    EXIT_KEY = True

    """Manager panel. Has control over different accounts,
    can add, remove, and edit account information"""

    def __init__(self):

        """commands for manager,
        inicialized bank class, and passed to other classes"""

        self._bank = Bank()
        self._checkingAccount = Account
        self._savingsAccount = SavingsAccount
        self._commands = {"1":self.addCheckingAccount, "2":self.addSavingsAccount, "3":self.removeCheckingAccount, "4":self.removeSavingsAccount, "5":self.blockCheckingAccount, "6":self.blockSavingsAccount, "7":self.getCheckingAccount, "8": self.getSavingsAccount, "9": self.getAccounts, "10":self.quit}

    def processing(self):
        """Main function of this classes. Prints instructions to Manager;
        gets input from user, checks if command is valid; calls command from dictionary"""
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
        """Gets input from manager, calls a method from bank class,
         and creates a new checking account, saves account into a file"""
        name = input("\nEnter costumer full name: ")
        account = self._checkingAccount(name)
        self._bank.addChecking(account)
        self._bank.saveCheking("c_accounts.txt")
        print ("%s is now an active costumer.\n" % name)

    def addSavingsAccount(self):
        """Gets input from manager, calls a method from bank class,
         and creates a new savings account, saves account into a file"""
        name = input("\nEnter costumer full name: ") + "\n"
        account = self._savingsAccount(name)
        self._bank.addSavings(account)
        self._bank.saveSavings("s_accounts.txt")
        print ("%s is now an active costumer.\n" % name)

    def removeCheckingAccount(self):
        """Gets input from manager; input gets account from dict, accounts is removed, clears accounts storage fiel """
        acctNum = str(input("\nEnter account number: "))
        if self._bank.getCheckingAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            self._bank.removeChecking(acctNum)
            self._bank.saveCheking("c_accounts.txt")
            print ("Account %s deleted.\n" % acctNum)

    def removeSavingsAccount(self):
        """Gets input from manager; input gets account from dict, accounts is removed, clears accounts storage fiel """
        acctNum = str(input("\nEnter account number: "))
        if self._bank.getSavingsAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            self._bank.removeSavings(acctNum)
            self._bank.saveSavings("s_accounts.txt")
            print ("Account %s deleted.\n" % acctNum)

    def blockCheckingAccount(self):
        """Gets acount from input, enters condition, initializes a method from the bank class that unables costumers from accessing their accounts."""
        acctNum = str(input("\nEnter account number: "))
        if self._bank.getCheckingAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            condition = input("Enter 'Blocked' to freeze account or 'Not blocked' to unfreeze account: ")
            self._bank.blockChecking(acctNum, condition)
            self._bank.saveCheking("c_accounts.txt")
            if condition == "Blocked":
                print ("Account blocked.\n")
            elif condition == "Unblocked":
                print ("Account unblocked.\n")

    def blockSavingsAccount(self):
        """Gets acount from input, enters condition, initializes a method from the bank class that unables costumers from accessing their accounts."""
        acctNum = str(input("\nEnter account number: "))
        if self._bank.getSavingsAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            condition = input("Enter 'Blocked' to freeze account or 'Unblocked' to unfreeze account: ")
            self._bank.blockSavings(acctNum, condition)
            self._bank.saveSavings("c_accounts.txt")
            if condition == "Block":
                print ("Account blocked.\n")
            elif condition == "Unblocked":
                print ("Account unblocked.\n")

    def getCheckingAccount(self):
        """Gets account by calling a method from the bank class"""
        acctNum = str(input('\nEnter account number:'))
        if self._bank.getCheckingAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            account = self._bank.getCheckingAccountInfo(acctNum)
            print("\n" + str(account) + "\n")

    def getSavingsAccount(self):
        """Gets account by calling a method from the bank class"""
        acctNum = str(input('\nEnter account number:'))
        if self._bank.getSavingsAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            account = self._bank.getSavingsAccountInfo(acctNum)
            print("\n" + str(account) + "\n")

    def quit(self):
        """Sets the key to fall  which consequently breaks the loop"""
        ManagerPanel.EXIT_KEY = False

    def getAccounts(self):
        """Checks for accounts in bank class accounts dictionaries, and if populated, runs a loop to get all the accounts and prints its information"""
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
