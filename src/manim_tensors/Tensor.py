import numpy as np
from manim import *
from manim_tensors import Unit

class Tensor(VGroup):
    def __init__(self, width = 0, height = 0, depth = 0, origin = [0, 0, 0], empty = False):
        super().__init__()
        self.mwidth = width
        self.mheight = height
        self.mdepth = depth
        self.buff = 0.025   # Gap between units
        self.origin = origin
        if not empty:
            self.init_tensor()

    def init_tensor(self):
        for z in range(self.mdepth):
            for y in range(self.mheight):
                for x in range(self.mwidth):
                    self.create_unit(x, y, z)

    # Moves
    def shift(self, direction):
        self.origin = self.origin + direction
        return super().shift(direction)

    # Getters
    def dims(self):
        return [self.mwidth, self.mheight, self.mdepth]
    
    def get_unit(self, x, y, z):
        for unit in self:
            if unit.mx == x and unit.my == y and unit.mz == z:
                return unit
            
    def get_coord_from_offset(self, offset):
        z = offset // (self.mwidth * self.mheight)
        offset %= self.mwidth * self.mheight
        y = offset // self.mwidth
        x = offset % self.mwidth
        return x, y, z

    # Others
    def empty(self):
        for unit in self:
            self.remove(unit)
        return self
    
    def create_unit(self, x, y, z):
        unit = Unit(x, y, z)
        pos = self.origin
        unit.move_to([pos[0] + x * (unit.width + self.buff),
                      pos[1] - y * (unit.height + self.buff),
                      pos[2] + z * (unit.depth + self.buff)], aligned_edge=UL)
        self.add(unit)
        
        # Update tensor dimensions
        if x >= self.mwidth:
            self.mwidth = x + 1
        if y >= self.mheight:
            self.mheight = y + 1
        if z >= self.mdepth:
            self.mdepth = z + 1

    def add_unit(self, unit, x, y, z):
        unit.mx = x
        unit.my = y
        unit.mz = z

        pos = self.origin
        self.add(unit)

        # Update tensor dimensions
        if x >= self.mwidth:
            self.mwidth = x + 1
        if y >= self.mheight:
            self.mheight = y + 1
        if z >= self.mdepth:
            self.mdepth = z + 1

        return unit.animate.move_to([pos[0] + x * (unit.width + self.buff),
                                     pos[1] - y * (unit.height + self.buff),
                                     pos[2] + z * (unit.depth + self.buff)], aligned_edge=UL)
