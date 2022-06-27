# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# credit_card.py

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt: the account identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = limit

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


# credit_card_tests.py

from credit_card import CreditCard

wallet = []
wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309" , 5000))

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print("Customer = ", wallet[c].customer)
    print("Bank = ", wallet[c].bank)
    print("Account = ", wallet[c].account)
    print("Limit = ", wallet[c].get_limit())
    print("Balance = ", wallet[c].get_balance())

    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print("New balance = ", wallet[c].get_balance())
    print()
