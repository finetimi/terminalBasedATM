from accounts import *
from bank import Bank



class ManagerPanel():

    """Manager panel. Has control over different accounts,
    can add, remove, and edit account information"""

    def __init__(self):
        """commands for manager"""
        self._bank = Bank()
        self._checkingAccount = Account()
        self._savingsAccount = SavingsAccount()
        self._commands = {}
        self._commands ["1"] = self.addCheckingAccount()
        self._commands ["2"] = self.addSavingsAccount()
        self._commands ["3"] = self.removeCheckingAccount()
        self._commands ["4"] = self.removeSavingsAccount()
        self._commands ["5"] = self.putBlock()
        self._commands ["6"] = self.quit()

    def addCheckingAccount(self):
        name = input("Enter costumer full name: ")
        self._bank.addChecking(self._checkingAccount(name))
        self._bank.saveCheking("c_accounts.txt")
        return ("%s is now an active costumer." % name)

    def addSavingsAccount(self):
        name = input("Enter costumer full name: ")
        self._bank.addSavings(self._checkingAccount(name))
        self._bank.saveSavings("s_accounts.txt")
        return ("%s is now an active costumer." % name)

    def removeCheckingAccount(self):
        acctNum = str(input("Enter account number: "))
        self._bank("c_accounts.txt")

# class ATM():
#
#     """Terminal based ATM. Client will be able to perform
#     basic transactions."""
#
#     def __init__(self):
#         """List of commands for the ATM, it should also load
#         some accounts in order to be able to function"""
