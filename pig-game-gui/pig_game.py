import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os

class PigGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pig Game")
        self.root.geometry("1000x600")
        
        # Set the background gradient
        self.bg_frame = tk.Frame(root, bg="#753682")
        self.bg_frame.place(relwidth=1, relheight=1)
        
        # Game variables
        self.scores = [0, 0]
        self.current_score = 0
        self.active_player = 0
        self.playing = True
        
        # Configure the main container
        self.container = tk.Frame(root, bg="white", bd=5)
        self.container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)
        
        # Create player sections
        self.create_player_section(0)
        self.create_player_section(1)
        
        # Create dice image area
        self.dice_label = tk.Label(self.container, bg="white")
        self.dice_label.place(relx=0.5, rely=0.3, anchor="center")
        
        # Load dice images
        self.dice_images = []
        for i in range(1, 7):
            image = Image.open(f"dice-{i}.png")
            image = image.resize((100, 100), Image.LANCZOS)
            self.dice_images.append(ImageTk.PhotoImage(image))
        
        # Hide dice initially
        self.dice_visible = False
        
        # Create buttons
        self.create_buttons()
        
        # Initialize game
        self.init_game()

    def create_player_section(self, player_num):
        x_pos = 0.25 if player_num == 0 else 0.75
        
        # Player frame
        self.player_frame = tk.Frame(
            self.container, 
            bg="white" if player_num == 0 else "#f0f0f0"
        )
        self.player_frame.place(relx=x_pos, rely=0.5, anchor="center", relwidth=0.48, relheight=0.96)
        
        # Player name
        player_name = tk.Label(
            self.player_frame, 
            text=f"PLAYER {player_num + 1}", 
            font=("Helvetica", 24, "bold"), 
            bg=self.player_frame["bg"]
        )
        player_name.place(relx=0.5, rely=0.1, anchor="center")
        
        # Player total score
        player_score = tk.Label(
            self.player_frame, 
            text="0", 
            font=("Helvetica", 60), 
            fg="#c7365f", 
            bg=self.player_frame["bg"]
        )
        player_score.place(relx=0.5, rely=0.25, anchor="center")
        
        # Current score section
        current_frame = tk.Frame(
            self.player_frame, 
            bg="#c7365f", 
            bd=2
        )
        current_frame.place(relx=0.5, rely=0.75, anchor="center", relwidth=0.6, relheight=0.2)
        
        current_label = tk.Label(
            current_frame, 
            text="CURRENT", 
            font=("Helvetica", 14), 
            fg="white", 
            bg="#c7365f"
        )
        current_label.place(relx=0.5, rely=0.3, anchor="center")
        
        current_score = tk.Label(
            current_frame, 
            text="0", 
            font=("Helvetica", 24), 
            fg="white", 
            bg="#c7365f"
        )
        current_score.place(relx=0.5, rely=0.7, anchor="center")
        
        # Store references
        if player_num == 0:
            self.player0_frame = self.player_frame
            self.score0_label = player_score
            self.current0_label = current_score
        else:
            self.player1_frame = self.player_frame
            self.score1_label = player_score
            self.current1_label = current_score

    def create_buttons(self):
        # New Game button
        self.btn_new = ttk.Button(
            self.container, 
            text="🔄 New Game", 
            command=self.init_game
        )
        self.btn_new.place(relx=0.5, rely=0.1, anchor="center")
        
        # Roll Dice button
        self.btn_roll = ttk.Button(
            self.container, 
            text="🎲 Roll Dice", 
            command=self.roll_dice
        )
        self.btn_roll.place(relx=0.5, rely=0.75, anchor="center")
        
        # Hold button
        self.btn_hold = ttk.Button(
            self.container, 
            text="📥 Hold", 
            command=self.hold
        )
        self.btn_hold.place(relx=0.5, rely=0.85, anchor="center")

    def init_game(self):
        # Reset game state
        self.scores = [0, 0]
        self.current_score = 0
        self.active_player = 0
        self.playing = True
        
        # Reset UI
        self.score0_label.config(text="0")
        self.score1_label.config(text="0")
        self.current0_label.config(text="0")
        self.current1_label.config(text="0")
        
        # Hide dice
        self.dice_label.config(image="")
        self.dice_visible = False
        
        # Set active player
        self.player0_frame.config(bg="white")
        self.player1_frame.config(bg="#f0f0f0")
        
        # Reset winner styles
        self.reset_styles()

    def reset_styles(self):
        self.player0_frame.config(bg="white")
        self.player1_frame.config(bg="#f0f0f0")
        
        # Update nested widgets' backgrounds
        for widget in self.player0_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="white")
                
        for widget in self.player1_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#f0f0f0")

    def switch_player(self):
        self.current_score = 0
        
        if self.active_player == 0:
            self.current0_label.config(text="0")
            self.player0_frame.config(bg="#f0f0f0")
            self.player1_frame.config(bg="white")
            
            # Update nested widgets' backgrounds
            for widget in self.player0_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                    widget.config(bg="#f0f0f0")
                    
            for widget in self.player1_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                    widget.config(bg="white")
                    
            self.active_player = 1
        else:
            self.current1_label.config(text="0")
            self.player1_frame.config(bg="#f0f0f0")
            self.player0_frame.config(bg="white")
            
            # Update nested widgets' backgrounds
            for widget in self.player1_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                    widget.config(bg="#f0f0f0")
                    
            for widget in self.player0_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                    widget.config(bg="white")
                    
            self.active_player = 0

    def roll_dice(self):
        if self.playing:
            # Generate random dice roll
            dice = random.randint(1, 6)
            
            # Display dice
            self.dice_label.config(image=self.dice_images[dice-1])
            self.dice_visible = True
            
            # Check for rolled 1
            if dice != 1:
                # Add dice to current score
                self.current_score += dice
                if self.active_player == 0:
                    self.current0_label.config(text=str(self.current_score))
                else:
                    self.current1_label.config(text=str(self.current_score))
            else:
                # Switch to next player
                self.switch_player()

    def hold(self):
        if self.playing:
            # Add current score to active player's score
            self.scores[self.active_player] += self.current_score
            
            if self.active_player == 0:
                self.score0_label.config(text=str(self.scores[self.active_player]))
            else:
                self.score1_label.config(text=str(self.scores[self.active_player]))
            
            # Check if player's score is >= 100
            if self.scores[self.active_player] >= 100:
                # Finish the game
                self.playing = False
                self.dice_label.config(image="")
                self.dice_visible = False
                
                if self.active_player == 0:
                    self.player0_frame.config(bg="#2f2f2f")
                    for widget in self.player0_frame.winfo_children():
                        if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                            widget.config(bg="#2f2f2f", fg="#c7365f")
                else:
                    self.player1_frame.config(bg="#2f2f2f")
                    for widget in self.player1_frame.winfo_children():
                        if isinstance(widget, tk.Label) and widget.cget("fg") != "#c7365f":
                            widget.config(bg="#2f2f2f", fg="#c7365f")
            else:
                # Switch to next player
                self.switch_player()


if __name__ == "__main__":
    root = tk.Tk()
    app = PigGame(root)
    root.mainloop()
