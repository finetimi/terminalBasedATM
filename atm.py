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
        self._commands = {"1":self.addCheckingAccount, "2":self.addSavingsAccount, "3":self.removeCheckingAccount, \
        "4":self.removeSavingsAccount, "5":self.blockCheckingAccount, "6":self.blockSavingsAccount, "7":self.unblockWithdrawals, "8":self.getCheckingAccount, "9": self.getSavingsAccount, "10": self.getAccounts,\
         "11": self.quit }

    def processing(self):
        """Main function of this classes. Prints instructions to Manager;
        gets input from user, checks if command is valid; calls command from dictionary"""
        while True:
            if ManagerPanel.EXIT_KEY == False:
                print("\nHave a nice day!\n")
                break
            print("\n1  Add New Checking Account;")
            print("2  Add New Savings Account;")
            print("3  Remove Existing Checking Account;")
            print("4  Remove Existing Savings Account;")
            print("5  Block/Unblock Checking Account;")
            print("6  Block/Unblock Savings Account;")
            print("7  Resetting Withdrawals;")
            print("8  Get Costumer Information (Checking);")
            print("9  Get Costumer Information (Savings);")
            print("10 Get All Accounts;")
            print("11 Quit\n")
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
        name = input("\nEnter costumer full name: ")
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
            condition = input("Enter '1' to freeze account or '2' to unfreeze account: ")
            self._bank.blockChecking(acctNum, condition)
            self._bank.saveCheking("c_accounts.txt")
            if condition == "1":
                print ("Account blocked.\n")
            elif condition == "2":
                print ("Account unblocked.\n")

    def blockSavingsAccount(self):
        """Gets acount from input, enters condition, initializes a method from the bank class that unables costumers from accessing their accounts."""
        acctNum = str(input("\nEnter account number: "))
        if self._bank.getSavingsAccountInfo(acctNum) == None:
            print("Inexistent Account.")
        else:
            condition = input("Enter '1' to freeze account or '2' to unfreeze account: ")
            self._bank.blockSavings(acctNum, condition)
            self._bank.saveSavings("s_accounts.txt")
            if condition == "1":
                print ("Account blocked.\n")
            elif condition == "2":
                print ("Account unblocked.\n")

    def unblockWithdrawals(self):
        # Manager resets counter of with limit
        acctNum = str(input("Enter Account Number: "))
        account = self._bank.getSavingsAccountInfo(acctNum)
        self._bank.unblockWithdrawals(acctNum)
        self._bank.saveSavings("s_accounts.txt")
        print("\nWithdrawals Available for account: %s\n" % acctNum)

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


class ATM():

    """Terminal based ATM. Client will be able to perform
    basic transactions."""

    EXIT_KEY = True
    TRIES = 3

    def __init__(self):
        """List of commands for the ATM, it should also load
        some accounts in order to be able to function"""
        self._bank = Bank()
        self._checkingAccount = self._bank.getCheckingAccountInfo
        self._savingsAccount = self._bank.getSavingsAccountInfo
        self._loggedIn = None
        self._counterCheckingAcct = 0
        self._counterSavingsAcct = 0
        self._counterCheckingPin = 0
        self._counterSavingsPin= 0
        self._counterChangePin = 0
        self._commands = {"1": self.deposit,"2": self.withdraw, "3": self.getBalance, "4": self.changePin, "5": self.quit}

    def processing(self):
        """Main function. Initiates every other function inside the dictionary. Before accessing functions,
        it confirms user's personal info. If user fails to provide required info more than 3 times, loop breaks. Stores logged account into a class variable.
        With the logged account, it gets its type and execute different functions according to account type."""
        while True:
            if ATM.EXIT_KEY == False:
                break
            else:
                if self._counterCheckingAcct == ATM.TRIES and self._counterSavingsAcct == ATM.TRIES:
                    print("It seems like you don't know your account number. Police is on the way to help.")
                    ATM.EXIT_KEY = False
                    return
                if self._counterCheckingPin == ATM.TRIES and self._counterSavingsPin == ATM.TRIES:
                    print("It seems like you don't know your pin number. Police is on the way to help.")
                    ATM.EXIT_KEY = False
                    return
                acctNum = str(input("Enter Account number. (To quit, enter 'q') : "))
                if acctNum == "q":
                    print("Have a nice day!")
                    ATM.EXIT_KEY = False
                    return
                verifier1 = self._checkingAccount(acctNum)
                verifier2 = self._savingsAccount(acctNum)
                if verifier1 == None and verifier2 == None:
                    print("Invalid or Inexistent Accout Number. Try again.")
                    self._counterCheckingAcct += 1
                    self._counterSavingsAcct += 1
                elif verifier1 != None:
                    self._loggedIn = verifier1
                    self._counterCheckingAcct = 0
                    pin = str(input("Enter Pin: "))
                    if pin != verifier1._pinNumber:
                        print("Wrong Pin, try again.")
                        self._counterCheckingPin += 1
                        self._counterSavingsPin += 1
                    else:
                        while True:
                            if ATM.EXIT_KEY == False:
                                print("Have a nice day!\n")
                                break
                            print("\n1   Deposit Funds;")
                            print("2   Withdraw Funds;")
                            print("3   Check Balance;")
                            print("4   Change Pin;")
                            print("5   Quit\n")
                            number = str(input("Enter number: "))
                            theCommand = self._commands.get(number, None)
                            if theCommand == None:
                                print("Inexistent Command. Try Again.")
                            else:
                                theCommand()
                elif verifier2 != None:
                    self._loggedIn = verifier2
                    self._counterSavingsAcct = 0
                    pin = str(input("Enter Pin: "))
                    if pin != verifier2._pinNumber:
                        print("Wrong Pin, try again.")
                        self._counterSavingsPin += 1
                        self._counterCheckingPin += 1
                    else:
                        while True:
                            if ATM.EXIT_KEY == False:
                                print("Have a nice day!\n")
                                break
                            print("\n1   Deposit Funds;")
                            print("2   Withdraw Funds;")
                            print("3   Check Balance;")
                            print("4   Change Pin;")
                            print("5   Quit\n")
                            number = str(input("Enter number: "))
                            theCommand = self._commands.get(number, None)
                            if theCommand == None:
                                print("Inexistent Command. Try Again.")
                            else:
                                theCommand()
    def deposit(self):
        """Checks account type, deposit money into account and saves it into dict stored in Bank object/class"""
        if self._loggedIn._accountType == "Checking":
            money = float(input("Enter deposit amount: "))
            if self._loggedIn.deposit(money) == "1":
                print("Account Blocked. Contact bank for more information.")
                return
            else:
                print("\nDeposit Amount: $%.2f" % money + "\n")
                self._bank.saveCheking("c_accounts.txt")
        elif self._loggedIn._accountType == "Savings":
            money = float(input("Enter deposit amount: "))
            if self._loggedIn.deposit(money) == "1":
                print("Account Blocked. Contact bank for more information.")
                return
            else:
                print("\nDeposit Amount: $%.2f" % money + "\n")
                self._bank.saveSavings("s_accounts.txt")

    def withdraw(self):
        """Checks account type, withdraws money from account and saves it into dict stored in Bank object/class"""
        if self._loggedIn._accountType == "Checking":
            money = float(input("Withdrawal amount: "))
            if self._loggedIn.withdraw(money) == "1":
                print("Account Blocked. Contact bank for more information.")
                return
            else:
                print("\nAmount Withdrew: $%.2f" % money + "\n")
                self._bank.saveCheking("c_accounts.txt")
        elif self._loggedIn._accountType == "Savings":
            money = float(input("withdrawal amount: "))
            if self._loggedIn.withdraw(money) == "1":
                print("Account Blocked. Contact bank for more information.")
                return
            else:
                print(self._loggedIn.withdraw(money))
                self._bank.saveSavings("s_accounts.txt")

    def getBalance(self):
        # Gets balance for user
        balance = self._loggedIn.getBalance()
        print("\nCurrent Balance: $%.2f" % balance + "\n")

    def changePin(self):
        """Checks to see if user has old pin, if not, breaks. Gets new pin and confirms it."""
        while True:
            if self._counterChangePin == ATM.TRIES:
                print("\nIt seems like you don't know your pin. Police is on the way to help.\n")
                ATM.EXIT_KEY = False
                return
            if self._loggedIn._accountType == "Checking":
                old_pin = str(input("Current Pin: "))
                if old_pin == self._loggedIn._pinNumber:
                    new_pin = str(input("New Pin: "))
                    if len(new_pin) != 4:
                        print("Insert 4 digit Pin.")
                    else:
                        new_pin_confirmation = str(input("Confirm New Pin: "))
                        if new_pin != new_pin_confirmation:
                            print("Confirmation Pin does not match new Pin. Try again.")
                        else:
                            self._loggedIn._pinNumber = new_pin_confirmation
                            self._bank.saveCheking("c_accounts.txt")
                            print('Pin number changed successfully.')
                            return
                else:
                    print("Incorrect Pin. Try again.")
                    self._counterChangePin += 1
            elif self._loggedIn._accountType == "Savings":
                old_pin = str(input("Current Pin: "))
                if old_pin == self._loggedIn._pinNumber:
                    new_pin = str(input("New Pin: "))
                    if len(new_pin) != 4:
                        print("Insert 4 digit Pin.")
                    else:
                        new_pin_confirmation = str(input("Confirm New Pin: "))
                        if new_pin != new_pin_confirmation:
                            print("Confirmation Pin does not match new Pin. Try again.")
                        else:
                            self._loggedIn._pinNumber = new_pin_confirmation
                            self._bank.saveSavings("s_accounts.txt")
                            print('Pin number changed successfully.')
                            return
                else:
                    print("Incorrect Pin. Try again.")
                    self._counterChangePin += 1
    def quit(self):
        """Quits by changing exit_key value"""
        ATM.EXIT_KEY = False
