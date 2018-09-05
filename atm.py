from accounts import *
from bank import Bank



class ManagerPanel():

    EXIT_KEY = True

    """Manager panel. Has control over different accounts,
    can add, remove, and edit account information"""

    def __init__(self):
        """commands for manager"""
        self._bank = Bank()
        self._checkingAccount = Account()
        self._savingsAccount = SavingsAccount()
        self._commands = {}
        self._commands["1"] = self.addCheckingAccount()
        self._commands["2"] = self.addSavingsAccount()
        self._commands["3"] = self.removeCheckingAccount()
        self._commands["4"] = self.removeSavingsAccount()
        self._commands["5"] = self.putBlockChecking()
        self._commands["6"] = self.putBlockSavings()
        self._commands["7"] = self.getAllAccounts()
        self._commands["8"] = self.quit()

    def processing(self):
        while True:
            if ManagerPanel.EXIT_KEY == False:
                print("Have a nice day!")
                break
            print("1  Add New Checking Account;")
            print("2  Add New Savings Account;")
            print("3  Remove Existing Checking Account;")
            print("4  Remove Existing Savings Account;")
            print("5  Block Checking Account;")
            print("6  Block Savings Account;")
            print("7  Get All Accounts;")
            print("8  Quit\n")
            command = input("Enter number: ")
            if self._commands.get(command, None) == None:
                print("Invalid command. Try again.")
            else:
                return self._commands[command]


    def addCheckingAccount(self):
        name = input("Enter costumer full name: ")
        self._bank.addChecking(self._checkingAccount(name))
        self._bank.saveCheking("c_accounts.txt")
        return ("%s is now an active costumer." % name)

    def addSavingsAccount(self):
        name = input("Enter costumer full name: ")
        self._bank.addSavings(self._savingsAccount(name))
        self._bank.saveSavings("s_accounts.txt")
        return ("%s is now an active costumer." % name)

    def removeCheckingAccount(self):
        acctNum = str(input("Enter account number: "))
        self._bank.removeChecking(acctNum)
        return ("Account %s deleted." % acctNum)

    def removeSavingsAccount(self):
        acctNum = str(input("Enter account number: "))
        self._bank.removeSavings(acctNum)
        return ("Account %s deleted." % acctNum)

    def blockCheckingAccount(self):
        acctNum = str(input("Enter account number: "))
        status = input("Enter 'Blocked' to freeze account or 'Not blocked' to unfreeze account: ")
        self._bank.blockChecking(acctNum, status)
        if status == "Blocked":
            return ("Account blocked.")
        elif status == "Not blocked":
            return ("Account unblocked.")

    def blockSavingsAccount(self):
        acctNum = str(input("Enter account number: "))
        status = input("Enter 'Blocked' to freeze account or 'Not blocked' to unfreeze account: ")
        self._bank.blockSavings(acctNum, status)
        if status == "block":
            return ("Account blocked.")
        elif status == "Not blocked":
            return ("Account unblocked")

    def quit(self):
        ATM.EXIT_KEY = False
        return

    def getAllAccounts(self):
        return self._bank.__str__()
# class ATM():
#
#     """Terminal based ATM. Client will be able to perform
#     basic transactions."""
#
#     def __init__(self):
#         """List of commands for the ATM, it should also load
#         some accounts in order to be able to function"""
