import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic-Tac-Toe AI')
        self.setGeometry(300, 300, 300, 300)
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buttons = []
        for i in range(9):
            button = QPushButton('')
            button.setFixedSize(80, 80)
            button.setStyleSheet("font-size: 24px;")
            button.clicked.connect(lambda _, idx=i: self.player_move(idx))
            self.grid.addWidget(button, i // 3, i % 3)
            self.buttons.append(button)

    def player_move(self, idx):
        if self.board[idx] == '' and self.current_player == 'X':
            self.board[idx] = 'X'
            self.buttons[idx].setText('X')
            if self.check_winner('X'):
                self.game_over("You win!")
            elif '' not in self.board:
                self.game_over("It's a draw!")
            else:
                self.current_player = 'O'
                self.ai_move()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.board[best_move] = 'O'
            self.buttons[best_move].setText('O')
            if self.check_winner('O'):
                self.game_over("AI wins!")
            elif '' not in self.board:
                self.game_over("It's a draw!")
            self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner_board(board, 'O'):
            return 1
        elif self.check_winner_board(board, 'X'):
            return -1
        elif '' not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        return self.check_winner_board(self.board, player)

    def check_winner_board(self, board, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(board[i] == player for i in condition):
                return True
        return False

    def game_over(self, message):
        QMessageBox.information(self, "Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.setText('')
        self.current_player = 'X'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
