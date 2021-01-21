import header
from header import *


class Player:

    def __init__(self, sprite, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.playerImage = sprite
        self.image_copy = sprite
        self.direction = 0
        self.position_x = SCREEN_WIDTH/2
        self.position_y = SCREEN_HEIGHT/2
        self.health = 100
        self.speed = 5
        self.overall_position_x = 0
        self.overall_position_y = 0

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
