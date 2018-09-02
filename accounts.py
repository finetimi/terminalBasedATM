from random import randint

class Account():
    """Initialize the code"""
    def __init__(self, name, balance = 0.0):
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

    def deposit(self, amount):
        """Makes a deposit to account """
        if amount < 0:
            print("Deposit needs to be bigger than 0")
        else:
            self._balance += amount
        return None

    def withdraw(self, amount):
        #balance gets reduced
        if amount < 0:
            print("Amount needs to be bigger than 0")
        elif self._balance < amount:
            print("Insufficient funds.")
        else:
            self._balance -= amount
        return None


    def __str__(self):
        # Returns information of the account
        accounts = "Name:   " + self._name + "\n"
        accounts += "Account Number:   " + self._accountNumber + "\n"
        accounts += "Account Type:   " + self._accountType + "\n"
        accounts += "Balance:   " + "$" + str(self._balance)
        return accounts

class SavingsAccount(Account):
    RATE = 0.03
    LIMIT = 5

    def __init__(self, name, balance = 0.0):
        Account.__init__(self, name, balance)
        self._count = 0
        self._accountType = "Savings"


    def computeInterest(self):
        #computes interest and it is deposit to account
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def withdraw(self, amount):
        #balance gets reduced
        if self._count == SavingsAccount.LIMIT:
            return ("Reach the withdrawal limit.")
        else:
            withdrawal = Account.withdraw(amount)
            if withdrawal == None:
                self._count += 1
            return withdrawal
