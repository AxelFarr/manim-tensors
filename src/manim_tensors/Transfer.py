from manim import *
from manim_tensors import Tensor

class Transfer():
    def __init__(self, src: Tensor, dst: Tensor):
        self.src = src
        self.dst = dst
        self.it = 0
        self.init_transfer()

    def init_transfer(self):
        # Offsets
        self.initial_ioffset = 0
        self.initial_doffset = 0
        
        # Trigger
        self.trig = 1

        # Source user counters
        self.icnt0 = 1
        self.icnt1 = 1
        self.icnt2 = 1
        self.icnt3 = 1
        self.icnt4 = 1
        self.icnt5 = 1

        # Source dimensions (offsets)
        self.dim1 = 1
        self.dim2 = 1
        self.dim3 = 1
        self.dim4 = 1
        self.dim5 = 1

        # Destination user counters
        self.dicnt0 = 1
        self.dicnt1 = 1
        self.dicnt2 = 1
        self.dicnt3 = 1
        self.dicnt4 = 1
        self.dicnt5 = 1

        # Destination dimenstions (offsets)
        self.ddim1 = 1
        self.ddim2 = 1
        self.ddim3 = 1
        self.ddim4 = 1
        self.ddim5 = 1
    
    def itrig(self):
        i0 = self.it % self.icnt0
        i1 = (self.it // self.icnt0) % self.icnt1
        i2 = (self.it // (self.icnt0 * self.icnt1)) % self.icnt2
        i3 = (self.it // (self.icnt0 * self.icnt1 * self.icnt2)) % self.icnt3
        i4 = (self.it // (self.icnt0 * self.icnt1 * self.icnt2 * self.icnt3)) % self.icnt4

        if self.trig == 1:
            return True if i0 == 0 else False
        if self.trig == 2:
            return True if i1 == 0 and i0 == 0 else False
        if self.trig == 3:
            return True if i2 == 0 and i1 == 0 and i0 == 0 else False
        if self.trig == 4:
            return True if i3 == 0 and i2 == 0 and i1 == 0 and i0 == 0 else False
        if self.trig == 5:
            return True if i4 == 0 and i3 == 0 and i2 == 0 and i1 == 0 and i0 == 0 else False

    def dtrig(self):
        di0 = self.it % self.dicnt0
        di1 = (self.it // self.dicnt0) % self.dicnt1
        di2 = (self.it // (self.dicnt0 * self.dicnt1)) % self.dicnt2
        di3 = (self.it // (self.dicnt0 * self.dicnt1 * self.dicnt2)) % self.dicnt3
        di4 = (self.it // (self.dicnt0 * self.dicnt1 * self.dicnt2 * self.dicnt3)) % self.dicnt4

        if self.trig == 1:
            return True if di0 == 0 else False
        if self.trig == 2:
            return True if di1 == 0 and di0 == 0 else False
        if self.trig == 3:
            return True if di2 == 0 and di1 == 0 and di0 == 0 else False
        if self.trig == 4:
            return True if di3 == 0 and di2 == 0 and di1 == 0 and di0 == 0 else False
        if self.trig == 5:
            return True if di4 == 0 and di3 == 0 and di2 == 0 and di1 == 0 and di0 == 0 else False

    def get_curr_ioffset(self):
        i0 = self.it % self.icnt0
        i1 = (self.it // self.icnt0) % self.icnt1
        i2 = (self.it // (self.icnt0 * self.icnt1)) % self.icnt2
        i3 = (self.it // (self.icnt0 * self.icnt1 * self.icnt2)) % self.icnt3
        i4 = (self.it // (self.icnt0 * self.icnt1 * self.icnt2 * self.icnt3)) % self.icnt4
        i5 = (self.it // (self.icnt0 * self.icnt1 * self.icnt2 * self.icnt3 * self.icnt4)) % self.icnt5
        return i5 * self.dim5 + i4 * self.dim4 + i3 * self.dim3 + i2 * self.dim2 + i1 * self.dim1 + i0 + self.initial_ioffset

    def get_curr_doffset(self):
        di0 = self.it % self.dicnt0
        di1 = (self.it // self.dicnt0) % self.dicnt1
        di2 = (self.it // (self.dicnt0 * self.dicnt1)) % self.dicnt2
        di3 = (self.it // (self.dicnt0 * self.dicnt1 * self.dicnt2)) % self.dicnt3
        di4 = (self.it // (self.dicnt0 * self.dicnt1 * self.dicnt2 * self.dicnt3)) % self.dicnt4
        di5 = (self.it // (self.dicnt0 * self.dicnt1 * self.dicnt2 * self.dicnt3 * self.dicnt4)) % self.dicnt5
        return di5 * self.ddim5 + di4 * self.ddim4 + di3 * self.ddim3 + di2 * self.ddim2 + di1 * self.ddim1 + di0 + self.initial_doffset

    def get_nb_trigs(self):
        if self.trig == 1:
            return min(self.icnt1 * self.icnt2 * self.icnt3 * self.icnt4 * self.icnt5,
                       self.dicnt1 * self.dicnt2 * self.dicnt3 * self.dicnt4 * self.dicnt5)
        elif self.trig == 2:
            return min(self.icnt2 * self.icnt3 * self.icnt4 * self.icnt5,
                       self.dicnt2 * self.dicnt3 * self.dicnt4 * self.dicnt5)
        elif self.trig == 3:
            return min(self.icnt3 * self.icnt4 * self.icnt5,
                       self.dicnt3 * self.dicnt4 * self.dicnt5)
        elif self.trig == 4:
            return min(self.icnt4 * self.icnt5,
                       self.dicnt4 * self.dicnt5)
        elif self.trig == 5:
            return min(self.icnt5, self.dicnt5)

    def trigger(self, scene):
        anim = []

        while True:
            # Source
            ioffset = self.get_curr_ioffset()
            ix, iy, iz = self.src.get_coord_from_offset(ioffset)
            src_unit = self.src.get_unit(ix, iy, iz)

            # Destination
            doffset = self.get_curr_doffset()
            dx, dy, dz = self.dst.get_coord_from_offset(doffset)
            dst_unit = src_unit.copy()
            anim.append(self.dst.add_unit(dst_unit, dx, dy, dz))

            # Update transfer counter
            self.it += 1
            if self.itrig() or self.dtrig():
                break

        # Play animations
        scene.play(AnimationGroup(*anim, lag_ratio=0))