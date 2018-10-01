from flask import Flask, request,render_template,url_for, redirect
from accounts import *
from bank import *
from atm import *

app = Flask(__name__)

bank = Bank()
account = Account
atm = ATM

@app.route('/', methods = ['POST', 'GET'])
def index():

    accountNumber = request.form.get("acctNum")

    if request.method == 'POST':
        if bank.getCheckingAccountInfo(accountNumber) == None:
            return redirect(url_for ('noAccount'))
        else:
            return redirect(url_for ('accountInfo'))
    else:
        return render_template("home.html")

@app.route('/accountInformation', methods = ['GET', 'POST'])
def accountInfo():
    accountNumber = request.form.get("acctNum")
    c_account = bank.getCheckingAccountInfo(accountNumber)
    s_account = bank.getSavingsAccountInfo(accountNumber)
    if c_account == None and s_account == None:
        return redirect(url_for ('noAccount'))
    else:
        if c_account != None:
            clientName = c_account._name
            accountType = c_account._accountType
            status = None
            if c_account._block == False:
                status = "Unblocked"
            else:
                status = "Blocked"
            balance = "$" + str(c_account._balance)
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
            balance = "$ %.2f" % value
            return render_template("accountInfoView.html", accountNumber = accountNumber, clientName = clientName, accountType = accountType, status = status, balance = balance)
# @app.route('/about')
# def about():
#     return render_template("about.html")

# @app.route("/addchecking.html", method=['GET', 'POST'])
# def add_cheking():


if __name__ == '__main__':
    app.run(debug = True)
