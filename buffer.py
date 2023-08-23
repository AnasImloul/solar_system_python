class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0 for i in range(size)]
        self.index = 0
        self.sum = 0

    def add(self, value):
        if self.index < self.size:
            self.sum += value
        else:
            self.sum += value
            self.sum -= self.buffer[self.index % self.size]

        self.buffer[self.index % self.size] = value
        self.index += 1

    def sum(self):
        return self.sum

    def average(self):
        if self.index == 0:
            return 0
        elif self.index < self.size:
            return self.sum / self.index
        else:
            return self.sum / self.size