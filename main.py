import tkinter as tk
from TicTacToeGUI import GUI
# from TicTacToeGame import Game
# from tkinter import messagebox

def main ():
    root = tk.Tk()
    game = GUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()