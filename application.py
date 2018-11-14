from flask import Flask, request,render_template,url_for,redirect, session
import os
from accounts import *
from bank import *
from atm import *
from mpHome import index
from mpCAcctView import c_accountInfo
from addAccounts import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

@app.route('/', methods = ['POST', 'GET'])
def index_app():
    return index()

@app.route('/accountInformation', methods = ['GET', 'POST'])
def checkingAcctView():
    return c_accountInfo()

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
