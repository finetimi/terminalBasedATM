from random import randint
from sqlalchemy_declarative import CUSTOMER, ADDRESS, ACCOUNTS, engine, Session, session
import sqlalchemy
from sqlalchemy import and_

class NEW_ACCOUNT():

    def __init__(self):
        # initializes and loads the accounts into a mysql DB
        self._engine = engine
        self._Session = Session
        self._session = self._Session()
        self._pin = self.pin_generator()
        self._customer_id = None

    def customer(self, email, **personal_info):
        """Adding new customer"""
        new_customer = CUSTOMER(pin_number=self._pin, email = email, **personal_info)
        self._session.add(new_customer)
        self._session.commit()
        return

    def address(self, email, **address_info):
        address = ADDRESS(customer_id = self.customer_id(email), **address_info)
        self._session.add(address)
        self._session.commit()
        return

    def account(self, email, type):

        customer_account = ACCOUNTS(customer_id = self.customer_id(email), account_type = type, customer_email = email)
        self._session.add(customer_account)
        self._session.commit()
        return

    def second_account(self, id, email):
        customer_obj = self._session.query(CUSTOMER).filter(and_(CUSTOMER.id == id, CUSTOMER.email == email)).first()
        try:
            cust_id = customer_obj.id
            cust_email = customer_obj. email
            number = 0
            for accounts in self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == cust_id, ACCOUNTS.customer_email == cust_email)).all():
                number += 1
            if number <= 1:
                acct_obj = self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == cust_id, ACCOUNTS.customer_email == cust_email)).first()
                if acct_obj.account_type == "Checking":
                    customer_account = ACCOUNTS(customer_id = id, account_type = 'Savings', customer_email = email)
                    self._session.add(customer_account)
                    self._session.commit()
                    return
                if acct_obj.account_type == "Savings":
                    customer_account = ACCOUNTS(customer_id = id, account_type = 'Checking', customer_email = email)
                    self._session.add(customer_account)
                    self._session.commit()
                    return
            else:
                print("Too many accounts")
                return
        except Exception:
            return "Invalid Inputs"

    def customer_id(self, email):
        id = self._session.query(CUSTOMER).filter_by(email = email).first()
        return id.id


    def pin_generator(self):
        # Generates random pin
        pin = ""
        for number in range(4):
            pin += str(randint(0,9))
        return pin
