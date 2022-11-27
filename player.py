"""
Reaperopoly - Player Class

Initialize with a name and starting wallet amount
me = Player("Bob",0.00)

- TODO
    * Need a collection of our properties
        ?? store cost we paid?
        ?? store profit / loss?
        ?? calculate potential P&L?

"""
class Player(object):
    name = "Unknown"
    wallet = 0.00
    boardPosition = 0
        
    def __init__(self,name,wallet):
        self.name = name
        self.wallet = wallet
        
    def __str__(self):
        return 'Player(name='+self.name+',wallet=RS$'+str(self.wallet)+')'
    
    def printPlayer(self):
        print(self.name)
        print("RS$" + str(self.wallet))
    
    def getWallet(self):
        return self.wallet
    
    def addWallet(self,amt):
        self.wallet += amt

class HumanPlayer(Player):
    def __init__(self, name, wallet):
        super().__init__(name, wallet)

    def __str__(self):
        return f"Human: {self.name} RS${self.wallet}"

class AIPlayer(Player):
    def __init__(self, name, wallet):
        super().__init__(name, wallet)

    def __str__(self):
        return f"AI: {self.name} RS${self.wallet}"
