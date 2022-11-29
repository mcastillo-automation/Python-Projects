"""
This module will contain the player class, which will handle player behavior.
"""
class Player:
    """
    Will be creating player logic:
    * Removing a card from top of hand
    * Adding card(s) to bottom of hand.
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """
        Function to remove card at index 0 i.e top of hand.
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """
        Logic to add cards to hand via append (single) or extend (multiple).
        First, need to determine if multiple by checking for lists. If single, append.
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
