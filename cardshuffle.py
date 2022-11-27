from random import*
import os
import time
import math




#Clears screen each time
os.system("cls")

#Uniformly Distributed Random Values for Dice 
dice_1=randrange(6)+1
dice_2=randrange(6)+1

#Components of Cards
# top =       
# bottom =    
blank =     '         '

sides = [   '_________', 
            '|       |', 
            '|       |', 
            '| Death |', 
            '| Chest |', 
            '|       |', 
            '|_______|']


def draw_cards(all_cards, delay):
    os.system("cls")
    num_cards = []
    offset_down_num = []
    gap_between_stacks_num = []

    for card in range(0, len(all_cards)):
        num_cards.append(all_cards[card][2])
        offset_down_num.append(all_cards[card][0])
        if card == 0:
            gap_between_stacks_num.append(all_cards[0][1])
            furthest_right = all_cards[0][1] + len(sides[0])
        else:
            gap_between_stacks_num.append(all_cards[card][1] - furthest_right)
            if all_cards[card][1] + len(sides[0]) > furthest_right:
                furthest_right = all_cards[card][1] + len(sides[0])


    stacks = len(num_cards)
    #Constrcutor string
    s = ""

    #Offsets
    #offset_right = ''
    offset_down = ''
    g = ''
    gap_between_stacks = []

    
    for gap in range(0, len(gap_between_stacks_num)):
        for space in range(0, gap_between_stacks_num[gap]):
            g += " "
        gap_between_stacks.append(g)
        g = ''

    flag = 0

    for card in range(0,max(num_cards)+len(sides)+max(offset_down_num)):
        for gap in range(0, stacks):
            if gap_between_stacks_num[gap] < 0 and offset_down_num[gap] <= card and offset_down_num[gap] + num_cards[gap] + len(sides) > card + 1:
                if -1*gap_between_stacks_num[gap] > len(sides[0]):
                    back_num =  len(sides[0]) - abs(gap_between_stacks_num[gap])
                    back_str = s[back_num:]
                    s = s[:gap_between_stacks_num[gap]]
                    flag = 1
                else:
                    s = s[:gap_between_stacks_num[gap]]
            if offset_down_num[gap] > card:
                s += gap_between_stacks[gap] + blank
                if gap_between_stacks_num[gap] < 0:
                    if abs(gap_between_stacks_num[gap]) > len(sides[0]):
                        back_num = -1*len(blank)
                        s = s[:back_num]
                    else:
                        s = s[:gap_between_stacks_num[gap]]
            elif offset_down_num[gap] == card:
                s += gap_between_stacks[gap] + sides[0]
            elif num_cards[gap] + offset_down_num[gap] > card:
                s += gap_between_stacks[gap] + sides[6]
            elif num_cards[gap] + offset_down_num[gap] == card:
                s += gap_between_stacks[gap] + sides[1]
            elif num_cards[gap] + offset_down_num[gap] == card - 1:
                s += gap_between_stacks[gap] + sides[2]
            elif num_cards[gap] + offset_down_num[gap] == card - 2:
                s += gap_between_stacks[gap] + sides[3]
            elif num_cards[gap] + offset_down_num[gap] == card - 3:
                s += gap_between_stacks[gap] + sides[4]
            elif num_cards[gap] + offset_down_num[gap] == card - 4:
                s += gap_between_stacks[gap] + sides[5]
            elif num_cards[gap] + offset_down_num[gap] == card - 5:
                s += gap_between_stacks[gap] + sides[6]
            else:
                s += gap_between_stacks[gap] + blank
                if -1*gap_between_stacks_num[gap] > len(sides[0]):
                    back_num = -1*len(blank)
                    s = s[:back_num]
                elif gap_between_stacks_num[gap] < 0:
                    s = s[:gap_between_stacks_num[gap]]
                
            if flag == 1:
                s += back_str
                flag = 0 
            
        s += '\n'
    s+='\n'
    print(s)
    time.sleep(delay)

#Each Card is a list. Position 0 is offset down, Position 1 is offset right
#Cards added later in the list will be added on top of existing cards
all_cards = [[0,20,1]]
delay = 0.02

# draw_cards(all_cards,delay)

# for x in range(10,12):
#     for y in range(0,len(all_cards)):
#         all_cards[y][1] = x
#     draw_cards(all_cards,delay)


for x in range(40,60):
    all_cards[0][1] = x
    draw_cards(all_cards,delay)

for x in range(60,50, -1):
    all_cards[0][1] = x
    draw_cards(all_cards,delay)

for x in range(0,26):
    all_cards.append([0,50+2*x,1])
    draw_cards(all_cards,delay)

for x in range(50,40,-1):
    all_cards[0][1] = x
    delay = 0.033
    draw_cards(all_cards,delay)

for x in range(40,92):
    delay = 0.015
    all_cards[0][1] = x
    try:
        if all_cards[1][1] < x + 9:
            del(all_cards[1])
    except:
        continue
    draw_cards(all_cards,delay)

all_cards[0][1] = 100
all_cards[1][1] = 91

for x in range(91,101):
    all_cards[1][1] = x
    draw_cards(all_cards, delay)




delay = 0.015

for x in range(100, 69, -1):
    all_cards[0][1] = x
    all_cards[1][1] = 200 - x
    draw_cards(all_cards, delay)

print(all_cards)

delay = 0.033

for x in range(2,16):
    all_cards[0][2] = x
    all_cards[1][2] = x
    draw_cards(all_cards, delay)

for x in range(15, 0, -1):
    all_cards[0][2] = x
    all_cards[1][2] = x
    draw_cards(all_cards, delay)

all_cards.append([0,70,1])
all_cards.append([0,130,1])

delay = 0.015

for x in range(0,10):
    all_cards[2][1] += 3
    all_cards[3][1] -= 3
    draw_cards(all_cards,delay)
    
del(all_cards[3])

for y in range(0,12):
    all_cards.append([0,70,1])
    all_cards.append([0,130,1])
    for x in range(0,10):
        all_cards[3][1] += 3
        all_cards[4][1] -= 3
        draw_cards(all_cards,delay)
    del(all_cards[4])
    del(all_cards[3])
    all_cards[2][2] += 1

draw_cards(all_cards,delay)

for x in range(0,10):
    all_cards[0][1] += 3
    all_cards[1][1] -= 3
    draw_cards(all_cards,delay)

all_cards[2][2] += 1
draw_cards(all_cards,delay)

for x in range(0,13):
    all_cards[2][2] -= 1
    draw_cards(all_cards,delay)