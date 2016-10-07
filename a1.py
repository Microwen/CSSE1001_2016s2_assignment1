#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4378702
#
#   Student Name: Youwen Mao
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from a1_support import *

# End of support code
################################################################

# Write your code here

def get_position_in_direction(position,direction):
    """Return the change position after a vaild position has been inputed.

    Precondition:<position> -> tuple, <direction> -> string

    get_position_in_direction(tuple,str) -> tuple
    """
    row, column = position
    for i in DIRECTION_DELTAS:
        if i == direction:
            rowc, columnc = DIRECTION_DELTAS[i]
            row += rowc
            column += columnc
    position = (row,column)
    return position

def print_maze(maze,position):
    """Display the maze maps

    Precondition:<maze> -> string, position -> tuple
    
    print_maze(str,tuple) -> str
    """
    
    row, colunm = position
    mazef = maze[0:(maze_columns(maze)+1)*row+colunm]
    mazeb = maze[(maze_columns(maze)+1)*row+colunm+1:]
    mazep = mazef + PLAYER + mazeb
    print(mazep)
    
def move(maze, position, direction):
    """Return the changed position according to user's command

    Precondition: <maze> -> string, <position> -> tuple, <direction> -> string
    
    move(maze, position, commands) -> tuple
    """
    loc = get_position_in_direction(position,direction)
    row, columns = loc
    det = maze[(maze_columns(maze)+1)*row+columns]
    if det == WALL:
        loc = position
    return loc, det



def get_legal_directions(maze, position):
    """Return the possible directions which the player can move to

    Precondition:<maze> -> string, <position> -> tuple

    get_legal_directions(str, tuple) -> list
    """
    row, colunm = position
    N = ''
    S = ''
    W = ''
    E = ''
    if maze[(maze_columns(maze)+1)*(row-1)+colunm] != WALL :
        N = 'n '
    if maze[(maze_columns(maze)+1)*(row+1)+colunm] != WALL :
        S = 's '
    if maze[(maze_columns(maze)+1)*row+(colunm+1)] != WALL :
        E = 'e '
    if maze[(maze_columns(maze)+1)*row+(colunm-1)] != WALL :
        W = 'w ' 
    combined = N+S+E+W
    return str(combined).split()
    
def interact():
    """Start the game.

    Main structure of the game. Ask the user for the commands.
    Work out the result and show it to the user.
    
    """
    # Add your code for interact here
    maps = input('Maze File: ')
    maze = load_maze(maps)
    position = START_POSITION
    bur = []
    buc = []
    count = 0
    while True:
        print('')
        print_maze(maze,position)
        print('')
        commands = input('Command: ')
        commands = commands.strip()
        if commands == '?':
            print(HELP_TEXT)
        elif commands == 'r':
            position = START_POSITION
            bur = []
            buc = []
            count = 0
            #########
        elif commands == 'b':
            if bur != []:
                if count != 1:
                    count -= 1
                    position = (bur[count-1],buc[count-1])
                    del bur[-1]
                    del buc[-1]
                    #########
                else:
                    bur = []
                    buc = []
                    position = START_POSITION
                    print_maze(maze,position)
                    count = 0
            else:
                #########
                print("You cannot go back from the beginning.")
        elif commands == 'p':
            result = ''
            lenght = len(get_legal_directions(maze, position))
            count = 0
            for i in get_legal_directions(maze, position):
                result += i
                count += 1
                if lenght == count:
                    pass
                else:
                    result +=', '
            print('Possible directions: '+result)
        elif commands == 'q':
            quit = input('Are you sure you want to quit? [y] or n: ')
            if quit != 'n':
                break
                #########
        elif commands in ['n','s','w','e']:
            position, cmd = move(maze, position, commands)
            if position == START_POSITION and count == 0:
                #########
                print("You can't go in that direction.")
            else:
                
                if cmd in BAD_POKEMON:
                    for i in POKEMON:
                        if cmd == i:
                            target = POKEMON[i]
                            print(LOSE_TEXT.format(target))
                    break
                elif cmd in GOOD_POKEMON:
                    print(WIN_TEXT.format(POKEMON['P']))
                    break
                else:
                    #########
                    row, colunm = position
                    bur.append('')
                    buc.append('')
                    bur[count] = row
                    buc[count] = colunm
                    count += 1
                    if count >= 2:
                        if bur[count-1] == bur[count-2]:
                            if buc[count-1] == buc[count-2]:
                                del bur[count-1]
                                del buc[count-1]
                                count -= 1
                                print("You can't go in that direction.")
        else:
            print('Invalid command: '+commands)
            #########
            
    pass

##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()
