import tkinter as tk

# Initialize GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Set default window size
root.geometry("600x600")
root.minsize(400, 400)

# Create header
header_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 24), fg="blue")
header_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()

# Initialize board
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create game frame
game_frame = tk.Frame(root)
game_frame.pack(expand=True)

# Create buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            game_frame, text="", font=("Arial", 32), height=2, width=5,
            bg="white", activebackground="lightgray",
        )
        buttons[i][j].grid(row=i, column=j, padx=10, pady=10)

# Configure row/column resizing
for i in range(3):
    game_frame.grid_rowconfigure(i, weight=1)
    game_frame.grid_columnconfigure(i, weight=1)

def make_move(button, row, col):
    global current_player
    if board[row][col] == "" and current_player == "X":
        board[row][col] = "X"
        button.config(text="X", state=tk.DISABLED, fg="blue")

        if check_draw(board):
            end_game("It's a draw!")
            return
        current_player = "O"
        header_label.config(text="AI's Turn (O)", fg="green")
