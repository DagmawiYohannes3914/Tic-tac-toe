import tkinter as tk
from TicTacToeGame import Game
from tkinter import messagebox

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TicTacToe")
        
        self.game = Game()
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(button)

        self.restart_button = tk.Button(master, text="Restart", font=('Arial', 14),
                                        command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
        
    def on_click(self, row, col):
        index = 3 * row + col
        if self.game.make_move(index):
                
            self.buttons[index].config(text=self.game.current_player)
            if self.game.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"{self.game.current_player} wins!")
                self.restart_game()
            
            elif " " not in self.game.board:
                messagebox.showinfo("Tic Tac Toe", "Its a tie!")
                self.restart_game()
            else:
                self.game.switch_player()
                        
    def restart_game(self):
        self.game = Game()
        for button in self.buttons:
            button.config(text= " ")
        
