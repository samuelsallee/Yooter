from header import *
import bullet
from enemy import enemy

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60
FramesPerSecond = pygame.time.Clock()

if pygame.init() == 0:
    print("PyGame could not initialize")

logo = pygame.image.load("8bitlink.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("# Learn to Code")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerImage = pygame.image.load("really tiny soldier.png")


def player(angle, x, y):
    rot_radian = math.atan2((angle[1] - y), (angle[0] - x))
    dy = -1 * math.degrees(rot_radian)
    player_copy = pygame.transform.rotate(playerImage, dy)
    screen.blit(player_copy, (x-int(player_copy.get_width()/2), y-int(player_copy.get_height()/2)))


def draw_bullet():
    for bullet_object in bullet.bulletList:
        if bullet_object.locationx > SCREEN_WIDTH or bullet_object.locationx < 0 or bullet_object.locationy > SCREEN_HEIGHT or bullet_object.locationy < 0:
            bullet.bulletList.remove(bullet_object)
        else:
            bullet_copy = pygame.transform.rotate(bullet_object.image, bullet_object.direction)
            screen.blit(bullet_copy, (bullet_object.locationx - int(bullet_copy.get_width()/2) + bullet_object.changex, int(bullet_object.locationy - bullet_copy.get_height()/2) + bullet_object.changey))
            bullet_object.set_location(bullet_object.locationx + bullet_object.changex, bullet_object.locationy + bullet_object.changey)



player_x = 400
player_y = 300
xDelta = 0
yDelta = 0
Goblin = enemy(10, 10, 8, 8, 2, 550) #initalize enemy
running = True

while running:
    screen.fill((0, 0, 0))
    Goblin.draw(screen) #draw the enmy on the screen
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            radian = math.atan2((mouse[1] - player_y), (mouse[0] - player_x))
            direct = -1 * math.degrees(radian)
            buldeltay = math.sin(radian) * 10
            buldeltax = math.cos(radian) * 10
            new_bullet = bullet.Bullet(40, direct, 10, player_x, player_y, buldeltax, buldeltay)
            bullet.bulletList.append(new_bullet)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                xDelta -= 5
            if event.key == pygame.K_d:
                xDelta += 5
            if event.key == pygame.K_w:
                yDelta -= 5
            if event.key == pygame.K_s:
                yDelta += 5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                xDelta += 5
            if event.key == pygame.K_d:
                xDelta -= 5
            if event.key == pygame.K_w:
                yDelta += 5
            if event.key == pygame.K_s:
                yDelta -= 5
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - playerImage.get_size()[0]:
        player_x = SCREEN_WIDTH - playerImage.get_size()[0]
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - playerImage.get_size()[1]:
        player_y = SCREEN_HEIGHT - playerImage.get_size()[1]
    player_x += xDelta
    player_y += yDelta

    player(mouse, player_x, player_y)
    draw_bullet()
    pygame.display.update()
    FramesPerSecond.tick(FPS)
