from random import randint

class Account():

    BLOCK = False

    """Initialize the code"""
    def __init__(self, name = None, balance = 0.0):
        self._name = name
        self._balance = balance
        self._accountNumber = self.accountNumber()
        self._pinNumber = self.pinGenerator()
        self._accountType = "Checking"

    def accountNumber(self):
        # Generates random account number
        number = ""
        for numbers in range(10):
            number += str(randint(0,9))
        return number


    def pinGenerator(self):
        # Generates random pin
        pin = ""
        for number in range(4):
            pin += str(randint(0,9))
        return pin

    def getName(self):
        """Gets student's name"""
        return self._name

    def getBalance(self):
        """Get the balance of account"""
        return self._balance

    def getPin(self):
        """Get pin of account"""
        return self._pinNumber

    def getAccountNumber(self):
        # Returns account Number
        return self._accountNumber

    def __str__(self):
        # Returns information of the account
        accounts = "\nName:   " + self._name + "\n"+ "\n"
        accounts += "Account Number:   " + self._accountNumber + "\n"
        accounts += "Account Type:   " + self._accountType + "\n"
        accounts += "Balance:   " + "$" + str(self._balance) + "\n"
        return accounts

    def blockAccount(self, condition = None):
        """Condition changes value of class variable Block"""
        if condition == "Blocked":
            Account.BLOCK = True
        elif condition == "Unblocked":
            Account.BLOCK = False
        return Account.BLOCK


    def deposit(self, amount):
        #checkers checks if account is blocked; balance is increased
        checker = self.blockAccount()
        if checker == True:
            return ("Account Blocked. Contact bank for more information.")
        elif amount < 0:
            print("Deposit needs to be bigger than 0")
        else:
            self._balance += amount
        return None

    def withdraw(self, amount):
        #balance gets reduced
        checker = self.blockAccount()
        if checker == True:
            return ("Account Blocked. Contact bank for more information.")
        elif amount < 0:
            print("Amount needs to be bigger than 0")
        elif self._balance < amount:
            print("Insufficient funds.")
        else:
            self._balance -= amount
        return None



class SavingsAccount(Account):
    RATE = 0.03
    LIMIT = 5

    def __init__(self, name = None, balance = 0.0):
        Account.__init__(self, name, balance)
        self._count = 0
        self._accountType = "Savings"

    def computeInterest(self):
        #computes interest and it is deposit to account
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def withdraw(self, amount):
        #checkers checks if account is blocked; balance gets reduced
        checker = Account.blockAccount(self, condition = None)
        if checker == True:
            return("Account blocked, contact bank for more information.")
        elif self._count == SavingsAccount.LIMIT:
            return ("\nReach the withdrawal limit. Contact bank.\n")
        else:
            withdrawal = Account.withdraw(self, amount)
            if withdrawal == None:
                    self._count += 1
            return ("\nAmount Withdrew: $%.2f" % amount + "\n")

    def reset(self):
        # Resets monthly withdrawals
        self._count = 0
