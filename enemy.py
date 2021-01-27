from header import *


class enemy:

    def __init__(self, x, y, width, height, vel, end, health):
        self.static = pygame.transform.scale(pygame.image.load('Eliteknightshotgun.png'), (64, 64))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box_y = (self.y - self.height/2, self.y + self.height/2)
        self.box_x = (self.x - self.width/2, self.x + self.width/2)
        self.damage = 25
        self.end = end
        self.path = [self.x, self.end]
        # self.count = 0# for animation later
        self.velocity = vel
        self.hitbox = (self.x + 30, self.y + 30, 40, 90)
        self.health = health
        self.health_total = health
        self.center = (self.x - self.width/2, self.y - self.height/2)
        self.frame_counter: int = 0
        self.frame_at_last_hit: int = 0

    def draw_pause(self, screen):
        screen.blit(self.static, self.center)
        
    def draw(self, screen, player_x, player_y, xDelta, yDelta):
        self.move(player_x, player_y, xDelta, yDelta)
        if self.velocity > 0:
            self.center =  (self.x - self.width/2, self.y-self.height/2)
            screen.blit(self.static, self.center)
        self.hitbox = (self.x + 30, self.y + 30, 40, 90)
        pygame.draw.rect(screen, (255, 0, 0), (self.x - self.width/2, self.y - self.height/2, 50, 10))
        pygame.draw.rect(screen, (0, 128, 0), (self.x - self.width/2, self.y - self.height/2, 50 * self.health/self.health_total, 10))
        #pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)  # drawing hitbox right now

    def move(self, player_x, player_y, xDelta, yDelta):
        radian = math.atan2((self.y - player_y), (self.x - player_x))
        enemy_delta_y = math.sin(radian) * -3
        enemy_delta_x = math.cos(radian) * -3
        self.y += enemy_delta_y - yDelta
        self.x += enemy_delta_x - xDelta
        self.box_y = (self.y - self.height/2, self.y + self.height/2)
        self.box_x = (self.x - self.width/2, self.x + self.width/2)

#
