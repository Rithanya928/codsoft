import tkinter as tk
import math

# Initialize board
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # Human starts first

# Colors and styles
BG_COLOR = "#222831"   # Dark background
FG_COLOR = "#EEEEEE"   # Light text
BTN_COLOR = "#00ADB5"  # Blue buttons
WIN_COLOR = "#76FF03"  # Green for win highlight

# Function to check winner
def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if board is full
def is_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Minimax Algorithm for AI
def minimax(is_maximizing):
    if check_winner('X'): return -1
    if check_winner('O'): return 1
    if is_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

# AI selects the best move
def best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'O'
        buttons[move[0]][move[1]].config(text="O", fg="red", state="disabled")
        check_game_status()

# Handle player move
def player_move(row, col):
    global current_player
    if board[row][col] == ' ' and current_player == 'X':
        board[row][col] = 'X'
        buttons[row][col].config(text="X", fg="white", state="disabled")
        check_game_status()
        if not check_winner('X') and not is_full():
            current_player = 'O'
            best_move()
            current_player = 'X'

# Check for game over
def check_game_status():
    if check_winner('X'):
        status_label.config(text="🎉 You win!", fg=WIN_COLOR)
        highlight_winning_moves('X')
        disable_all_buttons()
    elif check_winner('O'):
        status_label.config(text="💀 AI wins!", fg="red")
        highlight_winning_moves('O')
        disable_all_buttons()
    elif is_full():
        status_label.config(text="🤝 It's a draw!", fg="yellow")

# Highlight winning moves
def highlight_winning_moves(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row win
            for j in range(3):
                buttons[i][j].config(bg=WIN_COLOR)
        if all(board[j][i] == player for j in range(3)):  # Column win
            for j in range(3):
                buttons[j][i].config(bg=WIN_COLOR)
    if all(board[i][i] == player for i in range(3)):  # Diagonal win
        for i in range(3):
            buttons[i][i].config(bg=WIN_COLOR)
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal win
        for i in range(3):
            buttons[i][2 - i].config(bg=WIN_COLOR)

# Disable all buttons after game over
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

# Reset the game
def reset_game():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    status_label.config(text="Your Turn (X)", fg=FG_COLOR)
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", fg="black", bg=BTN_COLOR, state="normal")

# Create the GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.configure(bg=BG_COLOR)

# Status label
status_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR)
status_label.grid(row=0, column=0, columnspan=3, pady=10)

# Buttons for the grid
buttons = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root, text=" ", font=("Arial", 20), width=5, height=2,
            bg=BTN_COLOR, fg="black", activebackground="gray",
            command=lambda r=i, c=j: player_move(r, c)
        )
        buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)

# Reset button
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 12), bg="#393E46", fg="white", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the GUI
root.mainloop()

