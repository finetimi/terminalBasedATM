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
    return render_template("accountInfoView.html", accountNumber = accountNumber)


# @app.route('/about')
# def about():
#     return render_template("about.html")

# @app.route("/addchecking.html", method=['GET', 'POST'])
# def add_cheking():


if __name__ == '__main__':
    app.run(debug = True)
