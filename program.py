# Assignment:
# Your assignment is to write the control program for a robot. Anything not described in the task (such as wether to implement a full UI or use strings as input)is up to you. 

# The robot is located in a two-dimensional room and moves around in the room by parsing a string of commands in English:

# L - Turn left  R - Turn right  F - Move forward
# Example string: LFFRFRFRFF

# When the robot runs out of commands, it shall report what square (x,y) it’s located at, and what direction it’s facing. When the program starts, you must be able to specify the size of the room, where the robot is located and which direction it is facing.


# Example 1: 
# Starting the program with a 5x5 room, and start position (1,2,N)
 
# The instructions “RFRFFRFRF” will result in the report “1 3 N”

# Example 2:
# Starting the program with a 5x5 room, and start position (0,0,E)

# The instructions “RFLFFLRF” will result in the report “3 1 E”

from typing import Type
from controller import navigate_room

navigate_room(5,5,'E',0,0,'RFLFFLRF')

# while exit:
#     try:
#         w = int(input('Enter the width of the room (Integers 0-100, inclusive): '))
#     except TypeError(w):
#         print(f'{type(w)} is not valid')
#     if w < 0 or w > 100:
#         print('Only numbers 0-100, inclusive, are valid')
#         raise ValueError(w)

#     try:
#         h = int(input('Enter the height of the room (Integers 0-100, inclusive): '))
#     except TypeError(h):
#         print(f'{type(h)} is not valid')
#     if h < 0 or h > 100:
#         print('Only numbers 0-100, inclusive, are valid')
#         raise ValueError(h)

#     print(f'Great! Your room is now {w} x {h}')

#     try:
#         x = int(input(f'Enter a starting x coordinate, valid coordinates go from 0-{w-1}, inclusive: '))
#     except TypeError(x):
#         print(f'{type(x)} is not valid')
#     if x < 0 or x > w-1:
#         print(f'Only numbers 0-{w-1}, inclusive, are valid')
#         raise ValueError(x)
    
#     try:
#         y = int(input(f'Enter a starting y coordinate, valid coordinates go from 0-{h-1}, inclusive: '))
#     except TypeError(y):
#         print(f'{type(y)} is not valid')
#     if y < 0 or y > h-1:
#         print(f'Only numbers 0-{h-1}, inclusive, are valid')
#         raise ValueError(y)

#     valid_directions = ['n','e','s','w']

#     try:
#         d = str(input('Enter a starting direction, "N", "E", "S", "W" are valid options: '))
#     except TypeError(d):
#         print(f'{d} is not valid')
#     if str.casefold(d) not in valid_directions:
#         print(f'{d} is not a valid char')
#         raise ValueError(d)

#     valid_commands = ['l','r','f']

#     try:
#         c = str((input('Enter a combination of comands, "L" - Left, "R" - Right, "F" - Forward are valid options, example: "FRLLFRRF": ')))
#     except TypeError(c):
#         print(f'{c} is not valid')
#     for x in c:
#         if str.casefold(x) not in valid_commands:
#             print(f'{x} is not a valid char')
#             raise ValueError(x)

#     navigate_room(room_width=w, room_height=h, facing_direction=d, x_start=x, y_start=y, instructions=c)

#     exit = input('Enter (1) to try again or (0) to exit the program: ')

    

