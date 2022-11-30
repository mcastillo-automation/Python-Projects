"""
Player gambling logic. Allows player to bet/deposit
"""


class Gambling:
    """
    First, let's instantiate the class. We need the following:
    - create a balance variable. Need to add funds.
    - create a hand to play with. I think it's all_cards
    """

    def __init__(self, balance, deposit_amount=0, bet_amount=0):
        self.balance = balance
        self.deposit_amount = deposit_amount
        self.bet_amount = bet_amount

    def deposit(self, deposit_amount):
        """
        In theory, this should allow me to deposit an initial starting balance.
        """
        self.deposit_amount = deposit_amount
        print(f"Deposit Accepted. New balance is ${self.balance}")

    def bet(self, bet_amount):
        """
        In theory, this should allow the user to set a bet.
        Should only prompt player response if it's an "all-in" situation.
        """
        self.bet_amount = bet_amount
        if self.balance < bet_amount:
            return False
        if self.balance == bet_amount:
            while True:
                player_response = input(
                    "Bet amount is equal to current balance. Go all in? Y/N\n"
                ).lower()
                if player_response == "y":
                    self.balance -= self.bet_amount
                    print(f"Understood. Balance is now: ${self.balance}")
                    return True
                return False
        else:
            self.balance -= self.bet_amount
            print(f"Bet accepted. Balance is now: ${self.balance}")
            return True

    def __str__(self):
        return f"has a balance of: ${self.balance}"
