import header
from header import *


class Player:

    def __init__(self, sprite, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.playerImage = sprite
        self.image_copy = sprite
        self.direction: int = 0
        self.position_x: int = SCREEN_WIDTH/2
        self.position_y: int = SCREEN_HEIGHT/2
        self.health: float = 100
        self.speed: int = 5
        self.overall_position_x: int = 0
        self.overall_position_y: int = 0

    def set_health(self, speed):
        self.speed = speed

    def set_health(self, health):
        self.health = health

    def set_direction(self, direction):
        self.direction = direction

    def set_position(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def move(self, change_in_x, change_in_y):
        self.overall_position_x += change_in_x
        self.overall_position_y += change_in_y

    def draw_player(self, angle, screen):
        rot_radian = math.atan2((angle[1] - self.position_y), (angle[0] - self.position_x))
        dy = -1 * math.degrees(rot_radian)
        self.image_copy = pygame.transform.rotate(self.playerImage, dy)
        screen.blit(self.image_copy, (self.position_x-int(self.image_copy.get_width()/2), self.position_y-int(self.image_copy.get_height()/2)))