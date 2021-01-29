from header import *
import bullet
from enemy import enemy
import draw
import player
import purchasable

testing = 0
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
BACKGROUND_WIDTH = 500
BACKGROUND_HEIGHT = 500

FPS: int = 60
FramesPerSecond = pygame.time.Clock()

enemyList = list()
if pygame.init() == 0:
    print("PyGame could not initialize")

logo = pygame.image.load("8bitlink.png")
pause = pygame.transform.scale(pygame.image.load("Pause.png"), (600, 150))
pygame.display.set_icon(logo)
pygame.display.set_caption("# Learn to Code")

if 0:
    pygame.mixer.music.load('bgmusic.wav')
    pygame.mixer.music.play(-1)
    Gunfire = pygame.mixer.Sound('gunfire.wav')
else:
    Gunfire = pygame.mixer.Sound('Silent.wav')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

Goblin = enemy(random.random(), 0, 64, 64, 2, 550, 100)


def hit_logic(person1):
    for enemy_object in enemyList:
        for bullet_object in bullet.bulletList:
            if enemy_object.box_x[0] < bullet_object.locationx < enemy_object.box_x[1]:
                if enemy_object.box_y[0] < bullet_object.locationy < enemy_object.box_y[1]:
                    bullet_object.locationx = -6000
                    enemy_object.health -= bullet_object.damage
                    if enemy_object.health < 1:
                        global money
                        money += enemy_object.health_total/10
                        enemyList.remove(enemy_object)
                        global score  # uses global varriable score inside the function
                        score = score + 5  # increases score by 5 for every kill
        player_to_enemy_distance_tuple = (person1.player_center[0] - enemy_object.center[0], person1.player_center[1] - enemy_object.center[1])
        p_to_e_distance = player_to_enemy_distance_tuple[0] * player_to_enemy_distance_tuple[0] + \
            player_to_enemy_distance_tuple[1] * player_to_enemy_distance_tuple[1]
        p_to_e_distance = math.sqrt(p_to_e_distance)
        if testing == 0:
            if p_to_e_distance < 25:
                return False
    return True


font = pygame.font.SysFont('comicsans', 30, True, True)  # Initializes Font

background = pygame.transform.scale(pygame.image.load("Stone Walls\stone_wall_1_small.png"), (BACKGROUND_HEIGHT, BACKGROUND_WIDTH))

def set_background():
    rand_num: int = int(random.random() * 10)
    if rand_num < 5:
        background = pygame.image.load("backgrounddetailed1_flower.png")
    else:
        background = pygame.image.load("backgrounddetailed1.png")


def runPauseMenu():
    pauseMenu: bool = True
    fontSize: int = 200
    pauseFont = pygame.font.SysFont('comicsans', fontSize, True, True)
    money_text = font.render("Money: $" + str("%.2f" % money), True, (0, 0, 0))
    while pauseMenu == True:
        screen.blit(pause, (screen.get_width()/2 -300, screen.get_height()/2 - 75))
        #mouse_position = pygame.mouse.get_pos()
        #mouse_x = int(mouse_position[0] / 25)
        #mouse_x *= 25
        #mouse_y = int(mouse_position[1] / 25)
        #mouse_y *= 25
        #screen.blit(purchasable.wooden_wall_1, (mouse_x, mouse_y))
        # screen.blit(pauseFont.render("Pause", True, (0, 0, 0)),
                    # (screen.get_width() / 2 - fontSize, screen.get_height() / 2 - fontSize / 2))

        for py_event in pygame.event.get():
            if py_event.type == QUIT:
                running = False
                game_quit = True
                pygame.quit()
            if py_event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseMenu = False
            elif event.type == VIDEORESIZE or VIDEOEXPOSE:
                player_one.position_x = screen.get_width() / 2
                player_one.position_y = screen.get_height() / 2
        pygame.display.update()
        FramesPerSecond.tick(FPS)
        draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, screen.get_width(),
                             screen.get_height())


game_quit: bool = True
mainMenu: bool = True

###############################################################################
# THIS IS WHERE THE MAIN MENU LOOP STARTS
###############################################################################
buttonWidth: int = 250
buttonHeight: int = 65
mmBackground = pygame.transform.scale(pygame.image.load("mainMenu\mmBackground.png"), (800, 720))
button_play = pygame.transform.scale(pygame.image.load("mainMenu\\button_play.png"), (buttonWidth, buttonHeight))
button_play_hovered = pygame.transform.scale(pygame.image.load("mainMenu\\button_play_hovered.png"), (buttonWidth, buttonHeight))
box_button_play = button_play.get_rect(topleft = (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - 50))
button_shop = pygame.transform.scale(pygame.image.load("mainMenu\\button_shop.png"), (buttonWidth, buttonHeight))
button_shop_hovered = pygame.transform.scale(pygame.image.load("mainMenu\\button_shop_hovered.png"), (buttonWidth, buttonHeight))
box_button_shop = button_play.get_rect(topleft = (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - - 50))
button_quit = pygame.transform.scale(pygame.image.load("mainMenu\\button_quit.png"), (buttonWidth, buttonHeight))
button_quit_hovered = pygame.transform.scale(pygame.image.load("mainMenu\\button_quit_hovered.png"), (buttonWidth, buttonHeight))
box_button_quit = button_play.get_rect(topleft = (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - - 150))
while mainMenu == True:
    screen.blit(mmBackground, (0, 0))
    screen.blit(button_play, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - 50))
    screen.blit(button_shop, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - -50))
    screen.blit(button_quit, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - -150))
    for py_event in pygame.event.get():
       if py_event.type == QUIT:
           running = False
           game_quit = True
           pygame.quit()
    if box_button_play.collidepoint(pygame.mouse.get_pos()):
        screen.blit(button_play_hovered, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - 40))
        if pygame.mouse.get_pressed(3)[0]:
                    running = True
                    mainMenu = False
                    game_quit = False
    elif box_button_shop.collidepoint(pygame.mouse.get_pos()):
        screen.blit(button_shop_hovered, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - - 40))
        if pygame.mouse.get_pressed(3)[0]:
                    None
    elif box_button_options.collidepoint(pygame.mouse.get_pos()):
        screen.blit(button_options_hovered, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - - 120))
        if pygame.mouse.get_pressed(3)[0]:
                    None
    elif box_button_quit.collidepoint(pygame.mouse.get_pos()):
        screen.blit(button_quit_hovered, (screen.get_width()/2 - buttonWidth/2, screen.get_height()/2 - - 200))
        if pygame.mouse.get_pressed(3)[0]:
                    running = False
                    pygame.quit()
    pygame.display.update()
    FramesPerSecond.tick(FPS)

###############################################################################
# END
###############################################################################

while not game_quit:

    # initializing in game variables
    start = float(round(time.time()))
    running: bool = True
    pauseMenu: bool = False
    background_x: int = -BACKGROUND_WIDTH
    background_y: int = -BACKGROUND_HEIGHT
    xDelta: float = 0
    yDelta: float = 0
    extra_enemies: int = 0
    menuRunning: bool = False
    wave: int = -1
    money: float = 0
    score: int = 0
    playerImage = pygame.transform.scale(pygame.image.load("survivor-idle_rifle_0.png"), (57, 40))
    player_one = player.Player(playerImage, screen.get_width(), screen.get_height())
    bullet_damage: int = 75
    bullet_speed: int = 10
    number_of_frames_shown: int = 0

    while running == True:
        number_of_frames_shown += 1
        if len(enemyList) == 0:
            wave += 1
            if wave < 60:
                multiplier = wave * 10
            i: int = 0
            now = float(round(time.time()))
            health = 100 + (now - start) / 2
            while i < extra_enemies:
                around = float(random.random() * 10)
                Goblin = enemy(math.cos(around) * (multiplier * random.random() * (1 + (now - start) / 10) + 700) + screen.get_width() / 2,
                               math.sin(around) * (multiplier * random.random() * (1 + (now - start) / 10) + 700) + screen.get_height() / 2,
                               64,
                               64,
                               2,
                               550,
                               health)
                enemyList.append(Goblin)
                i += 1
            extra_enemies += 1

        mouse = pygame.mouse.get_pos()
        draw.draw(mouse, screen.get_width(), screen.get_height(), screen, enemyList, background, xDelta, yDelta,
                  background_x, background_y, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, player_one)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()

            elif event.type == VIDEORESIZE:
                player_one.position_x = screen.get_width() / 2
                player_one.position_y = screen.get_height() / 2

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(5)[0]:
                    radian = math.atan2((mouse[1] - player_one.position_y), (mouse[0] - player_one.position_x))
                    direct = -1 * math.degrees(radian)
                    buldeltay = math.sin(radian) * 10
                    buldeltax = math.cos(radian) * 10
                    new_bullet = bullet.Bullet(bullet_damage,
                                               direct,
                                               bullet_speed,
                                               player_one.position_x + (math.cos(radian + .45) * 21),
                                               player_one.position_y + (math.sin(radian + .45) * 21),
                                               buldeltax,
                                               buldeltay)
                    bullet.bulletList.append(new_bullet)
                    # Gunfire.play()

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
                    menuRunning = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_a:
                    xDelta += 5
                if event.key == pygame.K_d:
                    xDelta -= 5
                if event.key == pygame.K_w:
                    yDelta += 5
                if event.key == pygame.K_s:
                    yDelta -= 5
        if menuRunning == True:
            runPauseMenu()
            menuRunning = False
#########################################################
#         Handles idle and walking animation
        if xDelta == 0 and yDelta == 0:
            player_one.walking_counter = 0
            if number_of_frames_shown % 3 == 0:
                player_one.idle_counter += 1
                player_one.sprite_to_show_while_idle()

        else:
            player_one.idle_counter = 0
            if number_of_frames_shown % 3 == 0:
                player_one.walking_counter += 1
                player_one.sprite_to_show_while_walking()
#############################################################################################
#       Not Currently used. If there are limits width and height then this will come into play
        if player_one.position_x < 0:
            player_one.position_x = 0
        if player_one.position_x > screen.get_width() - playerImage.get_size()[0]:
            player_one.position_x = screen.get_width() - playerImage.get_size()[0]
        if player_one.position_y < 0:
            player_one.position_y = 0
        if player_one.position_y > screen.get_height() - playerImage.get_size()[1]:
            player_one.position_y = screen.get_height() - playerImage.get_size()[1]
##############################################################################################

        background_x -= xDelta
        background_y -= yDelta
        player_one.overall_position_x += xDelta
        player_one.overall_position_y -= yDelta
        if background_x >= 0:
            background_x = -BACKGROUND_WIDTH
        if background_y >= 0:
            background_y = -BACKGROUND_HEIGHT

        running = hit_logic(player_one)

        draw.draw_useful_information(screen, font, score, wave, money, player_one)

        pygame.display.update()
        FramesPerSecond.tick(FPS)

    ###############################################################################
    # THIS IS WHERE THE GAME OVER LOOP STARTS
    ###############################################################################
    #Obsolete{
    enemyList.clear()
    bullet.bulletList.clear()
    extra_enemies = 0
    game_over: bool = True
    fontSize: int = 100
    fontSize2: int = 50
    fontSize3: int = 30
    gameOverFont = pygame.font.SysFont('comicsans', fontSize, True, True)
    gameOverFont2 = pygame.font.SysFont('comicsans', fontSize2, True, True)
    gameOverFont3 = pygame.font.SysFont('comicsans', fontSize3, True, True)

    yes_tuple = (263, 343, 55, 30)
    no_tuple = (487, 343, 55, 30)
    grey = (90, 90, 90)
    white = (255, 255, 255)
    #}
    while game_over:
        goButtonWidth: int = 200
        goButtonHeight: int = 45
        img_skull = pygame.transform.scale(pygame.image.load("gameOver\skull.png"), (100, 82))
        img_gameOver = pygame.transform.scale(pygame.image.load("gameOver\gameover.png"), (400, 229))
        button_retry = pygame.transform.scale(pygame.image.load("gameOver\\button_retry.png"), (goButtonWidth, goButtonHeight))
        button_retry_hovered = pygame.transform.scale(pygame.image.load("gameOver\\button_retry_hovered.png"), (goButtonWidth, goButtonHeight))
        box_button_retry = button_play.get_rect(topleft = (screen.get_width()/2 - goButtonWidth/2 - 200, screen.get_height()/2 - -200))
        button_quit2 = pygame.transform.scale(pygame.image.load("gameOver\\button_quit2.png"), (goButtonWidth, goButtonHeight))
        button_quit2_hovered = pygame.transform.scale(pygame.image.load("gameOver\\button_quit2_hovered.png"), (goButtonWidth, goButtonHeight))
        box_button_quit2 = button_quit.get_rect(topleft = (screen.get_width()/2 - goButtonWidth/2 - - 200, screen.get_height()/2 - -200))
        
        screen.fill([0, 0, 0])
        screen.blit(img_skull, (screen.get_width()/2 - 100/2, screen.get_height()/2 - 82/2 - 200))
        screen.blit(img_gameOver, (screen.get_width()/2 - 400/2, screen.get_height()/2 - 229/2))
        screen.blit(button_retry, (screen.get_width()/2 - goButtonWidth/2 - 200, screen.get_height()/2 - -200))
        screen.blit(button_quit2, (screen.get_width()/2 - goButtonWidth/2 - - 200, screen.get_height()/2 - -200))
        for py_event in pygame.event.get():
           if py_event.type == QUIT:
               game_over = False
               game_quit = True
               pygame.quit()
        if box_button_retry.collidepoint(pygame.mouse.get_pos()):
            screen.blit(button_retry_hovered, (screen.get_width()/2 - goButtonWidth/2 - 200, screen.get_height()/2 - - 200))
            if pygame.mouse.get_pressed(3)[0]:
                        game_over = False
                        player_one.overall_position_x = 0
                        player_one.overall_position_y = 0
        elif box_button_quit2.collidepoint(pygame.mouse.get_pos()):
            screen.blit(button_quit2_hovered, (screen.get_width()/2 - goButtonWidth/2 - - 200, screen.get_height()/2 - - 200))
            if pygame.mouse.get_pressed(3)[0]:
                        game_over = False
                        game_quit = True
        pygame.display.update()
        FramesPerSecond.tick(FPS)


