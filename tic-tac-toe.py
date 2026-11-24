
import math

HUMAN = "X"
AI = "O"
EMPTY = " "

board = [EMPTY] * 9

def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(
            board[j] if board[j] != EMPTY else str(j + 1)
            for j in range(i, i + 3)
        ))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        all(board[i] == player for i in line)
        for line in winning_positions
    )

def is_draw():
    return EMPTY not in board

def minimax(is_maximizing):
    if check_winner(AI):
        return 1
    if check_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(False)
                board[i] = EMPTY
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(True)
                board[i] = EMPTY
                best_score = min(score, best_score)

        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = AI
        print("AI selected position:", best_move + 1)

def human_move():
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1

            if 0 <= position < 9 and board[position] == EMPTY:
                board[position] = HUMAN
                break

            print("Invalid or occupied position. Try again.")

        except ValueError:
            print("Please enter a number from 1 to 9.")

def play_game():
    print("WELCOME TO TIC-TAC-TOE AI!")
    print("You are X and AI is O.")

    while True:
        print_board()
        human_move()

        if check_winner(HUMAN):
            print_board()
            print("Congratulations! You win!")
            break

        if is_draw():
            print_board()
            print("Game is a draw!")
            break

        ai_move()

        if check_winner(AI):
            print_board()
            print("AI wins! Better luck next time.")
            break

        if is_draw():
            print_board()
            print("Game is a draw!")
            break

    print("Thanks for playing!")

play_game()
