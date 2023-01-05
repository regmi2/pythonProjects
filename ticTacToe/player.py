#Player Class
#
#Defines the various players for the command line
#tic tac toe game
#
#Practicing inheritance, class creation, object instantiation,
#


import math
import random


# CLASS: Player class that is the base class for 
# human and computer player classes
# all players have a mark that is X or O
class Player: 
    def __init__(self,mark):
        self.mark = mark    #mark is x or o

    def get_move(self, game):
        pass    



#CLASS:
# Computer Player class
# inherits from Player class 
# 
# Defined to make a move based on any random empty
class ComputerPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)


    # METHOD:
    # Computer will randomly choose an empty spot on the board
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


#CLASS:
# Human Player class
# inherits from Player class 
# 
# Defined to make a move based on valid selection

class HumanPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)


    # METHOD:
    # Until the human selects a valid square, take the 
    # player's input which must be an int value that is the
    # index of an empty square. Otherwise, raise a ValueError
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.mark + '\'s turn. Input move (0-9): ')


            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
