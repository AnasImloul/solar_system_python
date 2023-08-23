class Moveable:
    def __init__(self, pos=None, velocity=None):
        self.pos = [0, 0]
        self.velocity = [0, 0]

        if pos is not None:
            self.pos = [pos[0], pos[1]]
        if velocity is not None:
            self.velocity = [velocity[0], velocity[1]]

    def move(self, dt):
        self.pos[0] += self.velocity[0] * dt
        self.pos[1] += self.velocity[1] * dt

    def accelerate(self, acceleration, dt):
        self.velocity[0] += acceleration[0] * dt
        self.velocity[1] += acceleration[1] * dt

    def set_velocity(self, velocity):
        self.velocity[0] = velocity[0]
        self.velocity[1] = velocity[1]

