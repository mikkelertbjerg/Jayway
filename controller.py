from models.robot import Robot
from models.room import Room

def create_room(room_width, room_height):
    room = Room(width=room_width, height=room_height)
    return room

def create_robot(facing_direction, x_start, y_start, room):
    robot = Robot(facing_direction=facing_direction, x=x_start, y=y_start, room=room)
    return robot

def navigate_room(room_width, room_height, facing_direction, x_start, y_start, instructions):

    room = create_room(room_width=room_width, room_height=room_height)
    print('Room created, layout:')
    for row in room.layout:
        for col in row:
            print(col, end=' ')
        print()

    robot = create_robot(facing_direction=facing_direction, x_start=x_start, y_start=y_start, room=room)
    print(f'Robot created, starting posistion is: {robot.x_pos}.{robot.y_pos} {robot.facing_direction}')

    print(f'Instrcutions: {instructions}')
    for char in instructions:
        robot.move(char)


