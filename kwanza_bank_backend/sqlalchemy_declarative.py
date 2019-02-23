from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, DateTime, Index, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
import mysql.connector

engine = create_engine("mysql+mysqlconnector://root:12345678@localhost/kwanza_bank")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class CUSTOMER(Base):
    __tablename__ = 'customers'
    id = Column('id',Integer, primary_key = True, autoincrement = True, nullable = False)
    f_name = Column('first_name',String(20), nullable = False)
    l_name = Column('last_name', String(20), nullable = False)
    dob = Column('dob', Date, nullable = False)
    ssn = Column('ssn', String(9), nullable = False, unique = True)
    driver_license =  Column('driver_license', String(15), unique = True, nullable = False)
    pin_number = Column('pin_number', Integer, nullable = False)
    email = Column('email', String(100), nullable = False, unique = True)
    alternative_email = Column('alternative_email', String(100), unique = True)
    phone_number = Column('phone_number', String(20), nullable = False, unique = True)
    status = Column('status', String(150), nullable = False, default = 'Active Customer')
    addresses = relationship("ADDRESS", backref = 'customers', cascade_backrefs = True, cascade = "all, delete, delete-orphan")
    accounts = relationship("ACCOUNTS", backref='customers', cascade_backrefs = True, cascade="all, delete, delete-orphan")


class ADDRESS(Base):
    __tablename__ = 'addresses'
    id = Column('id', Integer,autoincrement = True, primary_key = True, nullable =  False)
    customer_id = Column('customer_id', Integer, ForeignKey('customers.id', onupdate="cascade", ondelete="cascade"), nullable =  False)
    unit_number = Column('unit', String(10), nullable = False)
    street_name = Column('street', String(150), nullable = False)
    city =  Column('city', String(50), nullable = False)
    postal_code = Column('postal_code', String(5), nullable = False)
    state = Column('state', String(2), nullable = False)


class ACCOUNTS(Base):
    __tablename__ = 'accounts'
    id = Column('account_number', Integer, autoincrement = True, primary_key = True, nullable = False)
    customer_id = Column('customer_id', Integer, ForeignKey('customers.id', onupdate="cascade", ondelete="cascade"), nullable = False)
    account_type = Column('account_type', String(10), nullable = False)
    customer_email = Column('account_email', String(100), nullable = False)
    balance = Column('balance', Numeric(19,4), nullable = False, default = 0.0000000000)
    withdrawal_limit = Column('withdrawal_limit', Integer, default = 0)
    transfers_limit = Column('transfer_limit', Integer, default = 0)
    account_status = Column('status', String(10), nullable = False, default = 'active')
    transactions = relationship("TRANSACTIONS", uselist=False)



class TRANSACTIONS(Base):
    __tablename__ = 'transactions'
    id = Column('id', Integer, autoincrement = True, primary_key = True)
    account_id = Column('account_id', Integer, ForeignKey('accounts.account_number'), nullable = False)
    trans_date_time = Column('date_time', DateTime, nullable = False, default = datetime.now())
    amount = Column('amount', Numeric(19,4), nullable = False)
    transaction_status = Column('status', String(15), nullable = False)
    description = Column('description', String(200), nullable = False)
    receiver_account_id = Column('receiver_account_id', Integer)
    accounts = relationship("ACCOUNTS")

Base.metadata.create_all(engine)
