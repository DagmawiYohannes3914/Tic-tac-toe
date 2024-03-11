class Game:
    def __init__(self):
        self.current_player = "X"
        self.board = [" "]*9
        
    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            return True
        return False
    
    def check_winner(self):
        winning_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combo:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        