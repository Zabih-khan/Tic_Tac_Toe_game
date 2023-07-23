import random

# --------------create a board.--------------
def board(game_input):
    # Display the Tic Tac Toe board with the given inputs.
    print(game_input[1] + '_|_' + game_input[2] + '_|_' + game_input[3])
    print(game_input[4] + '_|_' + game_input[5] + '_|_' + game_input[6])
    print(game_input[7] + '_|_' + game_input[8] + '_|_' + game_input[9])

# --------------Ask from the player to choose a marker.--------------
def player_input():
    # Prompt player 1 to choose 'X' or 'O' (case insensitive).
    marker = ''
    while marker not in ['X', 'O']:
        print()
        marker = input("Player 1: please choose your marker [X/O]: ").upper()
    return ('X', 'O') if marker == 'X' else ('O', 'X')

# --------------Assign the marker to the desired position on the board.--------------
def put_marker(game_input, marker, pos):
    # Set the marker ('X' or 'O') at the specified position on the board.
    game_input[pos] = marker

# --------------How to win the game, see the logic.--------------
def win(game_input, marker):
    # Check all possible winning combinations on the board.
    return ((game_input[1] == game_input[2] == game_input[3] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[7] == game_input[5] == game_input[3] == marker) or
            (game_input[1] == game_input[5] == game_input[9] == marker) or
            (game_input[1] == game_input[4] == game_input[7] == marker) or
            (game_input[2] == game_input[5] == game_input[8] == marker) or
            (game_input[3] == game_input[6] == game_input[9] == marker))

# --------------Choose random player.--------------
def choose_player():
    # Randomly choose a player to start the game (player 1 or player 2).
    player = random.randint(1, 2)
    if player == 1:
        return "player 1"
    else:
        return "player 2"

# --------------Check if the marker position is empty or not.--------------
def space(game_input, pos):
    # Check if the position on the board is empty (no 'X' or 'O').
    return game_input[pos] == ' '

# --------------Check if the full board is empty or not.--------------
def full_board_check(game_input):
    # Check if the entire board is filled with 'X' and 'O'.
    for i in range(1, 10):
        if space(game_input, i):
            return False
    return True

# --------------Choose the position.--------------
def player_choice(game_input):
    # Prompt the player to choose a position on the board (1-9) to place the marker.
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space(game_input, pos):
        print()
        pos = int(input("please choose your position (1-9) on Numpad:"))
    return pos

# --------------Ask the user to play again or not.--------------
def play_again():
    # Ask the player if they want to play again (Y for Yes, N for No).
    choice = input("Would you like to play again [Y/N]:")
    return choice.lower() == 'y'

# --------------Main code to run the game.--------------
if __name__ == '__main__':
    while True:
        the_board = [' '] * 10
        # -------call player_input to assign markers [X, O].-------
        player_1, player_2 = player_input()
        print(player_1 + " is player 1 sign")
        print(player_2 + " is player 2 sign")
        # -------Call choose_player().-------
        turn = choose_player()
        print()
        print(turn + " will play first.")
        # -------Ask the user to start the game.-------
        play_game = input("Are you Ready to play[Y/N]: ")
        if play_game.lower() != "y":
            break

        # Set the game state to continue (True) and start the game loop.
        game_on = True
        while game_on:
            # Display the current state of the board.
            board(the_board)

            # Determine the player's marker based on the current turn.
            player_marker = player_1 if turn == "player 1" else player_2

            # Ask the player to choose a position on the board to place the marker.
            position = player_choice(the_board)

            # Place the player's marker at the chosen position on the board.
            put_marker(the_board, player_marker, position)

            # Check if the player has won the game.
            if win(the_board, player_marker):
                # Display the board after the win and print the winner's name.
                board(the_board)
                print()
                print(f"{turn} has won!")
                # End the game loop by setting the game state to False.
                game_on = False
            # If no one has won yet, check if the game is tied (board is full).
            elif full_board_check(the_board):
                # Display the board and print a message for a tie game.
                board(the_board)
                print("Game Tie")
                # End the game loop by setting the game state to False.
                game_on = False
            # If the game is not over, switch the turn to the other player for the next move.
            else:
                turn = "player 2" if turn == "player 1" else "player 1"

        # Check if the players want to play again.
        if not play_again():
            # If not, exit the game loop and end the program.
            break
