from trail import Trail


class Trailable:
    def __init__(self, color, max_size, refresh_rate):
        self.trail = Trail(self, color, max_size, refresh_rate)

    def add_point(self, point):
        if point is not None:
            self.trail.add_point(point)

    def draw_trail(self, win):
        self.trail.draw(win)

    def clear_trail(self):
        self.trail.clear()
