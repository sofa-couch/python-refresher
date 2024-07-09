# Self goes to stack --> permenant
# non goes to heat --> temporary


class bank_account(name=None, number=0):

    def __init__(self, name, number):
        self._balance = 0
        self._name = name
        self._accnum = number

    def withdraw(self, val):
        if val != int(val):
            return "Error: withdrawal ammount is not an integer"
        elif val > self._balance:
            return "Error: withdrawal cannot be greater than account balance"
        else:
            self._balance -= val
        return self.balance

    def deposit(self, val):
        if val != int(val):
            return "Error: deposit ammount is not an integer"
        elif val > 10000:
            return "Error: deposit ammount has exeeded its maximum (10,000)"
        else:
            self._balance += val
        return self._balance

    def balance_output(self, balance):
        print(f"Current balance: {self._balance}")
