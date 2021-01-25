import header
from header import*


class things_to_buy:
    def __init__(self):
        self.cost: float = 0


class placeable(things_to_buy):
    def __init__(self, player):
        self.x: int = 0
        self.y: int = 0
        self.overall_x: int = 0
        self.overall_y: int = 0

    def place(self, player, x, y):
        self.overall_x = player.overall_position_x + x - player.position_x
        self.overall_y = player.overall_position_y - y - player.position_y


class wall(placeable):
    def __init__(self, health, image):
        self.health: int = health
        self.image = image


class turret(placeable):
    def __init__(self, image):
        self.image = image


wooden_wall_1 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_1.png"),(25, 25))
wooden_wall_2 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_2.png"),(25, 25))
wooden_wall_3 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_3.png"),(25, 25))
wooden_wall_4 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_4.png"),(25, 50))
wooden_wall_5 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_5.png"),(25, 50))
wooden_wall_6 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_6.png"),(25, 50))
wooden_wall_7 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_7.png"),(50, 25))
wooden_wall_8 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_8.png"),(50, 25))
wooden_wall_9 = pygame.transform.scale(pygame.image.load("Wooden walls\Wooden_wall_9.png"),(50, 25))

stone_wall_1 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_1.png"),(25, 25))
stone_wall_2 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_2.png"),(25, 25))
stone_wall_3 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_3.png"),(25, 25))
stone_wall_4 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_4.png"),(25, 25))
stone_wall_5 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_5.png"),(25, 25))
stone_wall_6 = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_6.png"),(25, 25))

weak_wall = wall(300, wooden_wall_1)
reinforced_wall = wall(500, wooden_wall_3)
extra_reinforced_wall = wall(800, wooden_wall_2)
double_weak_wall_vertical = wall(600, wooden_wall_5)
double_reinforced_wall_vertical = wall(1000, wooden_wall_6)
double_extra_reinforced_wall_vertical = wall(1600, wooden_wall_4)
double_weak_wall_horizontal = wall(600, wooden_wall_8)
double_reinforced_wall_horizontal = wall(1000, wooden_wall_7)
double_extra_reinforced_wall_horizontal = wall(1600, wooden_wall_9)
stone_wall = wall(4000, stone_wall_2)

weak_wall.cost = 300
reinforced_wall.cost = 600
extra_reinforced_wall.cost = 1000
double_weak_wall_vertical.cost = 550
double_reinforced_wall_vertical = 1100
double_extra_reinforced_wall_vertical = 1800
double_weak_wall_horizontal = 550
double_reinforced_wall_horizontal = 1100
double_extra_reinforced_wall_horizontal = 1800

pistol_image = pygame.image.load("vippng.com-kalashnikov-png-1903984.png")
rifle_image = pygame.image.load("vippng.com-ak-47-png-1145009.png")
shotgun_image = pygame.image.load("vippng.com-sawed-off-shotgun-png-3257780.png")


wall_list = list()
