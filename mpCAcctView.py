from flask import Flask, request,render_template,url_for,redirect, session
from accounts import *
from bank import *
from atm import *
bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

def c_accountInfo():

    accountNumber = session.get('accountNumber', None)
    c_account = bank.getCheckingAccountInfo(accountNumber)

    """Gets the account number from main page and
    verifies the existence of the account, if true, passes the values to template"""

    if c_account == None:
        return redirect(url_for ('noAccount'))

    else:

        """ Enabling user to take actions upon accounts from UI"""
        if request.method == "POST":

            action = request.form.get("actions")

            if action == "blockAccount":
                c_account._block = True
            elif action == "unblockAccount":
                c_account._block = False
            elif action == "delete_c_Account":
                bank.removeChecking(accountNumber)
                bank.saveCheking("c_accounts.txt")
                return redirect(url_for('index_app'))


        clientName = c_account._name
        accountType = c_account._accountType
        status = None
        if c_account._block == False:
            status = "Unblocked"
        else:
            status = "Blocked"
        value = c_account._balance
        pin = c_account._pinNumber
        balance = "$ {:,.2f}".format(value)
        bank.saveCheking("c_accounts.txt")
        return render_template("checkingInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance, pin = pin)

def s_accountInfo():

    accountNumber = session.get('accountNumber', None)
    s_account = bank.getSavingsAccountInfo(accountNumber)

    """Gets the account number from main page and
    verifies the existence of the account, if true, passes the values to template"""

    if s_account == None:
        return redirect(url_for ('noAccount'))

    else:

        """ Enabling user to take actions upon accounts from UI"""
        if request.method == "POST":

            action = request.form.get("actions")

            if action == "blockAccount":
                s_account._block = True
            elif action == "unblockAccount":
                s_account._block = False
            elif action == "resetSavings":
                s_account.reset()
            elif action == "delete_s_Account":
                bank.removeSavings(accountNumber)
                bank.saveSavings("s_accounts.txt")
                return redirect(url_for('index_app'))

        clientName = s_account._name
        accountType = s_account._accountType
        status = None
        if s_account._block == False:
            status = "Unblocked"
        else:
            status = "Blocked"
        value = s_account._balance
        pin = s_account._pinNumber
        balance = "$ {:,.2f}".format(value)
        bank.saveSavings("s_accounts.txt")
    return render_template("savingsInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance, pin = pin)
