import header
from header import *


class Player:

    def __init__(self, sprite, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.player_size = (57, 40)  # changing this will fuck up a bunch of things
        self.playerImage = sprite
        self.image_copy = sprite
        self.direction: int = 0
        self.position_x: int = SCREEN_WIDTH/2
        self.position_y: int = SCREEN_HEIGHT/2
        self.health: float = 100
        self.speed: int = 5
        self.overall_position_x: int = 0
        self.overall_position_y: int = 0
        self.player_center = (self.position_x-int(self.image_copy.get_width()/2), self.position_y-int(self.image_copy.get_height()/2))
        self.hypo: float = 0
        self.idle = list()
        self.walking = list()
        self.initialize_player_idle_with_handgun()
        self.initialize_player_walking_with_handgun()
        self.idle_counter: int = 0
        self.walking_counter: int = 0

    def set_speed(self, speed):
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
        self.player_center = (self.position_x-int(self.image_copy.get_width()/2), self.position_y-int(self.image_copy.get_height()/2))
        screen.blit(self.image_copy, self.player_center)

    def initialize_player_idle_with_handgun(self):
        self.idle.clear()
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_0.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_1.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_2.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_3.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_4.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_5.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_6.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_7.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_8.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_9.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_10.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_11.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_12.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_13.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_14.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_15.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_16.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_17.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_18.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_player_sprites\survivor-idle_handgun_19.png"), self.player_size))

    def initialize_player_idle_with_rifle(self):
        self.idle.clear()
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_0.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_1.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_2.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_3.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_4.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_5.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_6.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_7.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_8.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_9.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_10.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_11.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_12.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_13.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_14.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_15.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_16.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_17.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_18.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_rifle\survivor-idle_rifle_19.png"), self.player_size))

    def initialize_player_idle_with_shotgun(self):
        self.idle.clear()
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_0.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_1.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_2.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_3.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_4.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_5.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_6.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_7.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_8.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_9.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_10.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_11.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_12.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_13.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_14.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_15.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_16.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_17.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_18.png"), self.player_size))
        self.idle.append(pygame.transform.scale(pygame.image.load("idle_with_shotgun\survivor-idle_shotgun_19.png"), self.player_size))

    def initialize_player_walking_with_handgun(self):
        self.walking.clear()
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_0.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_1.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_2.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_3.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_4.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_5.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_6.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_7.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_8.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_9.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_10.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_11.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_12.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_13.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_14.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_15.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_16.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_17.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_18.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_handgun\survivor-move_handgun_19.png"), self.player_size))

    def initialize_player_walking_with_rifle(self):
        self.walking.clear()
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_0.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_1.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_2.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_3.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_4.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_5.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_6.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_7.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_8.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_9.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_10.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_11.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_12.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_13.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_14.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_15.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_16.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_17.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_18.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_rifle\survivor-move_rifle_19.png"), self.player_size))

    def initialize_player_walking_with_shotgun(self):
        self.walking.clear()
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_0.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_1.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_2.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_3.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_4.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_5.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_6.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_7.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_8.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_9.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_10.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_11.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_12.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_13.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_14.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_15.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_16.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_17.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_18.png"), self.player_size))
        self.walking.append(pygame.transform.scale(pygame.image.load("walking_with_shotgun\survivor-move_shotgun_19.png"), self.player_size))

    def sprite_to_show_while_idle(self):
        self.playerImage = self.idle[self.idle_counter % 20]

    def sprite_to_show_while_walking(self):
        self.playerImage = self.walking[self.walking_counter % 20]
#
