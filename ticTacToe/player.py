#Player Class
#
#Defines the various players for the command line
#tic tac toe game
#
#Practicing inheritance, class creation, object instantiation,
#


import math
import random


#Base Player class
class Player: 
    def __init__(self,mark):
        self.mark = mark    #mark is x or o

    def get_move(self, game):
        pass    



#inheritance from Player class to build computer player
class ComputerPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)


    def get_move(self,game):
        pass

#inheritance from Player class to build computer player
class HumanPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)


    def get_move(self,game):
        pass