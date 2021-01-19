from header import *
import bullet
from enemy import enemy
import draw

testing = 1

start = float(round(time.time()))
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60
FramesPerSecond = pygame.time.Clock()

enemyList = list()
if pygame.init() == 0:
    print("PyGame could not initialize")

logo = pygame.image.load("8bitlink.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("# Learn to Code")

background = pygame.image.load("backgrounddetailed1.png")

if testing == 0:
    pygame.mixer.music.load('bgmusic.wav')
    pygame.mixer.music.play(-1)
    Gunfire = pygame.mixer.Sound('gunfire.wav')
else:
    Gunfire = pygame.mixer.Sound('Silent.wav')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

playerImage = pygame.image.load("really tiny soldier.png")

bullet_damage: int = 100
bullet_speed: int = 10

Goblin = enemy(random.random(), 0, 64, 64, 2, 550, 100)
score = 0

def hit_logic():
    for bullet_object in bullet.bulletList:
        for enemy_object in enemyList:
            if enemy_object.x < bullet_object.locationx < enemy_object.x + enemy_object.width:
                if enemy_object.y < bullet_object.locationy < enemy_object.y + enemy_object.width:
                    bullet_object.locationx = -6
                    enemy_object.health -= bullet_object.damage
                    global score #uses global varriable score inside the function
                    score = score+5 #increases score by 5 for every hit



font = pygame.font.SysFont('comicsans', 30, True, True) # Initializes Font

background_x: int = -500
background_y: int = -500
player_x = 400
player_y = 300
xDelta = 0
yDelta = 0
extra_enemies: int = 0
running = True

while running:
    screen.fill((0, 0, 0))

    if len(enemyList) == 0:
        i: int = 0
        now = float(round(time.time()))
        while i < extra_enemies:
            around = float(random.random() * 10)
            Goblin = enemy(math.cos(around) * 500 + SCREEN_WIDTH / 2, math.sin(around) * 500 + SCREEN_HEIGHT / 2, 64,
                           64, 2, 550,
                           100 + (now - start) / 10)
            enemyList.append(Goblin)
            i += 1
        extra_enemies += 1

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == VIDEORESIZE:
            SCREEN_WIDTH = screen.get_width()
            SCREEN_HEIGHT = screen.get_height()
            player_x = SCREEN_WIDTH / 2
            player_y = SCREEN_HEIGHT / 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            radian = math.atan2((mouse[1] - player_y), (mouse[0] - player_x))
            direct = -1 * math.degrees(radian)
            buldeltay = math.sin(radian) * 10
            buldeltax = math.cos(radian) * 10
            new_bullet = bullet.Bullet(bullet_damage, direct, bullet_speed, player_x + (math.cos(radian + .45) * 21),
                                       player_y + (math.sin(radian + .45) * 21), buldeltax, buldeltay)
            bullet.bulletList.append(new_bullet)
            Gunfire.play()

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

    background_x -= xDelta
    background_y -= yDelta
    if background_x >= 0:
        background_x = -500
    if background_y >= 0:
        background_y = -500
    draw.draw(mouse, player_x, player_y, playerImage, SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemyList, background,
              xDelta, yDelta, background_x, background_y)
    hit_logic()
    scoretxt = font.render("Score: " + str(score),True,(0,0,0))
    screen.blit(scoretxt,(0,0))
    pygame.display.update()
    FramesPerSecond.tick(FPS)
