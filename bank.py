from random import randint
from accounts import ACCOUNT, SAVINGS_ACCOUNT, CUSTOMER
import pymysql.cursors

def initialize_cursor():
    cur = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        db='kwanzaBank',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
     )
    return cur

class BANK():

    def __init__(self):
        # initializes and loads the accounts into a mysql DB
        self.connection = initialize_cursor()
        self.checking_account = ACCOUNT()
        self.savings_account = SAVINGS_ACCOUNT()
        self.customer_info = CUSTOMER


    # def __str__(self):
    #     #returns the general information of all accounts
    #     return "\n".join(map(str, self._checkingAccounts.values())) + "\n\n" +"\n".join(map(str,self._savingsAccounts.values()))

    def add_to_customer(self, f_name, l_name, date_of_birth, address, phone_number, ssn, driver_license, email):
        """Adding costumer info to costumer table"""
        c_info = self.customer_info(f_name, l_name, date_of_birth, address, phone_number, ssn, driver_license, email)
        with self.connection.cursor() as cursor:
            add_customer_table = "INSERT INTO `CUSTOMERS`(`firstName`, `lastName`, `dob`, `address`,`driver_license_id`, `email`, `status`, `customer_pin`, `phone_number`,`ssn`) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(add_customer_table,(c_info._f_name, c_info._l_name, c_info._date_of_birth, c_info._address, c_info._driver_license, c_info._email, c_info._status,  c_info._pin_number, c_info._phone_number, c_info._ssn))
        self.connection.commit()
        self.connection.close()
        return

    def add_checking_to_account(self, email_customer, customer_id):
        """Adding new checking account for costumer"""
        c_account = self.checking_account
        with self.connection.cursor() as cursor:
            email = email_customer
            id =  customer_id
            add_account_table = "INSERT INTO `ACCOUNTS`(`accountType`, `status`, `email`, `customer_id`) VALUES( %s, %s, %s, %s);"
            cursor.execute(add_account_table,(c_account.get_account_type(), c_account.get_status(), email, id))
        self.connection.commit()
        self.connection.close()
        return

    def add_savings_to_account(self, email_customer, customer_id):
        """Adding new savings account for costumer"""
        s_account = self.savings_account
        with self.connection.cursor() as cursor:
            email = email_customer
            id =  customer_id
            add_account_table = "INSERT INTO `ACCOUNTS`(`accountType`, `status`, `email`, `customer_id`) VALUES( %s, %s, %s, %s);"
            cursor.execute(add_account_table,(s_account.get_account_type(), s_account.get_status(), email, id))
        self.connection.commit()
        self.connection.close()
        return

    def remove_checking_accounts(self, customer_email):
        """remove checking account from accounts table"""
        with self.connection.cursor() as cursor:
            email = customer_email
            remove_account_table = "DELETE FROM ACCOUNTS WHERE `email` = %s AND `accountType` = `Checking`"
            past_costumer = "UPDATE CUSTOMERS SET status = %s WHERE `email` =%s"
            cursor.execute(remove_account_table,(email))
            cursor.execute(past_costumer,('Checking Account Inactive', email))
        self.connection.commit()
        self.connection.close()
        return

    def remove_savings_accounts(self, customer_email):
        """remove savings account from accounts table"""
        with self.connection.cursor() as cursor:
            email = customer_email
            remove_account_table = "DELETE FROM ACCOUNTS WHERE `email` = %s AND `accountType` = `Savings`"
            past_costumer = "UPDATE CUSTOMERS SET status = %s WHERE `email` =%s"
            cursor.execute(remove_account_table,(email))
            cursor.execute(past_costumer,('Savings Account Inactive', email))
        self.connection.commit()
        self.connection.close()
        return

    def remove_all_accounts(self, customer_email):
        """remove all accounts from accounts table"""
        with self.connection.cursor() as cursor:
            email = customer_email
            remove_account_table = "DELETE FROM ACCOUNTS WHERE `email` = %s"
            past_costumer = "UPDATE CUSTOMERS SET `status` = %s WHERE `email` =%s"
            cursor.execute(remove_account_table,(email))
            cursor.execute(past_costumer,('All Accounts Inactive',email))
        self.connection.commit()
        self.connection.close()
        return


    def block_checking(self, email):
        """Grabs email from session and changes status to block"""
        with self.connection.cursor() as cursor:
            customer_email = email
            new_status = "UPDATE ACCOUNTS SET status = `Blocked` WHERE email = %s AND accountType = `Checking`;"
            cursor.execute(new_status,(customer_email))
        self.connection.commit()
        self.connection.close()
        return

    def block_savings(self, email):
        """Grabs email from session and changes status to block"""
        with self.connection.cursor() as cursor:
            customer_email = email
            new_status = "UPDATE ACCOUNTS SET status = `Blocked` WHERE email = %s AND accountType = `Savings`"
            cursor.execute(new_status,(customer_email))
        self.connection.commit()
        self.connection.close()
        return

    def unblock_checking(self, email):
        """Grabs email from session and changes status to unblock"""
        with self.connection.cursor() as cursor:
            customer_email = email
            new_status = "UPDATE ACCOUNTS SET status = `Unblocked` WHERE email = %s AND accountType = `Checking`"
            cursor.execute(new_status,(customer_email))
        self.conection.commit()
        self.conection.close()
        return

    def unblock_savings(self, email):
        """Grabs email from session and changes status to unblock"""
        with self.connection.cursor() as cursor:
            customer_email = email
            new_status = "UPDATE ACCOUNTS SET status = `Unblocked` WHERE email = %s AND accountType = `Savings`"
            cursor.execute(new_status,(customer_email))
        self.connection.commit()
        self.connection.close()
        return

    def unblock_withdrawals(self):
        self.savings_account.reset()
        return

bank = BANK()
# bank.add_to_customer('Cristiano', 'Napoleao','1994-08-09','8710 10th st, Lubbock, 79416, TX','8062523647','123123123','DL162534','cjnapoleao@gmail.com')
# bank.add_checking_to_account('cjnapoleao@gmail.com','2')
bank.remove_all_accounts('cjnapoleao@gmail.com')
