from manim import *

class Unit(Cube):
    def __init__(self, x, y, z):
        super().__init__()
        self.mx = x
        self.my = y
        self.mz = z

        self.scale(0.1)
        self.set_stroke(WHITE, width=1)
