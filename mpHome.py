from flask import Flask, request,render_template,url_for,redirect, session
from accounts import *
from bank import *
from atm import *
bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

def index():
    session.pop('accountNumber', None)
    session['accountNumber'] = None

    if request.method == 'POST':
        session['accountNumber'] = request.form.get("acctNum")
        if bank.getCheckingAccountInfo(session.get('accountNumber', None)) != None:
            return redirect(url_for ('checkingAcctView'))
        elif bank.getSavingsAccountInfo(session.get('accountNumber', None)) != None:
            return redirect(url_for ('savingsAcctView'))
        else:
            return redirect(url_for ('noAccount'))

    else:
        return render_template("home.html")
