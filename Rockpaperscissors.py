import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors Game")
        self.window.geometry("400x300")
        
        # Game options
        self.options = ["rock", "paper", "scissors"]
        
        # Score tracking
        self.user_score = 0
        self.computer_score = 0
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.window, text="Rock Paper Scissors", 
                              font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)
        
        # Rules label
        rules_label = tk.Label(self.window, text="Rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock",
                             font=("Helvetica", 10))
        rules_label.pack(pady=5)
        
        # Score label
        self.score_label = tk.Label(self.window, text="Score: You 0 - Computer 0",
                                  font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(pady=20)
        
        # Create buttons
        for option in self.options:
            button = tk.Button(buttons_frame, text=option.capitalize(), 
                             command=lambda o=option: self.play_round(o),
                             width=10, height=2)
            button.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        reset_button = tk.Button(self.window, text="Reset Score",
                               command=self.reset_score,
                               width=10, height=1)
        reset_button.pack(pady=10)
        
        # Exit button
        exit_button = tk.Button(self.window, text="Exit",
                              command=self.window.quit,
                              width=10, height=1)
        exit_button.pack(pady=10)
        
    def play_round(self, user_choice):
        # Get computer's choice
        computer_choice = random.choice(self.options)
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        # Update score display
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")
        
        # Show result message
        messagebox.showinfo("Result", 
                           f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
        
    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You 0 - Computer 0")
        messagebox.showinfo("Score Reset", "Score has been reset!")
        
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()