# Author: Michael Castillo
# pylint: disable=missing-module-docstring


def launch_ttt_game():
    """Launches the tic-tac-toe game. Player 1 will be X. Player 2 will be O. Have fun!"""
    ttt_values = ["   "] * 9
    p_1 = "Player 1"
    p_2 = "Player 2"
    input_message = (
        ": What value(1-9) are you updating? Enter 'Exit' if you would like to quit.\n"
    )
    exit_message = "Thank you for playing. Have a good day."
    overwrite_message = "Please do not overwrite an existing value."
    error_message = "That is an invalid value. Please enter a number from 1-9"

    def display_ttt_board():
        print(
            f"""{ttt_values[0]}|{ttt_values[1]}|{ttt_values[2]}\n-----------\
              \n{ttt_values[3]}|{ttt_values[4]}|{ttt_values[5]}\n-----------\
              \n{ttt_values[6]}|{ttt_values[7]}|{ttt_values[8]}"""
        )

    def game_complete_check(board, mark):

        return (
            (board[6] == mark and board[7] == mark and board[8] == mark)
            or (board[3] == mark and board[4] == mark and board[5] == mark)
            or (board[0] == mark and board[1] == mark and board[2] == mark)
            or (board[6] == mark and board[3] == mark and board[0] == mark)
            or (board[7] == mark and board[4] == mark and board[1] == mark)
            or (board[8] == mark and board[5] == mark and board[2] == mark)
            or (board[6] == mark and board[4] == mark and board[2] == mark)
            or (board[8] == mark and board[4] == mark and board[0] == mark)
        )

    def is_board_full(board):
        for i in range(0, 9):
            if board[i] == "   ":
                return False
        return True

    def player1_input():
        while True:
            try:
                p1_input = input(p_1 + input_message)  # Player 1's Turn
                exit_test = p1_input.capitalize()  # Exit test. To determine shutdown.
                if exit_test == "Exit":
                    print(exit_message)
                    return True
                int_conversion_p1 = int(
                    p1_input
                )  # Converting input to an integer, if no exit.
                array_lookup_p1 = int_conversion_p1 - 1
                if int_conversion_p1 <= 0:  # Checking for negative values.
                    print(error_message)
                elif (
                    ttt_values[array_lookup_p1] == "   "
                ):  # If space available, write input to value. Else error.
                    ttt_values[array_lookup_p1] = " X "
                    break
                else:
                    print(overwrite_message)
            except ValueError:
                print(error_message)

    def player2_input():
        while True:
            try:
                p2_input = input(p_2 + input_message)  # Player 2's Turn. Repeat above.
                exit_test = p2_input.capitalize()
                if exit_test == "Exit":
                    print(exit_message)
                    return True
                int_conversion_p2 = int(p2_input)
                array_lookup_p2 = int_conversion_p2 - 1
                if int_conversion_p2 <= 0:
                    print(error_message)
                elif ttt_values[array_lookup_p2] == "   ":
                    ttt_values[array_lookup_p2] = " O "
                    break
                else:
                    print(overwrite_message)
            except ValueError:
                print(error_message)

    def welcome_message():
        welcome_message_text = "Welcome to Tic-Tac-Toe! Would you like to play? Enter Y/N\n"
        while True:
            start_input = input(welcome_message_text)
            response = start_input.capitalize()
            if response == "Y":
                return True
            if response == "N":
                print("Have a nice day!")
                return False
            print("Please enter Y/N")

    def replay():
        replay_message = "Do you want to play again? Enter Y/N.\n"
        while True:
            replay_input = input(replay_message)
            response = replay_input.capitalize()
            if response == "Y":
                return True
            if response == "N":
                print("Have a nice day!")
                return False
            print("Please enter Y/N")

    if not welcome_message():
        return
    while True:
        ttt_values = ["   "] * 9
        display_ttt_board()
        while True:

            if player1_input() is True:  # Player 1's turn
                return
            display_ttt_board()  # Display board to show status of game.

            if game_complete_check(ttt_values, " X ") is True:  # Is the game won?
                print(p_1 + " has won!")
                break
            if is_board_full(ttt_values) is True:  # Is there a tie?
                print("Game over! Nobody wins!")
                break

            if player2_input() is True:
                return
            display_ttt_board()

            if game_complete_check(ttt_values, " O ") is True:
                print(p_2 + " has won!")
                break
            if is_board_full(ttt_values) is True:
                print("Game over! Nobody wins!")
                break

        if not replay():
            break


launch_ttt_game()
