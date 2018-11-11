from flask import Flask, request,render_template,url_for,redirect, session
import os
from accounts import *
from bank import *
from atm import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

bank = Bank()
account = Account
atm = ATM

@app.route('/', methods = ['POST', 'GET'])
def index():

    session['accountNumber'] = None

    if request.method == 'POST':
        session['accountNumber'] = request.form.get("acctNum")

        if bank.getCheckingAccountInfo(session.get('accountNumber')) == None:
            return redirect(url_for ('noAccount'))
        else:
            return redirect(url_for ('accountInfo'))
    else:
        return render_template("home.html")

@app.route('/accountInformation', methods = ['GET', 'POST'])
def accountInfo():

    accountNumber = session.get('accountNumber')
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

        if c_account != None:
            clientName = c_account._name
            accountType = c_account._accountType
            status = None
            if c_account._block == False:
                status = "Unblocked"
            else:
                status = "Blocked"
            value = c_account._balance
            balance = "$ {:,.2f}".format(value)
            return render_template("accountInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance)
        elif s_account != None:
            clientName = s_account._name
            accountType = s_account._accountType
            status = None
            if s_account._block == False:
                status = "Unblocked"
            else:
                status = "Blocked"
            value = s_account._balance
            balance = "$ {:,.2f}".format(value)

    return render_template("accountInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance)

@app.route('/noAccount')
def noAccount():
    return render_template("noAccount.html")

# @app.route("/addchecking.html", method=['GET', 'POST'])
# def add_cheking():


if __name__ == '__main__':
    app.run(debug = True)
