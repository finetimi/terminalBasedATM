import unittest as ut, transaction_mng as tm, account_creation as ac, account_mng as am
from sqlalchemy_declarative import CUSTOMER, ACCOUNTS, TRANSACTIONS, engine, Session, session

new_account = ac.NEW_ACCOUNT()
acct_mng = am.ACCOUNT_MNG()
trans_mng = tm.TRANS_MNG()

class SqlAlchemyObjTestCase(ut.TestCase):

    def __init__(self, account_number, pin, email):
        self._engine = engine
        self._Session = Session
        self._session = self._Session()
        self._account_number = account_number
        self._pin = pin
        self._email = email
        self._user = .active_user()
