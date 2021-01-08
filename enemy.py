from header import *


class enemy:
    static = pygame.transform.scale(pygame.image.load('Eliteknightshotgun.png'), (64, 64))

    def __init__(self, x, y, width, height, vel, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.damage = dam
        self.end = end
        self.path = [self.x, self.end]
        # self.count = 0# for animation later
        self.velocity = vel
        self.hitbox = (self.x + 30, self.y + 30, 40, 90)

    def draw(self, screen):
        self.move()
        if self.velocity > 0:
            screen.blit(self.static, (self.x, self.y))
        self.hitbox = (self.x + 30, self.y + 30, 40, 90)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2) #drawing hitbox right now

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1  # for reversing path, not used currently
                # self.count = 0# for animation later
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity

    def hit(self,dam):
        print("Hit!")
        self.dam = dam

        #if self.miss


