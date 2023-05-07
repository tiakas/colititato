from colititato.cli import Game
from colititato.cli import Scoreboard
import unittest
from unittest.mock import patch

class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game()
        self.assertEqual(game.board, [' '] * 9)
        self.assertIsNone(game.player)
        self.assertIsNone(game.computer)
        self.assertIsInstance(game.scoreboard, Scoreboard)

    def test_reset_board(self):
        game = Game()
        game.board = ['X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        game.reset_board()
        self.assertEqual(game.board, [' '] * 9)

    def test_check_winner(self):
        game = Game()
        board1 = ['X', 'X', 'X', ' ', 'O', ' ', 'O', ' ', ' ']
        board2 = ['O', 'X', 'X', 'X', 'O', ' ', ' ', ' ', 'O']
        board3 = ['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']
        self.assertTrue(game.check_winner(board1, 'X'))
        self.assertTrue(game.check_winner(board2, 'O'))
        self.assertFalse(game.check_winner(board3, 'O'))

    def test_computer_move(self):
        game = Game()
        game.player = 'X'
        game.computer = 'O'
         
        # Test case 1: empty board
        board = [' '] * 9
        self.assertEqual(game.computer_move(board), 4)

        # Test case 2: player can win
        board = [
            'O', 'X', 'O',
            'X', 'X', ' ',
            ' ', ' ', ' ']
        self.assertEqual(game.computer_move(board), 5)
    
        # Test case 3: computer can win
        board = ['O', 'X', 'O',
                'O', 'X', ' ',
                ' ', ' ', ' ']

        self.assertEqual(game.computer_move(board), 6)

        # Test case 4: center already taken
        board = [' ', ' ', ' ',
                ' ', 'O', ' ',
                ' ', ' ', ' ']
        
        with patch('random.choice', return_value=0):
            self.assertEqual(game.computer_move(board), 0)
        


class TestGameIntegration(unittest.TestCase):
    @patch('builtins.input', return_value=9)
    def test_player_wins(self, mock_input):
        game = Game()
        game.player = 'X'
        game.computer = 'O'
        game.board = ['X', ' ', ' ', 'O', 'X', ' ', ' ', 'O', ' ']
        game.play()
        self.assertEqual(game.scoreboard.player_wins, 1)

    def test_computer_wins(self):
        game = Game()
        game.player = 'O'
        game.computer = 'X'
        game.board = ['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        game.play()
        self.assertEqual(game.scoreboard.computer_wins, 1)

    @patch('builtins.input', return_value=9)
    def test_tie(self, mock_input):
        game = Game()
        game.player = 'X'
        game.computer = 'O'
        game.board = ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', ' ']
        game.play()
        self.assertEqual(game.scoreboard.ties, 1)

