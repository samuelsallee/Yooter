import Header
from Header import*

bulletList = list()


class Bullet:
    damage: int = 0
    direction = 0
    speed = 0
    location = (0, 0)
    image = pygame.image.load("Transparent bullet.png")

    def __init__(self, dam, direct, spd, loc):
        damage = dam
        direction = direct
        speed = spd
        location = loc

    def set_damage(self, dam: int):
        damage = dam

    def set_direction(self, direct: int):
        direction = direct

    def set_speed(self, sp: int):
        speed = sp

    def set_location(self, loc):
        location = loc

    def get_damage(self,):
        return damage

    def get_direction(self,):
        return direction

    def get_speed(self,):
        return speed

    def get_location(self,):
        return location
