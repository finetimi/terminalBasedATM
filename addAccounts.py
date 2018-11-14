from flask import Flask, request,render_template,url_for,redirect, session
from accounts import *
from bank import *
from atm import *
bank = Bank()
account = Account
s_account = SavingsAccount
atm = ATM

def add_cheking():
    session.pop('accountNumber', None)
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        newChecking = account(fullName)
        session['accountNumber'] = newChecking.getAccountNumber()
        bank.addChecking(newChecking)
        bank.saveCheking("c_accounts.txt")
        return redirect( url_for('checkingAcctView') )
    return render_template("addchecking.html")

def add_savings():
    session.pop('accountNumber', None)
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        newSavings = s_account(fullName)
        session['accountNumber'] = newSavings.getAccountNumber()
        bank.addSavings(newSavings)
        bank.saveSavings("s_accounts.txt")
        return redirect( url_for('checkingAcctView') )
    return render_template("addsavings.html")
