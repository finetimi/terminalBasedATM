from flask import Flask, request,render_template,url_for,redirect, session
import os
from accounts import *
from bank import *
from atm import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

@app.route('/', methods = ['POST', 'GET'])
def index():
    session.pop('accountNumber', None)
    session['accountNumber'] = None

    if request.method == 'POST':
        session['accountNumber'] = request.form.get("acctNum")
        if bank.getCheckingAccountInfo(session.get('accountNumber', None)) == None and bank.getSavingsAccountInfo(session.get('accountNumber', None)) == None:
            return redirect(url_for ('noAccount'))
        else:
            return redirect(url_for ('accountInfo'))
    else:
        return render_template("home.html")

@app.route('/accountInformation', methods = ['GET', 'POST'])
def accountInfo():

    accountNumber = session.get('accountNumber', None)
    c_account = bank.getCheckingAccountInfo(accountNumber)
    s_account = bank.getSavingsAccountInfo(accountNumber)

    """Gets the account number from main page and
    verifies the existence of the account, if true, passes the values to template"""

    if c_account == None and s_account == None:
        return redirect(url_for ('noAccount'))

    else:

        """ Enabling user to take actions upon accounts from UI"""
        if request.method == "POST":
            action = request.form.get("actions")
            if c_account != None:
                if action == "blockAccount":
                    c_account._block = True
                elif action == "unblockAccount":
                    c_account._block = False
                elif action == "delete_c_Account":
                    bank.removeChecking(accountNumber)
                    bank.saveCheking("c_accounts.txt")
                    return redirect(url_for('index'))

            elif s_account != None:
                if action == "blockAccount":
                    s_account._block = True
                elif action == "unblockAccount":
                    s_account._block = False
                elif action == "resetSavings":
                    s_account.reset()
                elif action == "delete_s_Account":
                    bank.removeSavings(accountNumber)
                    bank.saveSavings("s_accounts.txt")
                    return redirect(url_for('index'))


        if c_account != None:
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
            return render_template("accountInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance, pin = pin)
        elif s_account != None:
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
    return render_template("accountInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance)

@app.route('/noAccount')
def noAccount():
    return render_template("noAccount.html")

@app.route("/addChecking", methods = ['GET', 'POST'])
def add_cheking():
    session.pop('accountNumber', None)
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        newChecking = account(fullName)
        session['accountNumber'] = newChecking.getAccountNumber()
        bank.addChecking(newChecking)
        bank.saveCheking("c_accounts.txt")
        return redirect( url_for('accountInfo') )
    return render_template("addchecking.html")

@app.route("/addSavings", methods = ['GET', 'POST'])
def add_savings():
    session.pop('accountNumber', None)
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        newSavings = s_account(fullName)
        session['accountNumber'] = newSavings.getAccountNumber()
        bank.addSavings(newSavings)
        bank.saveSavings("s_accounts.txt")
        return redirect( url_for('accountInfo') )
    return render_template("addsavings.html")


if __name__ == '__main__':
    app.run(debug = True)
