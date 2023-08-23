import heapq


class RenderSystem:
    def __init__(self):
        self.renderQueue = []

    def add(self, drawable, priority=0):
        heapq.heappush(self.renderQueue, (-priority, drawable))

    def draw(self, win, scale, offset):
        tmp = self.renderQueue.copy()
        while len(tmp) > 0:
            _, drawable = heapq.heappop(tmp)
            drawable.draw(win, scale, offset)
