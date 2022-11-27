from random import*
import os
import time
import math

#Random number of full rotations, anywhere from 2 to 4
spin_cycle = randrange(2,5)*36+9

for x in range(0,spin_cycle):
    #Clears screen each time
    os.system("cls")
    
    #Uniformly Distributed Random Values for Dice 
    dice_1=randrange(6)+1
    dice_2=randrange(6)+1
   
   #Components of Dice
    two_dots=       '|o o|'
    one_dot_left=   '|o  |'
    one_dot_center= '| o |'
    one_dot_right=  '|  o|'
    no_dots='|   |'
   
   #How far off the right the image will be 
    offset_right = ''
    offset_right_num = round(10 + 8*math.sin(x*math.pi/18))
    
    #Space Between Dice
    gap_between_dice = ""
    gap_between_dice_num = round(20 - 16*math.sin(x*math.pi/18))
    
    #How far down the dice will be from top of terminal
    offset_down = ''
    offset_down_num = round(4 - 4 * math.cos(x*math.pi/18))

    #Creates offset_right, gap_between_dice, and offset_down to have circular motion
    for y in range(0,offset_right_num):
        offset_right += " "    
    for y in range(0,gap_between_dice_num):
        gap_between_dice += " "
    for y in range(0,offset_down_num):
        offset_down += '\n'

    #Top of dice
    s=offset_down+offset_right+'-----' + gap_between_dice + '-----\n'

    #Goes through and creates dice drawings on a case by case basis determined by their random values
    #When the first die is greater than or equal to 4 there will be 2 dots in the first row
    if dice_1 >= 4:
        s+=offset_right+two_dots+gap_between_dice 
        #If the second die is also greater than or equal to four, there will be two dots in the top row
        if dice_2 >= 4:
            s+=two_dots + '\n'
        elif dice_2 >= 2:
            s+=one_dot_left +'\n'
        elif dice_2 == 1:
            s+=no_dots +'\n'
        #This next block handles the second row, if dice_1 =6 then add two dots
        if dice_1 == 6:
            s+=offset_right+two_dots+gap_between_dice 
            #If dice_2 is 6, also add two dots 
            if dice_2 == 6:
                s+=two_dots + '\n'
            #If dice 2 is an odd number, put one dot in the center
            elif dice_2 % 2 == 1:
                s+=one_dot_center + '\n'
            #If dice_2 is 2 or 4 then don't put any dots in the center
            elif dice_2 % 2 == 0:
                s+=no_dots +'\n'
        #If dice_1 is 5 then put one dot in the center.
        elif dice_1 == 5:
            s+=offset_right+one_dot_center + gap_between_dice
            #Same logic as the previous block for handling the middle row of the second dice
            if dice_2 == 6:
                s+=two_dots + '\n'
            elif dice_2 % 2 == 1:
                s+=one_dot_center + '\n'
            elif dice_2 % 2 == 0:
                s+=no_dots +'\n'
        #If dice_1 is 4, then there should be no dots in the middle row
        else:
            s+=offset_right+no_dots + gap_between_dice
            #Apply same middle row logic as before for dice 2.
            if dice_2 == 6:
                s+=two_dots + '\n'
            elif dice_2 % 2 == 1:
                s+=one_dot_center + '\n'
            elif dice_2 % 2 == 0:
                s+=no_dots +'\n'
        #Since dice_1 is greater than or equal to 4, always add two dots to the bottom  row
        s+=offset_right+two_dots + gap_between_dice
        #Bottom row of dice_2 will have two dots if its 4,5,6
        if dice_2 >= 4:
            s+=two_dots + '\n'
        #Bottom row of dice_2 will have one dot right if its 3 or 2
        elif dice_2 >= 2:
            s+=one_dot_right +'\n'
        #No dots on the bottom row of dice_2 if its 1 
        elif dice_2 == 1:
            s+=no_dots +'\n'
    
    elif dice_1 >= 2:
        s+=offset_right+one_dot_left + gap_between_dice
        if dice_2 >= 4:
            s+=two_dots + '\n'
        elif dice_2 >= 2:
            s+=one_dot_left +'\n'
        elif dice_2 == 1:
            s+=no_dots +'\n'
        if dice_1 == 3:
            s+=offset_right+one_dot_center + gap_between_dice
            if dice_2 == 6:
                s+=two_dots + '\n'
            elif dice_2 % 2 == 1:
                s+=one_dot_center + '\n'
            elif dice_2 % 2 == 0:
                s+=no_dots +'\n'    
        else:
            s+=offset_right+no_dots + gap_between_dice
            if dice_2 == 6:
                s+=two_dots + '\n'
            elif dice_2 % 2 == 1:
                s+=one_dot_center + '\n'
            elif dice_2 % 2 == 0:
                s+=no_dots +'\n'
        s+=offset_right+one_dot_right + gap_between_dice
        if dice_2 >= 4:
            s+=two_dots + '\n'
        elif dice_2 >= 2:
            s+=one_dot_right +'\n'
        elif dice_2 == 1:
            s+=no_dots +'\n'
    
    else:
        s+=offset_right+no_dots + gap_between_dice
        if dice_2 >= 4:
            s+=two_dots + '\n'
        elif dice_2 >= 2:
            s+=one_dot_left +'\n'
        elif dice_2 == 1:
            s+=no_dots +'\n'
        s+=offset_right+one_dot_center + gap_between_dice
        if dice_2 == 6:
            s+=two_dots + '\n'
        elif dice_2 % 2 == 1:
            s+=one_dot_center + '\n'
        elif dice_2 % 2 == 0:
            s+=no_dots +'\n'
        s+=offset_right+no_dots + gap_between_dice
        if dice_2 >= 4:
            s+=two_dots + '\n'
        elif dice_2 >= 2:
            s+=one_dot_right +'\n'
        elif dice_2 == 1:
            s+=no_dots +'\n'
    
    s+=offset_right+'-----'+gap_between_dice+'-----\n'
    print(s)
    # print(s1+dot[dice_2&1]+s1[::-1])
    time.sleep(0.033)
