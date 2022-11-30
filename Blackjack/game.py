"""
Module contains logic for how the game is played.
"""
# pylint: disable = e0611
# pylint: disable = c0200
# pylint: disable = e1102
from deck_info import Deck
from player_info import Player
from gambling_logic import Gambling

# Game Setup
if (
    input("Welcome to Blackjack, would you like to play? [Y/N]\n")
    .upper()
    .startswith("Y")
    is False
):
    raise SystemExit("Have a nice day!")

name = input("What is your name?\n")

player_one = Player(name)
npc_dealer = Player("Dealer")

while True:
    try:
        starting_balance = int(input("What is your starting balance?\n"))
        if starting_balance <= 0:
            print("Please enter a value greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

gambling = Gambling(starting_balance)

print(f"Okay, {player_one.name} {gambling}")

GAME_ON = True

while GAME_ON:

    new_deck = Deck()
    new_deck.shuffle()
    player_one.all_cards = []
    npc_dealer.all_cards = []

    # Starting Bets
    while True:
        try:
            bet_amount = int(input("What is your bet?\n"))
            if bet_amount <= 0:
                print("Please enter a value greater than 0.")
            else:
                if gambling.bet(bet_amount) is True:
                    break
        except ValueError:
            print("Please enter a valid number.")

    # Deal Cards
    for x in range(2):
        player_one.add_cards(new_deck.deal_one())
        npc_dealer.add_cards(new_deck.deal_one())

    # Find the values of all items in hand for P1.
    player_one_hand = []
    for i in range(0, len(player_one.all_cards)):
        player_one_hand.append(player_one.all_cards[i].value)

    print(player_one)
    print(player_one_hand)

    # Find the values of all items in hand for Dealer.
    dealer_hand = []
    for i in range(0, len(npc_dealer.all_cards)):
        dealer_hand.append(npc_dealer.all_cards[i].value)

    print(npc_dealer)
    print(dealer_hand)

    # These values determine if a player has stayed.
    # If so, they no longer draw cards and forfeit their turn
    PLAYER_STAY = False
    DEALER_STAY = False

    # While Loop for player action. If hit, deals another card. Dealer follows.
    while True:

        # Perform checks for blackjack
        if sum(player_one_hand) == 21 and sum(dealer_hand) == 21:
            print("Draw! Both players got Blackjack!")
            gambling.balance += bet_amount
            print(f"{player_one.name} {gambling}")
            break
        if sum(player_one_hand) == 21:
            print(f"Congratulations {player_one.name}! You got Blackjack!")
            gambling.balance += bet_amount * 2
            print(f"{player_one.name} {gambling}")
            break
        if sum(dealer_hand) == 21:
            print(f"Sorry {player_one.name}, the Dealer got Blackjack.")
            print(f"{player_one.name} {gambling}")
            break
        if PLAYER_STAY is True and DEALER_STAY is True:
            if sum(player_one_hand) == 21 and sum(dealer_hand) == 21:
                print("Draw!")
                gambling.balance += bet_amount
                print(f"{player_one.name} {gambling}")
                break
            if sum(player_one_hand) > sum(dealer_hand):
                print(f"{player_one.name} has won!")
                gambling.balance += bet_amount * 2
                print(f"{player_one.name} {gambling}")
                break
            if sum(player_one_hand) < sum(dealer_hand):
                print(
                    f"{npc_dealer.name} has won! Better luck next time, {player_one.name}!"
                )
                break

        # Hit/Stay input.
        if PLAYER_STAY is False:
            hit_or_stay = input("Do you want to hit or stay\n").lower()
            if hit_or_stay.startswith("h") is True:
                player_one.add_cards(new_deck.deal_one())
                player_one_hand.append(player_one.all_cards[-1].value)
            elif hit_or_stay.startswith("h") is False:
                PLAYER_STAY = True

        # If one value = 11 and sum > 21, replace 11 with 1.
        if (sum(player_one_hand) > 21) and (11 in player_one_hand):
            player_one_hand.remove(11)
            player_one_hand.append(1)
        print(
            f"{player_one.name}'s new hand is: {player_one_hand}. Total: {sum(player_one_hand)}"
        )

        # Check for busts.
        if sum(player_one_hand) > 21:
            print(f"{player_one.name} has busted!")
            print(f"{player_one.name} {gambling}")
            break

        # Safety check for 21.
        if sum(player_one_hand) == 21:
            print(f"Congratulations {player_one.name}! You got Blackjack!")
            gambling.balance += bet_amount * 2
            print(f"{player_one.name} {gambling}")
            break

        print("Dealer's turn.")

        if DEALER_STAY is False:
            # Dealer's must draw, if less than 17.
            if sum(dealer_hand) < 17:
                npc_dealer.add_cards(new_deck.deal_one())
                dealer_hand.append(player_one.all_cards[-1].value)
            # Dealer's automatically stay above 17 or higher.
            if 16 < sum(dealer_hand) < 21:
                DEALER_STAY = True
        if (sum(dealer_hand) > 21) and (11 in dealer_hand):
            dealer_hand.remove(11)
            dealer_hand.append(1)
        print(
            f"{npc_dealer.name}'s new hand is: {dealer_hand}. Total: {sum(dealer_hand)}"
        )

        # Check for busts.
        if sum(dealer_hand) > 21:
            print(f"{npc_dealer.name} has busted!")
            gambling.balance += bet_amount * 2
            print(f"{player_one.name} {gambling}")
            break

    # If balance is 0 and not all in, game over.
    if gambling.balance <= 0:
        print("You're broke! Game Over!")
        GAME_ON = False

    elif input("Do you want to keep playing?\n").lower().startswith("n"):
        GAME_ON = False
