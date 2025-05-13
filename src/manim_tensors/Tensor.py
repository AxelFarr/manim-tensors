from manim import *
from manim_tensors import Unit

class Tensor(VGroup):
    def __init__(self, depth, height, width):
        super().__init__()
        self.mdepth = depth
        self.mheight = height
        self.mwidth = width
        self.buff = 0.025   # Gap between units
        self.init_tensor()

    def add_unit(self, x, y, z):
        unit = Unit(x, y, z)
        pos = self.get_corner(UL)
        unit.move_to([pos[0] + x * (unit.width + self.buff),
                      pos[1] - y * (unit.height + self.buff),
                      pos[2] + z * (unit.depth + self.buff)], aligned_edge=UL)
        self.add(unit)

    def init_tensor(self):
        for z in range(self.mdepth):
            for y in range(self.mheight):
                for x in range(self.mwidth):
                    self.add_unit(x, y, z)
    