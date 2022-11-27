from random import*
import os
import time
import math

def draw_images(on_screen_images, blank_code, delay):
    #Clear screen
    os.system('cls')
    #Start by figuring out how many rows you'll need to draw
    #This will be the greatest combination of rows and offset down for each object
    total_rows = 0
    for image in range(0,len(on_screen_images)):
        if len(on_screen_images[image][0]) + on_screen_images[image][1] > total_rows:
            total_rows = len(on_screen_images[image][0]) + on_screen_images[image][1]
    
    #Final String to be constructed throughout then printed at the end
    output_str = ""

    #Loop through each row
    for row in range(0,total_rows):
        #Records the furthest to the right the row has gotten
        max_right = 0
        #Loop through each image
        for image in range(0, len(on_screen_images)):
            #Only change the output string if part of this image is in this row
            if row >= on_screen_images[image][1] and row < len(on_screen_images[image][0]) + on_screen_images[image][1]:
                #Allows for the offset down of the image of the image 
                adj_row = row-on_screen_images[image][1]
                #If this slice of the image is to the right of everything else on the screen
                if on_screen_images[image][2] >= max_right:
                    #See how much farther to the right, and then fill that in with blank spaces
                    gap_num = on_screen_images[image][2] - max_right
                    for gap in range(0,gap_num):
                        output_str += " "
                    #Add the whole row to output_str and reset max_right
                    for char in range(0,len(on_screen_images[image][0][adj_row])):
                        if on_screen_images[image][0][adj_row][char] == blank_code:
                            output_str += " "
                        #Otherwise just utilize the character
                        else:
                            output_str += on_screen_images[image][0][adj_row][char]
                    max_right += gap_num + len(on_screen_images[image][0][adj_row])
                #Overlaps with the farthest thing to the right. Causes the max_right to increase    
                elif on_screen_images[image][2] < max_right and on_screen_images[image][2] + len(on_screen_images[image][0][adj_row]) >= max_right:
                    #Calculates how many characters overlap, intentionally negative
                    back_num = on_screen_images[image][2] - max_right
                    #Keeps the overlap string in a seperate variable then slices it off
                    overlap_str = output_str[back_num:]
                    output_str = output_str[:back_num]
                    #Goes through character by character
                    for char in range(0,len(on_screen_images[image][0][adj_row])):
                        #If there might still be overlap
                        if char < abs(back_num):
                            #Add a blank space if you specify the designated blank_code
                            if on_screen_images[image][0][adj_row][char] == blank_code:
                                output_str += " "
                            #If its not blank, then add the character
                            elif on_screen_images[image][0][adj_row][char] != " ":
                                output_str += on_screen_images[image][0][adj_row][char]
                            #If it is blank, use the pre-existing character from the overlap string
                            else:
                                output_str += overlap_str[char]
                        #If we're past the point of overlap
                        else:
                            #Still check to see if the blank code has been entered
                            if on_screen_images[image][0][adj_row][char] == blank_code:
                                output_str += " "
                            #Otherwise just utilize the character
                            else:
                                output_str += on_screen_images[image][0][adj_row][char]
                    #Resets the max_right value
                    max_right = max_right + back_num + len(on_screen_images[image][0][adj_row])
                #Won't cause max right to increase, May or may not be any overlap with anything else
                else:
                    #back_num_1 is for the starting location
                    back_num_1 = on_screen_images[image][2] - max_right
                    #back_num_2 is for the end location
                    back_num_2 = back_num_1 + len(on_screen_images[image][0][adj_row])
                    #Saves the string that will be added back at the end, then slices it off.
                    add_back_str = output_str[back_num_2:]
                    output_str = output_str[:back_num_2]
                    #Calculates the size of the overlap string then saves it, then slices it off
                    overlap_num = abs(back_num_2)-abs(back_num_1)
                    overlap_str = output_str[overlap_num:] 
                    output_str = output_str[:overlap_num]
                    #Goes character by character
                    for char in range(0,len(on_screen_images[image][0][adj_row])):
                        #Blank code causes it to add a blank that covers up previous layers
                        if on_screen_images[image][0][adj_row][char] == blank_code:
                            output_str += " "
                        #If its not blank, add the character from this layer
                        elif on_screen_images[image][0][adj_row][char] != " ":
                            output_str += on_screen_images[image][0][adj_row][char]
                        #If it is transparent add back the characters from the overlap string
                        else:
                            output_str += overlap_str[char]
                    output_str += add_back_str
        #Done with the row, add a newline character
        output_str += '\n'
    print(output_str)
    time.sleep(delay)


#List of all images
images = [[ '_________', 
            '|BBBBBBB|', 
            '|BBBBBBB|', 
            '|BDeathB|', 
            '|BChestB|', 
            '|BBBBBBB|', 
            '|_______|'],

            ['       ___  ',
             '      / \B\ ',
             '     /   |B|',
             '    /    |B/',
             '   /     |/ ',
             '  /         ',
             ' /          ',
             '/           '],
             ['   _____    ',
              '  /BBBBB\   ',
              '  |BoBoB|   ',
              '   \B-B/    ',
              '    _|_     ',
              '   / | \    ',
              '  /  |  \   ',
              ' / _ | _ \  ',
              '   |\|/|    ',
              '   |   |   '],
             ['   _____    ',
              '  /BBBBB\   ',
              '  |BoBoB|   ',
              '   \B-B/    ',
              '  ___|___   ',
              ' /   |   \  ',
              '/    |    \ ',
              '    _|_     ',
              '   |   |    ',
              '   |   |    ' ], 
              ['    _____    ',
               '   /BBBBB\    ',
               '   |BoBoB|    ',
               '    \B-B/     ',
               '______|_______',
               '      |       ',
               '      |       ',
               '     / \      ',
               '    /   \     ',
               '   /     \    ',
               '  /       \   '],
               ['    _____    ',
               '   /BBBBB\    ',
               '   |BoBoB|    ',
               '\   \B-B/    /',
               ' \____|_____/ ',
               '      |       ',
               '      |       ',
               '     / \      ',
               '    /   \     ',
               '   /     \    ',
               '  |       |   '],
               ['    _____    ',
                '\  /BBBBB\   /',
                ' \ |BoBoB|  / ',
                '  \ \B-B/  /  ',
                '   \__|___/   ',
                '      |       ',
                '      |       ',
                '     / \      ',
                '    |   |     ',
                '    |   |     ',
                '    |   |     '],
                ['     _____    ',
                 '  / /BBBBB\ \ ',
                 '  | |BoBoB| | ',
                 '  \  \B-B/  / ',
                 '   \___|___/  ',
                 '       |      ',
                 '       |      ',
                 '      / \     ',
                 '     /   \    ',
                 '    /     \   ',
                 '   /       \   ']]

#Each list should have the object you want to draw, followed by the offset down from the top, and the offset to the right
#Items earlier in the list will be added to the base layer
on_screen_images = []
blank_code = "B"
delay = 0.033

# draw_images(on_screen_images,blank_code,delay)

# for x in range(0,100):
#     on_screen_images[0][1] += randint(-1,2)
#     on_screen_images[0][2] += randint(-1,2)
#     draw_images(on_screen_images,blank_code,delay) 

for x in range(0,50):
    on_screen_images.append([images[0],3,50])

on_screen_images.append([images[1],0,0])

for x in range(0,45):
    on_screen_images[50][2] = x
    draw_images(on_screen_images,blank_code,delay)

for y in range(0,3):
    for x in range(0,4):
        for image in range(0,len(on_screen_images)):
            on_screen_images[image][1] += 1
        draw_images(on_screen_images,blank_code,delay)

    for x in range(0,4):
        for image in range(0,len(on_screen_images)):
            on_screen_images[image][1] -= 1
        draw_images(on_screen_images,blank_code,delay)

del(on_screen_images[50])

for x in range(0,200):
    for image in range(0,len(on_screen_images)):
        on_screen_images[image][1] += round(2*random() - 1)
        on_screen_images[image][2] += round(3*random() - 1.5)
        if on_screen_images[image][1] < 0:
            on_screen_images[image][1] = 0
        elif on_screen_images[image][1] > 15:
            on_screen_images[image][1] = 15
        if on_screen_images[image][2] < 0:
            on_screen_images[image][2] = 0
        if on_screen_images[image][2] > 200:
            on_screen_images[image][2] = 200
    draw_images(on_screen_images,blank_code,delay)


# on_screen_images = [[images[0],10,80], [images[0],9,71], [images[0],9,81], [images[0],10,70], [images[0],9,74],
#                     [images[0],9,66], [images[0],9,72], [images[0],9,69], [images[0],9,93], [images[0],9,80],
#                     [images[0],10,66], [images[0],10,68], [images[0],10,73], [images[0],9,75], [images[0],9,72],
#                     [images[0],8,73], [images[0],10,78], [images[0],9,68], [images[0],10,87], [images[0],10,77],
#                     [images[1],9,64]]

# draw_images(on_screen_images, blank_code, delay)

on_screen_images = []
delay = 3

draw_images(on_screen_images,blank_code,delay)

delay = 0.033

for y in range(0,10):
    for x in range(2,8):
        on_screen_images.append([images[x],10-x,50])
        draw_images(on_screen_images,blank_code,delay)
        del(on_screen_images[0])

    for x in range(7,1,-1):
        on_screen_images.append([images[x],10-x,50])
        draw_images(on_screen_images,blank_code,delay)
        del(on_screen_images[0])