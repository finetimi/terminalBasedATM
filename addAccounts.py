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
        bank.addChecking(newChecking)
        bank.saveCheking("c_accounts.txt")
        session['accountNumber'] = newChecking.getAccountNumber()
        return redirect( url_for('checkingAcctView') )
    return render_template("addchecking.html")

def add_savings():
    session.pop('accountNumber', None)
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        newSavings = s_account(fullName)
        bank.addSavings(newSavings)
        bank.saveSavings("s_accounts.txt")
        session['accountNumber'] = newSavings.getAccountNumber()
        return redirect( url_for('savingsAcctView') )
    return render_template("addsavings.html")
