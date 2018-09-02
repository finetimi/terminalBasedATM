import pickle as cPickle
from random import randint
from accounts import Account, SavingsAccount


class Bank():

    def __init__(self, fileName = None):
        # initializes and loads the accounts into a dict
        self._checkingAccounts = {}
        self._savingsAccounts = {}
        self._fileName = fileName
        if fileName != None:
            fileObj = open(self._fileName, 'r')
            while True:
                try:
                    account = cPickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break


    def __str__(self):
        #returns the general information of all accounts
        return "\n".join(map(str, self._accounts.values()))

    def add(self, account):
        #add account into a dict
        self._accounts[account.getPin()] = account

    def remove(self, pin):
        #removes account from dict
        self._accounts.pop(pin, None)

    def getAccountInfo(self, pin):
        #Returns value associated with pin
        return self._accounts.get(pin, None)

    def computeInterest(self):
        #add total interest earned by all accounts
        total = 0.0
        for account in self._accounts.values():
            total += account.computeInterest()
        return total

    def save(self, fileName = None):
        #loads all the accounts into a file
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, "wb")
        for account in self._accounts.values():
            cPickle.dump(account, fileObj)
        fileObj.close()
