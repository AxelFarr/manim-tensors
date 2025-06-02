from manim import *
from manim_tensors import Tensor, Transfer

class CreateTensor(ThreeDScene):
    def construct(self):
        src = Tensor(8, 8, 1).shift(LEFT * 4)
        self.add(src)
        dst = Tensor(8, 8, 1, empty = True)
        self.add(dst)

        src.get_unit(0, 0, 0).set_color(RED)
        src.get_unit(1, 0, 0).set_color(GREEN)

        # Setup transfer
        tr = Transfer(src, dst)
        tr.icnt0 = 8
        tr.icnt1 = 1
        tr.icnt2 = 2
        tr.dim2 = 8

        tr.dicnt0 = 1
        tr.dicnt1 = 8
        tr.dicnt2 = 2
        tr.ddim1 = 8
        tr.ddim2 = 1

        tr.trig = 2

        # Trigger transfer
        tr.trigger(self)
        tr.trigger(self)
