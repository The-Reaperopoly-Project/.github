"""
Reaperopoly - Board Class

Defines the playing board of the game and all of it's spaces etc..

----------------------------------------------------------------
| GO             | Misery Avenue | Death Chest   | Bane Avenue |
| - Collect $200 |- Price $60    | - Pick a card | - Price $60 |
----------------------------------------------------------------

TODO 
* Could make BoardSpace the generic base type and create concrete types for each of the space types
* Use a generic playerLands() type of function to call when the player lands on the property
* Rents / color grouping

"""
import constant

class BoardSpace(object):
    name = ""
    purchasePrice = 0       # how will we handle church tax's 10%?
    group = ""              # should be from a fixed list of groups, could use group as our special indicator for tax/chance/chest/taxes etc...
    houses = 0
    isMortgaged = False

    def __init__(self, name, group, purchasePrice=0):
        self.name = name
        self.group = group
        self.purchasePrice = purchasePrice

    def __str__(self):
        return self.name

    def printBoardSpaceStr(self):
        lines = "/" + "-" * (constant.BOARDSPACE_WIDTH+2) + "\\\n"
        lines = lines + f"| {self.name.center(constant.BOARDSPACE_WIDTH)} |\n"
        lines = lines + f"| " + " ".center(constant.BOARDSPACE_WIDTH) + " |\n"
        if self.purchasePrice > 0:
            lines = lines + f"| " + f"Price RS${self.purchasePrice}".center(constant.BOARDSPACE_WIDTH) + " |\n"
        elif self.isMortgaged:
            lines = lines + f"| " + f"(Mortgaged RS${self.purchasePrice})".center(constant.BOARDSPACE_WIDTH) + " |\n"
        else:
            lines = lines + f"| " + " ".center(constant.BOARDSPACE_WIDTH) + " |\n"
        lines = lines + "\\" + "-" * (constant.BOARDSPACE_WIDTH+2) + "/\n"
        return lines

    def printBoardSpace(self):
        print("/" + "-" * (constant.BOARDSPACE_WIDTH+2) + "\\")
        print(f"| {self.name.center(constant.BOARDSPACE_WIDTH)} |")
        print(f"| " + " ".center(constant.BOARDSPACE_WIDTH) + " |")
        if self.purchasePrice > 0:
            print(f"| " + f"Price RS${self.purchasePrice}".center(constant.BOARDSPACE_WIDTH) + " |")
        elif self.isMortgaged:
            print(f"| " + f"(Mortgaged RS${self.purchasePrice})".center(constant.BOARDSPACE_WIDTH) + " |")
        else:
            print(f"| " + " ".center(constant.BOARDSPACE_WIDTH) + " |")
        print("\\" + "-" * (constant.BOARDSPACE_WIDTH+2) + "/")

class RailroadSpace(BoardSpace):
    # TODO - add special features for railroads
    def __init__(self, name, purchasePrice = 200):
        super().__init__(name, "Railroad", purchasePrice)

    def __str__(self):
        return "RR: " + self.name

class DeathChestSpace(BoardSpace):
    # TODO - add special features for selecting deathchest card
    def __init__(self, name):
        super().__init__(name, "DeathChest")

    def __str__(self):
        return "DC: " + self.name

class ChanceSpace(BoardSpace):
    # TODO - add special features for selecting chance card
    def __init__(self, name):
        super().__init__(name, "Chance")

class TaxSpace(BoardSpace):
    # TODO - add special features for taxing player on landing
    def __init__(self, name):
        super().__init__(name, "Tax")

# TODO - utilitiesspace, just visiting, free parking, jail

class Board(object):
    spaces = [ 
        BoardSpace("GO","GO"), # TODO handle giving player 200
        BoardSpace("Misery Avenue", "PURPLE", 60),
        DeathChestSpace("Death Chest"),
        BoardSpace("Bane Avenue", "PURPLE", 60),
        TaxSpace("Church Tax"),
        RailroadSpace("Ruination Railroad", 200),
        BoardSpace("Turmoil Terrace", "LIGHTBLUE", 100),
        ChanceSpace("Chance"),
        BoardSpace("Agony Avenue", "LIGHTBLUE", 100),
        BoardSpace("Dread Drive", "LIGHTBLUE", 120)
    ]
    name = 'Reaperopoly Board'
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


    def printBoard(self):
        def printBoardRow(row):
            strings = []
            for spaceId in row:
                if spaceId == -1:
                    strings.append((' ' * (constant.BOARDSPACE_WIDTH+4) + '\n')*constant.BOARDSPACE_HEIGHT)
                else:
                    strings.append(self.spaces[spaceId].printBoardSpaceStr())
            print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')

        # TODO printBoard(): This is sample ASCII art code to display the current board
        print("/----------------\ /---------------\ /---------------\ /-------------\\")
        print("| GO             | | Misery Avenue | | Death Chest   | | Bane Avenue |")
        print("| - Collect $200 | |- Price $60    | | - Pick a card | | - Price $60 |")
        print("\\---------------/ \---------------/ \---------------/ \-------------/")
        
        # TODO - array for the lines and append each one?
        print("DYNAMIC BELOW")
        for space in self.spaces:
            #print(space)
            space.printBoardSpace()
        
        print("SUPER DYNAMIC")

        #line1 = '|## {0} ##| |## {1} ##| |## {2} ##|'.format(self.spaces[0].printBoardSpace(), self.spaces[1].printBoardSpace(), self.spaces[2].printBoardSpace())
        #print(line1)
        #line2 = '|## {0} ##| |## {1} ##| |## {2} ##|'.format(self.spaces[0], self.spaces[1], self.spaces[2])
        #print(line2)

        boardFormat = [
            [0,1,2,3],
            [4,-1,-1,5],
            [6,7,8,9]
        ]

        for boardRow in boardFormat:
            printBoardRow(boardRow)

        
