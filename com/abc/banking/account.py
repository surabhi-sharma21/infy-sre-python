from .overdrafterror import OverdraftError

class Account:
    min_balance = 1000

    def __init__(self, acc_name, acc_type, acc_balance):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_balance = acc_balance
    
    def withdraw(self, amt):
        print('Transaction starts..')

        try:
            if amt <= 0:
                raise ValueError('Amt passed needs to be greater than 0')
            if self.acc_balance - amt < Account.min_balance:
                raise OverdraftError('Account balance going below {0}'.format(Account.min_balance))
            
            self.acc_balance -= amt
            return self.acc_balance
        finally:
            # stmts will execute irrespective of whatever happens in the try block
            # 1 ValueError
            # 2 OverdraftError
            # 3. Success and it returns
            print('Transaction ends..')