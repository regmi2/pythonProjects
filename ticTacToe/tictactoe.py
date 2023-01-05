import math
import time
from player import ComputerPlayer, HumanPlayer


#CLASS: 
# TicTacToe class that defines the game's logic & prints
# the board on the command line

class TicTacToe:
    def __init__(self):

        #single list to rep multidimensional 3x3 board
        self.board = [' ' for _ in range(9)]    

        #keep track of winner
        self.currWinner = None  

    # METHOD: 
    # for loop accesses game board (self.board) and identifies
    # each row with 3 spaces. From the first index of the row to the last
    # index of the row, print the board with the | lines

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            
            #join these in a string with the line | as a separator
            print('| ' + ' | '.join(row) + ' |')


    #METHOD:
    # static method because it doesn't relate to a specific board,
    # its a general method for ALL boards
    # no need to pass in a self
    #
    # print which number corresponds to which spot using same logic from above

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    


    # METHOD
    # given the board, the square, and the mark
    # if the square is empty, mark it
    # and return that the move was made with True
    # otherwise, return false

    def make_move(self,square,mark):
        if self.board[square] ==' ': 
            self.board[square] = mark

            #if on that move that player wins,
            #label them winner
            if self.winner(square, mark):
                self.currWinner = mark

            return True
        return False

    #METHOD:
    #checks for winner and returns true if someone wins

    def winner(self, square, mark):

        #check row for winning
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind+1) * 3]
        if all([spot == mark for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == mark for spot in column]):
            return True

        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == mark for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == mark for spot in diagonal2]):
                return True
        return False

    # METHOD: 
    # INPUT: Game board
    # OUTPUT/RETURN: List of available moves
    #
    # For each index, create a tuple (index, mark at index)
    # using list comprehension to process the for loop and the
    # enumeraion

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    #METHOD:
    #returns any spaces characters found in the self.board list

    def empty_squares(self):
        return ' ' in self.board


    #METHOD:
    #returns the number of empty squares found in self.board

    def num_empty_squares(self):
        return self.board.count(' ')


#FUNCTION:
#Start the game 
def play(game, x_player, o_player, print_game=True):

    # return mark of winner or None for a tie
    if print_game:
        game.print_board_nums()

    mark = 'X'


    while game.empty_squares():
        
        #get move from appropriate player
        if (mark == 'O'): 
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)

        #if the make move returns true,
        #print a new board with the mark and 
        #tell the user the move was made to what square
        if game.make_move(square,mark):
            if print_game:
                print(mark + f' makes a move to square {square}')
                game.print_board()
                print('')
        
            if game.currWinner:
                if print_game:
                    print(mark + ' wins!')
                return mark

            #switches player after move
            mark = 'O' if mark == 'X' else 'X'  

        #delay on computer to play
        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player,o_player, print_game=True)