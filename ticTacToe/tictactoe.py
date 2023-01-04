class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    #single list to rep 3x3 board
        self.currWinner = None  #keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i*1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    