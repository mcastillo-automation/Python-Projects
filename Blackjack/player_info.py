"""
Player needs a balance. Print running total of cards/values.
"""


class Player:
    """
    First, let's instantiate the class. We need the following:
    - create a hand to play with. Var = all_cards
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        """
        Add logic to add cards to all_cards array.
        """
        self.all_cards.append(new_cards)

    def __str__(self):
        converted_hand = list(map(str, self.all_cards))
        return f"{self.name} has {len(self.all_cards)} cards in hand. Cards are: {', '.join(converted_hand)}"
