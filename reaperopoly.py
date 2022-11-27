"""
Reaperopoly - The game of death and taxes

Property trading gaming where winner takes all, 
"""
from player import Player
import constant
import board
import os

class Reaperopoly(object):
    name = "Reaperopoly"
    players = []
    
    def __init__(self, name):
        self.name = name
        self.num_players = 0
        self.players = []
        
    def __str__(self):
        return 'Reaperopoly(' + self.name +')'
    
    def setup(self):

        # TODO: Game Setup - ask # of players, rules options, etc..
        # TODO - ask # of humans
        #       - ask for name for each
        #       - ask # of AI
        while self.num_players < 1 or self.num_players > constant.MAX_PLAYERS:
            playerCountInput = input('Enter the number of players for the game: ')

            try:
                playerCount = int(playerCountInput)
                if playerCount > constant.MAX_PLAYERS:
                    print('Please enter a number between %s and %s' % (constant.MIN_PLAYERS, constant.MAX_PLAYERS))
                    continue
                else:
                    self.num_players = playerCount
            except ValueError:
                print('Please enter a number between ' + str(constant.MIN_PLAYERS) + ' and ' + str(constant.MAX_PLAYERS))
        # TODO - exit if valueError?                
        self.board = board.Board(self.name)

game = Reaperopoly("Reaperopoly Game 1")
game.setup()

# define constants

me = Player("Bob",0.00)
you = Player("SomeoneElse", 0.00)
ai = Player("AI (Empty)", 100.00)

players = [ me, you, ai ]
print(players)
print("#####")
for player in players:
    print(player)
    player.printPlayer()
    player.addWallet(200.00)
    print(player)
    print("#####")

game.board.printBoard()

# TODO - roll dice
