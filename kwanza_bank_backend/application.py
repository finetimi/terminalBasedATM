from flask import Flask, request,render_template,url_for,redirect, session
import os
from accounts import Account, SavingsAccount
from bank import Bank
from atm import ManagerPanel, ATM
from mpHome import index
from mpCAcctView import c_accountInfo, s_accountInfo
from addAccounts import add_cheking, add_savings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

@app.route('/', methods = ['POST', 'GET'])
def index_app():
    return index()

@app.route('/checking_information', methods = ['GET', 'POST'])
def checkingAcctView():
    return c_accountInfo()

@app.route('/savings_information', methods = ['GET', 'POST'])
def savingsAcctView():
    return s_accountInfo()

@app.route('/noAccount')
def noAccount():
    return render_template("noAccount.html")

@app.route("/addChecking", methods = ['GET', 'POST'])
def addCheckingAcct():
    return add_cheking()

@app.route("/addSavings", methods = ['GET', 'POST'])
def addSavingsAcct():
    return add_savings()


if __name__ == '__main__':
    app.run(debug = True)
