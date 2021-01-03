import Header
from Header import*


class Bullet:

    image = pygame.transform.scale(pygame.image.load("Transparent bullet.png"),(30,20))

    def __init__(self, dam, direct, spd, locx, locy, chx, chy):
        self.damage = dam
        self.direction = direct
        self.speed = spd
        self.locationx = locx
        self.locationy = locy
        self.changex = chx
        self.changey = chy

    def set_damage(self, dam: int):
        self.damage = dam

    def set_direction(self, direct: int):
        direction = direct

    def set_speed(self, sp: int):
        speed = sp

    def set_location(self, locx, locy):
        self.locationx = locx
        self.locationy = locy

    def get_damage(self,):
        return self.damage

    def get_direction(self,):
        return self.direction

    def get_speed(self,):
        return self.speed

    def get_locationx(self,):
        return self.locationx


bullet1 = Bullet(0, 0, 0, 0, 0, 0, 0)
bullet2 = Bullet(0, 0, 0, 0, 0, 0, 0)
bulletList = list((bullet1, bullet2))
bulletList.pop()
bulletList.pop()
