from ursina import *

class Voxel(Button):
    def __init__(self, position: tuple[int], texture=None):
        super().__init__(
                position = position,
                color = color.white,
                scale = (2, 2, 2),
                highlight_color = color.lime
                )
    
    # input function for destroying and create blocks
    def input(self):
        pass

