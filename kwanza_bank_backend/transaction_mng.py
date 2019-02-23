from sqlalchemy_declarative import CUSTOMER, ACCOUNTS, TRANSACTIONS, engine, Session, session
from sqlalchemy import and_


class TRANS_MNG():

    def __init__(self, account_number, pin, email):
        self._engine = engine
        self._Session = Session
        self._session = self._Session()
        self._account_number = account_number
        self._pin = pin
        self._email = email
        self._user = self.active_user()

    def active_user(self):
        try:
            user_obj = self._session.query(CUSTOMER).filter(and_(CUSTOMER.email == self._email,
            CUSTOMER.pin_number == self._pin)).first()
            id = user_obj.id
            return user_obj

        except Exception:
            return None


    def acct_tb_query(self, user_id, account_num):
        acct_query = self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.customer_id == user_id, ACCOUNTS.id == account_num))
        return acct_query

    def trans_record(self, acct_id , trans_description, trans_amount, status, trans_receiver_account_id = None):
        new_transaction = TRANSACTIONS(account_id = acct_id, description = trans_description, amount = trans_amount,
            transaction_status = status, receiver_account_id = trans_receiver_account_id)
        self._session.add(new_transaction)
        self._session.commit()
        return

    def account_status(self):
        acct_obj = self.acct_tb_query(self._user.id, self._account_number).first()
        status = acct_obj.account_status.title()
        return status

    def deposit_trans(self, amount):

        if self.account_status() == "Inactive" or self.account_status() == "Blocked":

            description = ("Unable to make deposit $%f: %s Account." % (amount, self.account_status()))
            status = "Denied"
            self.trans_record(self._account_number, description, amount, status)
            return

        elif amount > 0:
            acct_obj = self.acct_tb_query(self._user.id, self._account_number).first()
            self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(acct_obj.balance) + float(amount)})
            self._session.commit()
            description = ("Deposit Value: $%f." % (amount))
            status = "Approved"
            self.trans_record(self._account_number, description, amount, status)
            return

    def withdrawal_trans(self, amount):
        if self.account_status() == "Inactive" or self.account_status() == "Blocked":
            description = ("Unable to make withdrawal $%f: %s Account." % (amount, self.account_status()))
            status = "Denied"
            self.trans_record(self._account_number, description, amount, status)
            return

        else:
            account_obj = self.acct_tb_query(self._user.id, self._account_number).first()

            if account_obj.balance <= 0:
                description = ("Unable to make withdrawal $%f: Insufficient Funds." % (amount))
                status = "Denied"
                self.trans_record(self._account_number, description, amount, status)
                return

            elif account_obj.account_type == "Savings":

                if account_obj.withdrawal_limit == 3:
                    description = ("Unable to make withdrawal: Withdrawal Limit Reached.")
                    status = "Denied"
                    self.trans_record(self._account_number, description, amount, status)
                    return

                elif amount > 0:
                    self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(account_obj.balance) - float(amount)})
                    self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.withdrawal_limit:ACCOUNTS.withdrawal_limit + 1})
                    self._session.commit()
                    description = ("Withdrawal Value: $%f." % (amount))
                    status = "Approved"
                    self.trans_record(self._account_number, description, amount, status)
                    return
            else:
                self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(account_obj.balance) - float(amount)})
                self._session.commit()
                description = ("Withdrawal Value: $%f." % (amount))
                status = "Approved"
                self.trans_record(self._account_number, description, amount, status)
                return

    def check_to_savings(self, amount, receiv_account_num):

        if self.account_status() == "Inactive" or self.account_status() == "Blocked":
            description = ("Unable To Transfer: %s Account." % (self.account_status()))
            status = "Denied"
            self.trans_record(self._account_number, description, amount, status, receiv_account_num)
            return

        else:
            account_obj = self.acct_tb_query(self._user.id, self._account_number).first()
            receiver_acct_obj = self.acct_tb_query(self._user.id, receiv_account_num).filter(ACCOUNTS.customer_email == self._email).first()

            if account_obj.balance <= 0:
                description = ("Unable to make Transfer: Insufficient Funds.")
                status = "Denied"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            elif receiver_acct_obj != None and receiver_acct_obj.account_type == 'Savings' and account_obj.account_type == "Checking" and amount > 0:
                self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(account_obj.balance) - float(amount)})
                self.acct_tb_query(self._user.id, receiv_account_num).filter(ACCOUNTS.customer_email == self._email).update({ACCOUNTS.balance:float(receiver_acct_obj.balance) + float(amount)})
                self._session.commit()
                description = (("Transfer Complete: $%d." % amount))
                status = "Approved"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            else:
                description = ("Transfer Incomplete, Invalid Savings Account.")
                status = "Denied"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

    def savings_to_check(self, amount, receiv_account_num):
        if self.account_status() == "Inactive" or self.account_status() == "Blocked":
            description = ("Unable To Transfer: %s Account." % (self.account_status()))
            status = "Denied"
            self.trans_record(self._account_number, description, amount, status, receiv_account_num)
            return

        else:
            account_obj = self.acct_tb_query(self._user.id, self._account_number).first()
            receiver_acct_obj = self.acct_tb_query(self._user.id, receiv_account_num).filter(ACCOUNTS.customer_email == self._email).first()

            if account_obj.balance <= 0:
                description = ("Unable to make Transfer: Insufficient Funds.")
                status = "Denied"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            elif receiver_acct_obj != None and receiver_acct_obj.transfers_limit <= 6 and receiver_acct_obj.account_type == 'Checking' and account_obj.account_type == "Savings" and amount > 0:
                self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(account_obj.balance) - float(amount)})
                self.acct_tb_query(self._user.id, receiv_account_num).filter(ACCOUNTS.customer_email == self._email).update({ACCOUNTS.balance:float(receiver_acct_obj.balance) + float(amount)})
                self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.transfers_limit:ACCOUNTS.transfers_limit + 1})
                self._session.commit()
                transfers_left = 6 - account_obj.transfers_limit
                description = ("Transfer Complete. %d transfers left for this month." % (transfers_left))
                status = "Approved"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            else:
                return None

    def intrabank_transf(self, amount, receiv_account_num, receiver_email):

        if self.account_status() == "Inactive" or self.account_status() == "Blocked":
            description = ("Unable To Transfer: %s Account." % (self.account_status()))
            status = "Denied"
            self.trans_record(self._account_number, description, amount, status, receiv_account_num)
            return

        else:

            account_obj = self.acct_tb_query(self._user.id, self._account_number).first()
            receiver_acct_obj = self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.id == receiv_account_num, ACCOUNTS.customer_email == receiver_email, ACCOUNTS.customer_id != self._user.id)).first()

            if account_obj.balance <= 0:
                description = ("Unable to make Transfer to Account Number# %d due to Insufficient Funds." % receiver_acct_obj.id)
                status = "Denied"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            elif receiver_acct_obj != None and receiver_acct_obj.account_type != 'Savings' and amount > 0:
                self.acct_tb_query(self._user.id, self._account_number).update({ACCOUNTS.balance:float(account_obj.balance) - float(amount)})
                self._session.query(ACCOUNTS).filter(and_(ACCOUNTS.id == receiv_account_num, ACCOUNTS.customer_email == receiver_email, ACCOUNTS.customer_id != self._user.id)).update({ACCOUNTS.balance:float(receiver_acct_obj.balance) + float(amount)})
                self._session.commit()
                description = ("Money Transfered to Account Number# %d." % receiver_acct_obj.id)
                status = "Approved"
                self.trans_record(self._account_number, description, amount, status, receiv_account_num)
                return

            else:
                return None
