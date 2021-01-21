from header import *


class enemy:
    static = pygame.transform.scale(pygame.image.load('Eliteknightshotgun.png'), (64, 64))

    def __init__(self, x, y, width, height, vel, end, health):
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
        self.health = health

    def draw_pause(self, screen):
        screen.blit(self.static, (self.x, self.y))
        
    def draw(self, screen, player_x, player_y, xDelta, yDelta):
        self.move(player_x, player_y, xDelta, yDelta)
        if self.velocity > 0:
            screen.blit(self.static, (self.x, self.y))
        self.hitbox = (self.x + 30, self.y + 30, 40, 90)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 10))
        pygame.draw.rect(screen, (0, 128, 0), (self.x, self.y, self.health/2, 10))
        #pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)  # drawing hitbox right now

    def move(self, player_x, player_y, xDelta, yDelta):
        radian = math.atan2((self.y - player_y), (self.x - player_x))
        enemy_delta_y = math.sin(radian) * -3
        enemy_delta_x = math.cos(radian) * -3
        self.y += enemy_delta_y - yDelta
        self.x += enemy_delta_x - xDelta

