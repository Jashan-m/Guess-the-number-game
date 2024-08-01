import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the number between 1 and 100:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.pack(pady=10)
        
        self.button = tk.Button(root, text="Submit Guess", font=('Arial', 14), command=self.check_guess)
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number between 1 and 100.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumber(root)
    root.mainloop()
