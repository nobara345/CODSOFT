import tkinter as tk
import random

choices = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("300x300")

instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
instruction_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()