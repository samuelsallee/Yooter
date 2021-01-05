from header import *


class enemy:
    static = pygame.image.load('Eliteknightshotgun.png')

    def __init__(self, x, y, width, height, vel, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.damage = dam
        self.end = end
        self.path = [self.x, self.end]
        # self.count = 0# for animation later
        self.velocity = vel

    def draw(self, win):
        self.move()
        if self.velocity > 0:
            win.blit(self.static, (self.x, self.y))

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1 # for reversing path, not used currently
                # self.count = 0# for animation later
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
