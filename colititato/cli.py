import random

class Game:
    def __init__(self):
        self.board = [' '] * 9
        self.player = None
        self.computer = None
        self.scoreboard = Scoreboard()

    
    def reset_board(self):
        self.board = [' '] * 9

    def print_board(self):
        """Print the board."""
        marker_info = f"Player: {self.player}, Computer: {self.computer}"
        for i in range(0, 9, 3):
            row = ' | '.join(self.board[i:i+3])
            # display the marker info on the first row in the same line
            if i == 0:
                print(f' {row}  {marker_info}')
            else:
                print(f' {row} ')

            if i < 6:
                print('-----------')

    def select_marker(self):
        """Select the player's marker."""
        self.player = self.computer = None
        while self.player not in ('X', 'O'):
            self.player = input('Select your marker (X/O): ').upper()

        self.computer = 'O' if self.player == 'X' else 'X'

    def player_move(self):
        """Get the player's move."""
        while True:
            try:
                move = int(input('Enter your move (1-9): '))
                if move not in range(1, 10) or self.board[move-1] != ' ':
                    raise ValueError
                return move - 1
            except ValueError:
                print('Invalid move. Please try again.')

    def computer_move(self, board):
        """
        Returns the computer's move using a decision tree.
        """
        # Check if the computer can win in the next move
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.computer
                if self.check_winner(board, self.computer):
                    return i
                board[i] = ' '

        # Check if the player can win in the next move and block them
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.player
                if self.check_winner(board, self.player):
                    board[i] = self.computer
                    return i
                board[i] = ' '

        # Choose center spot if it is available
        if board[4] == ' ':
            return 4

        # Choose a corner spot if it is available
        corners = [0, 2, 6, 8]
        available_corners = [corner for corner in corners if board[corner] == ' ']
        if available_corners:
            return random.choice(available_corners)

        # Choose a side spot
        sides = [1, 3, 5, 7]
        available_sides = [side for side in sides if board[side] == ' ']
        return random.choice(available_sides)
    
   
    def check_winner(self, board, marker):
        win_combos = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        )

        for combo in win_combos:
            if all(board[i] == marker for i in combo):
                return True

        return False

    def play(self):
        if self.player == 'X':
            turn = 'player'
        else:
            turn = 'computer'

        while True:
            if self.scoreboard.games_played > 0:
                print(str(self.scoreboard))
            self.print_board()

            if turn == 'player':
                print("Player's turn.")
                move = self.player_move()
                self.board[move] = self.player
                turn = 'computer'
            else:
                print("Computer's turn.")
                move = self.computer_move(self.board)
                turn = 'player'
                if move is None:
                    print('The game is a tie!')
                    self.scoreboard.ties += 1
                    break
                self.board[move] = self.computer

            if self.check_winner(self.board, self.player):
                self.print_board()
                print('Player wins!')
                self.scoreboard.player_wins += 1
                break
            elif self.check_winner(self.board, self.computer):
                self.print_board()
                print('Computer wins!')
                self.scoreboard.computer_wins += 1
                break
            elif ' ' not in self.board:
                self.print_board()
                print('The game is a tie!')
                self.scoreboard.ties += 1
                break

class Scoreboard():
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0

    @property
    def games_played(self):
        return self.player_wins + self.computer_wins + self.ties

    def __str__(self):
        return f'Score: Player {self.player_wins} - Computer {self.computer_wins} - Ties {self.ties}'

    def __repr__(self):
        return f'Scoreboard(player_wins={self.player_wins}, computer_wins={self.computer_wins}, ties={self.ties}, games_played={self.games_played})'

def main():
    game = Game()
    game.select_marker()
    while True:
        game.play()
        if input('Play again? (Y/N): ').upper() != 'Y':
            print(game.scoreboard)
            break
        game.reset_board()
        game.select_marker()

if __name__ == '__main__':
    main()
