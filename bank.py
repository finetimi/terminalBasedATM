import pickle as cPickle
from random import randint
from accounts import Account, SavingsAccount


class Bank():

    def __init__(self, c_fileName = "c_accounts.txt", s_fileName = "s_accounts.txt"):
        # initializes and loads the accounts into a dict
        self._checkingAccounts = {}
        self._savingsAccounts = {}
        self._c_fileName = c_fileName
        self._s_fileName = s_fileName
        if c_fileName == "c_accounts.txt":
            fileObj = open(self._c_fileName, 'rb')
            while True:
                try:
                    account = cPickle.load(fileObj)
                    self.addChecking(account)
                except EOFError:
                    fileObj.close()
                    break
        if s_fileName == "s_accounts.txt":
            fileObj = open(self._s_fileName, "rb")
            while True:
                try:
                    account = cPickle.load(fileObj)
                    self.addSavings(account)
                except EOFError:
                    fileObj.close()
                    break



    def __str__(self):
        #returns the general information of all accounts
        return "\n".join(map(str, self._checkingAccounts.values())) + "\n\n" +"\n".join(map(str,self._savingsAccounts.values()))

    def addChecking(self, account):
        #add checking account into a dict
        self._checkingAccounts[account.getAccountNumber()] = account

    def addSavings(self, account):
        #add savings account into dict
        self._savingsAccounts[account.getAccountNumber()] = account

    def removeChecking(self, acctNum):
        #removes account from dict
        self._checkingAccounts.pop(acctNum, None)

    def removeSavings(self, acctNum):
        #removes account from dict
        self._savingsAccounts.pop(acctNum, None)

    def blockChecking(self, acctNum, condition):
        """Checks if account exists in dict; pass condition to an Account method."""
        account = self._checkingAccounts.get(acctNum, None)
        account.blockAccount(condition)

    def blockSavings(self, acctNum, condition):
        """Checks if account exists in dict; pass condition to an Account method."""
        account = self._savingsAccounts.get(acctNum, None)
        account.blockAccount(condition)

    def unblockWithdrawals(self, acctNum):
        # Resetting monthly savings withdrawals
        account = self._savingsAccounts.get(acctNum, None)
        if account != None:
            account.reset()
        else:
            return

    def getCheckingAccountInfo(self, acctNum):
        #Returns value associated with account number
        account = self._checkingAccounts.get(acctNum, None)
        return account

    def getSavingsAccountInfo(self, acctNum):
        #Returns value associated with account number
        account = self._savingsAccounts.get(acctNum, None)
        return account

    def getBalance(self, acctNum):
        # Get balance of Checking or savings accounts, by accessing dict. Checks if accounts exist or not.
        accountCheking = self.getCheckingAccountInfo(acctNum)
        accountSavings = self.getSavingsAccountInfo(acctNum)
        if accountCheking == None and accountSavings == None:
            print("Incorrect Account Number.")
        elif accountSavings != None:
            return accountCheking.getBalance()
        elif accountSavings != None:
            return accountSavings.getBalance()

    def getPin(self, acctNum):
        # Get pin of Checking or savings accounts, by accessing dict. Checks if accounts exist or not.
        accountCheking = self.getCheckingAccountInfo(acctNum)
        accountSavings = self.getSavingsAccountInfo(acctNum)
        if accountCheking == None and accountSavings == None:
            print("Incorrect Account Number.")
        elif accountCheking != None:
            print (accountCheking._pinNumber)
        elif accountSavings != None:
            print (accountSavings._pinNumber)




    def computeInterest(self):
        #add total interest earned by all accounts
        total = 0.0
        for account in self._savingsAccounts.values():
            total += account.computeInterest()
        return total

    def saveCheking(self, fileName = None):
        #saves all the checking accounts into a file
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, "wb")
        for account in self._checkingAccounts.values():
            cPickle.dump(account, fileObj)
        fileObj.close()

    def saveSavings(self, fileName = None):
        #saves all the savings accounts into a file
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, "wb")
        for account in self._savingsAccounts.values():
            cPickle.dump(account, fileObj)
        fileObj.close()
