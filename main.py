import tkinter as tk
import random

# -----------------------------
# Game Variables
# -----------------------------
secret_number = random.randint(1, 100)
attempt_count = 0

# -----------------------------
# Functions
# -----------------------------
def check_guess():
    global attempt_count

    try:
        guess = int(guess_entry.get())
        attempt_count += 1

        attempts_label.config(text=f"Attempts: {attempt_count}")

        if guess < secret_number:
            result_label.config(
                text="⬇ Too Low",
                fg="#FAB387"
            )

        elif guess > secret_number:
            result_label.config(
                text="⬆ Too High",
                fg="#F38BA8"
            )

        else:
            result_label.config(
                text=f"🎉 Correct! You guessed it in {attempt_count} attempts.",
                fg="#A6E3A1"
            )

    except ValueError:
        result_label.config(
            text="⚠ Please enter a valid number!",
            fg="#F38BA8"
        )

    guess_entry.delete(0, tk.END)


def new_game():
    global secret_number, attempt_count

    secret_number = random.randint(1, 100)
    attempt_count = 0

    attempts_label.config(text="Attempts: 0")

    result_label.config(
        text="Start guessing!",
        fg="#CDD6F4"
    )

    guess_entry.delete(0, tk.END)
    guess_entry.focus()


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

# -----------------------------
# Main Card
# -----------------------------
main_frame = tk.Frame(
    root,
    bg="#313244",
    padx=30,
    pady=30
)
main_frame.pack(expand=True, padx=25, pady=25)

# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    main_frame,
    text="🎯 Number Guessing Game",
    font=("Segoe UI", 22, "bold"),
    bg="#313244",
    fg="#CDD6F4"
)
title_label.pack(pady=(0, 15))

# -----------------------------
# Instructions
# -----------------------------
instruction_label = tk.Label(
    main_frame,
    text="Guess a number between 1 and 100",
    font=("Segoe UI", 11),
    bg="#313244",
    fg="#CDD6F4"
)
instruction_label.pack()

# -----------------------------
# Entry Box
# -----------------------------
guess_entry = tk.Entry(
    main_frame,
    font=("Segoe UI", 18),
    justify="center",
    width=10,
    relief="flat",
    bd=0
)
guess_entry.pack(pady=20, ipady=10)

# -----------------------------
# Submit Button
# -----------------------------
submit_btn = tk.Button(
    main_frame,
    text="Submit Guess",
    command=check_guess,
    font=("Segoe UI", 11, "bold"),
    bg="#89B4FA",
    fg="black",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
submit_btn.pack()

# -----------------------------
# Attempts Label
# -----------------------------
attempts_label = tk.Label(
    main_frame,
    text="Attempts: 0",
    font=("Segoe UI", 11),
    bg="#313244",
    fg="#CDD6F4"
)
attempts_label.pack(pady=20)

# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(
    main_frame,
    text="Start guessing!",
    font=("Segoe UI", 14, "bold"),
    bg="#313244",
    fg="#CDD6F4",
    wraplength=350
)
result_label.pack(pady=10)

# -----------------------------
# New Game Button
# -----------------------------
new_game_btn = tk.Button(
    main_frame,
    text="🔄 New Game",
    command=new_game,
    font=("Segoe UI", 11, "bold"),
    bg="#A6E3A1",
    fg="black",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
new_game_btn.pack(pady=20)

# Press Enter to Submit
root.bind("<Return>", lambda event: check_guess())

# Focus on Entry at Startup
guess_entry.focus()

# -----------------------------
# Run App
# -----------------------------
root.mainloop()