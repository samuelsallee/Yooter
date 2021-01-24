import header
from header import*


class Bullet:

    image = pygame.transform.scale(pygame.image.load("Transparent bullet.png"), (30, 20))

    def __init__(self, dam, direct, spd, locx, locy, chx, chy):
        self.damage = dam
        self.direction = direct
        self.speed = spd
        self.locationx = locx
        self.locationy = locy
        self.changex = chx
        self.changey = chy

    def set_location(self, locx, locy):
        self.locationx = locx
        self.locationy = locy


bulletList = list()
