import Header
from Header import*
import bullet



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
pygame.transform.rotate(playerImage, 200)

player_x: int = 400
player_y: int = 300

xDelta: int = 0
yDelta: int = 0


def player(angle, x, y):
    radian = math.atan2((angle[1] - y), (angle[0] - x))
    dy = -1 * math.degrees(radian)
    screen.blit(pygame.transform.rotate(playerImage, dy), (x , y))


def draw_bullet():
    for bullet_object in bullet.bulletList:
        screen.blit(pygame.transform.rotate(bullet_object.image, bullet_object.direction), (bullet_object.location[0], bullet_object.location[1]))


running = True

while running:
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        #if event.type == pygame.mouse.get_pressed():


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                xDelta -= 5
            if event.key == pygame.K_d:
                xDelta += 5
            if event.key == pygame.K_w:
                yDelta -= 5
            if event.key == pygame.K_s:
                yDelta += 5
            if event.key == pygame.K_SPACE:
                radian = math.atan2((mouse[1] - player_y), (mouse[0] - player_x))
                direct = -1 * math.degrees(radian)
                new_bullet = bullet.Bullet(40, direct, 10, (player_x, player_y))
                bullet.bulletList.append(new_bullet)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                xDelta += 5
            if event.key == pygame.K_d:
                xDelta -= 5
            if event.key == pygame.K_w:
                yDelta += 5
            if event.key == pygame.K_s:
                yDelta -= 5

    player_x += xDelta
    player_y += yDelta

    player(mouse, player_x, player_y)
    draw_bullet()
    pygame.display.update()
    FramesPerSecond.tick(FPS)

