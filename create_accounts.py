from com.abc.banking.account import Account
from com.abc.banking.overdrafterror import OverdraftError
from traceback import print_exc

a = Account(acc_name='mehul', acc_type='Savings', acc_balance=10000)

try:
    ub = a.withdraw(900)
except OverdraftError:
    print_exc()
except ValueError:
    print_exc()
else:
    print(ub)

''' try:
    ub = a.withdraw(-4500)
except Exception:
    # catch all exception block
    print_exc() ''' # avoid it