"""
This module contains the deck class, which is used for deck management.
"""
# pylint: disable = e0611
import random
from card_info import suits
from card_info import ranks
from card_info import Card


class Deck:
    """
    Instantiates a deck object.
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """
        Will be used to shuffle the instantiated deck object
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        Will be used to deal a singular card, and remove it from array
        """
        return self.all_cards.pop()
