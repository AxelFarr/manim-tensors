from manim import *
from manim_tensors import Tensor

class CreateTensor(Scene):
    def construct(self):
        tensor = Tensor(1, 10, 10)
        self.add(tensor)
