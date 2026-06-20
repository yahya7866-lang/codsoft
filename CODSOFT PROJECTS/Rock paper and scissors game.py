import tkinter as tk
import random

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("900x600")
root.configure(bg="#f0f4f7")

# Scores
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# Game Logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "😢 Computer Wins!"
        computer_score += 1

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}   |   Computer Score: {computer_score}"
    )

# Reset Game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer Choice: ")
    result_label.config(text="Choose Rock, Paper, or Scissors")

    score_label.config(
        text="Your Score: 0   |   Computer Score: 0"
    )

# Heading
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 28, "bold"),
    bg="#f0f4f7",
    fg="#2c3e50"
)
title.pack(pady=20)

instruction = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 16),
    bg="#f0f4f7"
)
instruction.pack()

# Buttons Frame
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=30)

rock_btn = tk.Button(
    frame,
    text=" Rock",
    font=("Arial", 16, "bold"),
    width=12,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(
    frame,
    text=" Paper",
    font=("Arial", 16, "bold"),
    width=12,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(
    frame,
    text=" Scissors",
    font=("Arial", 16, "bold"),
    width=12,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=15)

# Output Labels
user_choice_label = tk.Label(
    root,
    text="Your Choice:",
    font=("Arial", 18),
    bg="#f0f4f7"
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="Computer Choice:",
    font=("Arial", 18),
    bg="#f0f4f7"
)
computer_choice_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 22, "bold"),
    bg="#f0f4f7",
    fg="green"
)
result_label.pack(pady=20)

score_label = tk.Label(
    root,
    text="Your Score: 0   |   Computer Score: 0",
    font=("Arial", 18, "bold"),
    bg="#f0f4f7",
    fg="blue"
)
score_label.pack(pady=10)

reset_btn = tk.Button(
    root,
    text=" Play Again",
    font=("Arial", 16, "bold"),
    command=reset_game
)
reset_btn.pack(pady=20)
root.mainloop()