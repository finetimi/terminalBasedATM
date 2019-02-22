from sqlalchemy_declarative import CUSTOMER, ADDRESS, ACCOUNTS, engine, Session, session
from sqlalchemy import and_
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

class ACCOUNT_MNG():

    def __init__(self, email, pin):
        self._engine = engine
        self._Session = Session
        self._session = self._Session()
        self._email = email
        self._pin = pin

# Here the customer object is stored under a variable.

    def active_user(self):
        try:
            user_obj = self._session.query(CUSTOMER).filter(and_(CUSTOMER.email == self._email,
            CUSTOMER.pin_number == self._pin))
            validator = user_obj.first()
            validator_id = validator.id
            return user_obj

        except Exception:
            return None
# Validate customer if it exists or not

    def user_id(self):
        c_id = self.active_user().first()
        id = c_id.id
        logging.debug(id)
        return id

# Updating customer's table

    def update_driver_license(self, new_license):
        customer = active_user()
        self.active_user().update({CUSTOMER.driver_license:new_license.upper()})
        self._session.commit()
        return

    def update_pin(self, new_pin):
        self.active_user().update({CUSTOMER.pin_number:new_pin})
        self._session.commit()
        return

    def update_phone_number(self, new_number):
        self.active_user().update({CUSTOMER.phone_number:new_number})
        self._session.commit()
        return

    def update_email(self, new_email):
        self.active_user().update({CUSTOMER.email:new_email})
        self._session.commit()
        return

# Updating Address Table

    def update_address(self, unit, street, city, postal, state):
        id = self.user_id()
        self._session.query(ADDRESS).filter(ADDRESS.customer_id == id).update({ADDRESS.unit_number: unit.title()})
        self._session.query(ADDRESS).filter(ADDRESS.customer_id == id).update({ADDRESS.street_name: street.title()})
        self._session.query(ADDRESS).filter(ADDRESS.customer_id == id).update({ADDRESS.city: city.title()})
        self._session.query(ADDRESS).filter(ADDRESS.customer_id == id).update({ADDRESS.postal_code: postal})
        self._session.query(ADDRESS).filter(ADDRESS.customer_id == id).update({ADDRESS.state: state.upper()})
        self._session.commit()
        return

# Updating Accounts' Table/ Should this be part of the transaction (Not accessible to mng)

    def update_balance(self, new_balace):
        id = self.user_id()
        account_obj = self._session.query(ACCOUNTS).filter(ACCOUNTS.customer_id == id).update({ACCOUNTS.balance:new_balance})
        self._session.commit()
        return

# This goes to a different page

    def remove_account(self, customer_id):
        self._session.query(CUSTOMER).filter(CUSTOMER.id == customer_id).delete()
        self._session.commit()
        return

# Deactivating/Blocking Accounts

    def inactive_account(self, account_id):
        id = self.user_id()
        self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == id, ACCOUNTS.id == account_id)).update({ACCOUNTS.account_status:'Inactive'})
        self._session.commit()
        return

    def block_account(self, account_id):
        id = self.user_id()
        self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == id, ACCOUNTS.id == account_id)).update({ACCOUNTS.account_status:'Blocked'})
        self._session.commit()
        return


    def activate_account(self, account_id):
        id = self.user_id()
        self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == id, ACCOUNTS.id == account_id)).update({ACCOUNTS.account_status:'Active'})
        self._session.commit()
        return

    def reset_withdrawals(self, account_id):
        id = self.user_id()
        self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == id, ACCOUNTS.id == account_id)).update({ACCOUNTS.withdrawal_limit:0})
        self._session.commit()
        return

    def reset_savings_transfer(self, account_id):
        id = self.user_id()
        self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == id, ACCOUNTS.id == account_id)).update({ACCOUNTS.transfer_limit:0})
        self._session.commit()
        return
