from models.room import Room

class Robot(object):
    def __init__(self, facing_direction:str, x:int, y:int, room:Room=None):
        self._facing_direction = str.casefold(facing_direction)
        self._room = room
        self._x_pos = x
        self._y_pos = y
        self._valid_directions = ['n','e','s','w'] #{'n':'North'},{'e':'East'},{'s':'South'},{'w':'West'}

    @property
    def facing_direction(self):
        return self._facing_direction

    @facing_direction.setter
    def facing_direction(self, facing_direction:str):
        self._facing_direction = str.casefold(facing_direction)

    @property
    def valid_directions(self):
        return self._valid_directions

    @property
    def x_pos(self):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, x:int):
        self._x_pos = x

    @property
    def y_pos(self):
        return self._y_pos

    @y_pos.setter
    def y_pos(self, y:int):
        self._y_pos = y

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room:Room):
        self._room = room

    def current_posistion(self):
        return f'{self.room.layout[self.x_pos][self.y_pos]}{self.facing_direction}'

    def turn_right(self):
        for i in range(len(self.valid_directions)):
            if i == len(self.valid_directions)-1:
                self.facing_direction = self.valid_directions[0]
                break
            elif self.facing_direction == self.valid_directions[i]:
                self.facing_direction = self.valid_directions[i+1]
                break

    def turn_left(self):
        for i in range(len(self.valid_directions)):
            if i == len(self.valid_directions)-1:
                self.facing_direction = self.valid_directions[0]
                break
            elif self.facing_direction == self.valid_directions[i]:
                self.facing_direction = self.valid_directions[i-1]
                break

    def forward(self):
        if self.facing_direction == 'n' and self.y_pos < self.room.height -1:
            self.y_pos += 1
        elif self.facing_direction == 'e' and self.x_pos < self.room.width -1:
            self.x_pos += 1
        elif self.facing_direction == 's' and self.y_pos > 0:
            self.y_pos -= 1
        elif self.facing_direction == 'w' and self.x_pos > 0:
            self.x_pos -= 1

    def move(self, command):
        command = str.casefold(command)
        if command == 'f':
            self.forward()
            print(f'Moved forward, now in square {self.current_posistion()}')
        elif command == 'r':
            self.turn_right()
            print(f'Turned right, now facing {self.facing_direction}')
        elif command == 'l':
            self.turn_left()
            print(f'Turned left, now facing {self.facing_direction}')
        else:
            raise ValueError(command)

