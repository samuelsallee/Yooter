from header import *
import bullet
from enemy import enemy
import draw
import player

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


if testing == 0:
    pygame.mixer.music.load('bgmusic.wav')
    pygame.mixer.music.play(-1)
    Gunfire = pygame.mixer.Sound('gunfire.wav')
else:
    Gunfire = pygame.mixer.Sound('Silent.wav')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

playerImage = pygame.image.load("really tiny soldier.png")
player_one = player.Player(playerImage, SCREEN_WIDTH, SCREEN_HEIGHT)

bullet_damage: int = 100
bullet_speed: int = 10

Goblin = enemy(random.random(), 0, 64, 64, 2, 550, 100)
score = 0



def hit_logic():
    for bullet_object in bullet.bulletList:
        for enemy_object in enemyList:
            if enemy_object.x < bullet_object.locationx < enemy_object.x + enemy_object.width:
                if enemy_object.y < bullet_object.locationy < enemy_object.y + enemy_object.width:
                    bullet_object.locationx = -6000
                    enemy_object.health -= bullet_object.damage
                    if enemy_object.health < 1:
                        enemyList.remove(enemy_object)
                        global score #uses global varriable score inside the function
                        score = score+5 #increases score by 5 for every kill


font = pygame.font.SysFont('comicsans', 30, True, True) # Initializes Font

background_x: int = -500
background_y: int = -500
xDelta: float = 0
yDelta: float = 0
extra_enemies: int = 0
running: bool = True
pauseMenu: bool = False

#background = pygame.image.load("backgrounddetailed1_flower.png")
background = pygame.image.load("backgrounddetailed1.png")

def setBackground():
    randNum: int = int(random.random()*10)
    if randNum < 5:
        background = pygame.image.load("backgrounddetailed1_flower.png")
    else:
        background = pygame.image.load("backgrounddetailed1.png")

def runPauseMenu():
    pauseMenuOff: bool = False
    while pauseMenuOff == False:
        fontSize: int = 200
        pauseFont = pygame.font.SysFont('comicsans', fontSize, True, True)
        screen.blit(pauseFont.render("Pause", True, (0, 0, 0)), (SCREEN_WIDTH/2-fontSize, SCREEN_HEIGHT/2-fontSize/2))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseMenuOff = True
        pygame.display.update()
        FramesPerSecond.tick(FPS)
        draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, SCREEN_WIDTH, SCREEN_HEIGHT)


while running:

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
    draw.draw(mouse, player_one.position_x, player_one.position_y, player_one.playerImage, SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemyList, background, xDelta, yDelta, background_x, background_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()

        elif event.type == VIDEORESIZE:
            SCREEN_WIDTH = screen.get_width()
            SCREEN_HEIGHT = screen.get_height()
            player_one.position_x = SCREEN_WIDTH / 2
            player__one.position_y = SCREEN_HEIGHT / 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            radian = math.atan2((mouse[1] - player_one.position_y), (mouse[0] - player_one.position_x))
            direct = -1 * math.degrees(radian)
            buldeltay = math.sin(radian) * 10
            buldeltax = math.cos(radian) * 10
            new_bullet = bullet.Bullet(bullet_damage, direct, bullet_speed, player_one.position_x + (math.cos(radian + .45) * 21),
                                       player_one.position_y + (math.sin(radian + .45) * 21), buldeltax, buldeltay)
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
            if event.key == pygame.K_ESCAPE:
                pauseMenu = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                xDelta += 5
            if event.key == pygame.K_d:
                xDelta -= 5
            if event.key == pygame.K_w:
                yDelta += 5
            if event.key == pygame.K_s:
                yDelta -= 5
    if pauseMenu == True:
        runPauseMenu()
        pauseMenu = False
    if player_one.position_x < 0:
        player_one.position_x = 0
    if player_one.position_x > SCREEN_WIDTH - playerImage.get_size()[0]:
        player_one.position_x = SCREEN_WIDTH - playerImage.get_size()[0]
    if player_one.position_y < 0:
        player_one.position_y = 0
    if player_one.position_y > SCREEN_HEIGHT - playerImage.get_size()[1]:
        player_one.position_y = SCREEN_HEIGHT - playerImage.get_size()[1]

    background_x -= xDelta
    background_y -= yDelta
    if background_x >= 0:
        background_x = -500
    if background_y >= 0:
        background_y = -500
    hit_logic()
    scoretxt = font.render("Score: " + str(score),True,(0,0,0))
    screen.blit(scoretxt,(0,0))
    pygame.display.update()
    FramesPerSecond.tick(FPS)

        
