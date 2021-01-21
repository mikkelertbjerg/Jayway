class Room(object):
    def __init__(self, width:int, height:int):
        self._width = width
        self._height = height
        self._layout = None
        self.create_room()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width:int):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height:int):
        self._height = height

    @property
    def layout(self):
        return self._layout

    def create_room(self):
        self._layout = [[0 for x in range(self.width)] for y in range(self.height)]
        for i in range(self.width):
            for j in range(self.height):
                self._layout[i][j] = f'{i}.{j}'
        #self._layout.reverse()
                
    
