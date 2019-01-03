from random import randint

class CUSTOMER():

    """ Creating a class for costumer's personal information. """

    def __init__(self, f_name, l_name, date_of_birth, address, phone_number, ssn, driver_license, email, status = 'Active'):
        self._f_name = f_name
        self._l_name = l_name
        self._date_of_birth = date_of_birth
        self._address = address
        self._phone_number = phone_number
        self._driver_license = driver_license
        self._ssn = ssn
        self._pin_number = self.pin_generator()
        self._email = email
        self._status = status

    def pin_generator(self):
        # Generates random pin
        pin = ""
        for number in range(4):
            pin += str(randint(0,9))
        return pin

    def get_pin(self):
        """Get pin of account"""
        return self._pinNumber

    def change_status(self):
        """Upon removal of account, customer info will be kept and status will change"""
        self._status = "Inactive"
        return self._status

    def change_pin(self, new_pin):
        """Enables customer to change Pin"""
        self._pinNumber = new_pin
        return self._pinNumber

    def change_address(self, new_address):
        """ Mutal method: To change address of costumer in case he/she moves """
        self._address = new_address
        return self._address

    def change_phone_number(self, new_phone_number):
        """ Mutal method: To change phone number of costumer """
        self._phone_number = new_phone_number
        return self._phone_number

    def change_address(self, new_email):
        """ Mutal method: To change email of costumer """
        self._email = new_email
        return self._email

class ACCOUNT():
    """Initialize the code"""
    def __init__(self, balance = 0.0):
        self._balance = balance
        self._account_type = "Checking"
        self._block = False


    def get_balance(self):
        """Get the balance of account"""
        return self._balance


    def get_account_type(self):
        # Returns account type
        return self._account_type

    def get_status(self):
        if self._block == True:
            return "Blocked"
        return "Unblocked"


    def __str__(self):
        # Returns information of the account
        accounts += "Account Type:   " + self._account_type + "\n"
        accounts += "Balance:   " + "$" + str(self._balance) + "\n"
        if self._block == True:
            status = "Blocked"
        else:
            status = "Unblocked"
        accounts += "Status:   " + status + "\n"
        return accounts

    def block_account(self):
        """Condition changes value of class variable Block"""
        self._block = True
        return

    def unblock_account(self):
        """Condition changes value of class variable Block"""
        self._block = False
        return

    def deposit(self, amount):
        #checkers checks if account is blocked; balance is increased
        if self._block == True:
            return "1"
        elif amount < 0:
            print("Deposit needs to be bigger than 0")
        else:
            self._balance += amount


    def withdraw(self, amount):
        #balance gets reduced
        if self._block == True:
            return "1"
        elif amount < 0:
            print("Amount needs to be bigger than 0")
        elif self._balance < amount:
            print("Insufficient funds.")
        else:
            self._balance -= amount
        return None


class SAVINGS_ACCOUNT(ACCOUNT):
    RATE = 0.03
    LIMIT = 5

    def __init__(self, balance = 0.0):
        ACCOUNT.__init__(self, balance)
        self._count = 0
        self._account_type = "Savings"

    def compute_interest(self):
        #computes interest and it is deposit to account
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def withdraw(self, amount):
        #checkers checks if account is blocked; balance gets reduced
        if self._block == True:
            return "1"
        elif self._count == SavingsAccount.LIMIT:
            return ("\nReach the withdrawal limit. Contact bank.\n")
        else:
            withdrawal = Account.withdraw(self, amount)
            if withdrawal == None:
                    self._count += 1
            return ("\nAmount Withdrew: $%.2f" % amount + "\n")

    def reset(self):
        # Resets monthly withdrawals
        self._count = 0
