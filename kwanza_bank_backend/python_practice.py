from account_mng import ACCOUNT_MNG
from transaction_mng import TRANS_MNG
from account_creation import NEW_ACCOUNT
import datetime as dt
new_customer = NEW_ACCOUNT()
#
# new_customer.second_account('1','elle_singer@gmail.com')

# new_customer.second_account('2','cj_gwenver@gmail.com')

# new_customer.customer("elle_singer@gmail.com", f_name = 'Elle', l_name = 'Singer',
# dob = '1995-03-09', ssn = '12335678', driver_license = 'DL222437', alternative_email = 'es@lsu.edu',
# phone_number = '9802345627')
#
# new_customer.address("elle_singer@gmail.com",unit_number='Room B', street_name='10th Street',city='Amarillo',
# postal_code='79123', state='TX')
#
# new_customer.account("elle_singer@gmail.com", 'Checking')
#
# new_customer.customer("cj_gwenver@gmail.com", f_name = 'Cristiano', l_name = 'Napoleao',
# dob = '1994-02-19', ssn = '12345678', driver_license = 'DL221937', alternative_email = 'bad_cj@mich.edu',
# phone_number = '7453728890')
#
# new_customer.address("cj_gwenver@gmail.com",unit_number='Room B', street_name='10th Street',city='Amarillo',
# postal_code='79123', state='TX')
#
# new_customer.account("cj_gwenver@gmail.com", 'Checking')

# a = ACCOUNT_MNG('cj_gwenver@gmail.com','2650')
# a.update_pin('1248')



# t.withdrawal_trans(100)
#  [(%y/%Y – Year), (%a/%A- weekday), (%b/%B- month), (%d - day of month)]
# print(dt.datetime.now())

t = TRANS_MNG(2,'9233','cj_gwenver@gmail.com')
# t.deposit_trans(1950)
t.intrabank_transf(200, 1, "elle_singer@gmail.com")
