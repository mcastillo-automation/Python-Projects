"""
This module will contain the actual game logic for our War game.
"""
# pylint: disable = e0611
from deck_info import Deck
from player_info import Player

# Game setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

GAME_ON = True

ROUND_NUM = 0

while GAME_ON:
    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Player Two Wins!")
        GAME_ON = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Player One Wins!")
        GAME_ON = False
        break

    # Continue new round.
    player_one_cards = [player_one.remove_one()]

    player_two_cards = [player_two.remove_one()]

    AT_WAR = True

    while AT_WAR:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            AT_WAR = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            AT_WAR = False

        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player Two Wins!")
                GAME_ON = False
                break

            if len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One Wins!")
                GAME_ON = False
                break

            for num in range(3):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
