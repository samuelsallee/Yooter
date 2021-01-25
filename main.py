from header import *
import bullet
from enemy import enemy
import draw
import player
import purchasable

testing = 0
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

# background = pygame.image.load("backgrounddetailed1_flower.png")
background = pygame.image.load("backgrounddetailed1.png")


def set_background():
    rand_num: int = int(random.random() * 10)
    if rand_num < 5:
        background = pygame.image.load("backgrounddetailed1_flower.png")
    else:
        background = pygame.image.load("backgrounddetailed1.png")


def runPauseMenu():
    pauseMenuOff: bool = False
    fontSize: int = 200
    pauseFont = pygame.font.SysFont('comicsans', fontSize, True, True)
    money_text = font.render("Money: $" + str("%.2f" % money), True, (0, 0, 0))
    while pauseMenuOff == False:
        mouse_position = pygame.mouse.get_pos()
        mouse_x = int(mouse_position[0] / 25)
        mouse_x *= 25
        mouse_y = int(mouse_position[1] / 25)
        mouse_y *= 25
        screen.blit(purchasable.wooden_wall_1, (mouse_x, mouse_y))
        # screen.blit(pauseFont.render("Pause", True, (0, 0, 0)),
                    # (screen.get_width() / 2 - fontSize, screen.get_height() / 2 - fontSize / 2))

        for py_event in pygame.event.get():
            if py_event.type == QUIT:
                running = False
                game_quit = True
                pygame.quit()
            if py_event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseMenuOff = True
            elif event.type == VIDEORESIZE:
                player_one.position_x = screen.get_width() / 2
                player_one.position_y = screen.get_height() / 2
        pygame.display.update()
        FramesPerSecond.tick(FPS)
        draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, screen.get_width(),
                             screen.get_height())


game_quit: bool = False

while not game_quit:

    # initializing in game variables
    start = float(round(time.time()))
    running: bool = True
    background_x: int = -500
    background_y: int = -500
    xDelta: float = 0
    yDelta: float = 0
    extra_enemies: int = 0
    pauseMenu: bool = False
    wave: int = -1
    money: float = 0
    score: int = 0
    playerImage = pygame.transform.scale(pygame.image.load("survivor-idle_rifle_0.png"), (57, 40))
    player_one = player.Player(playerImage, screen.get_width(), screen.get_height())
    bullet_damage: int = 75
    bullet_speed: int = 10
    number_of_frames_shown: int = 0

    while running:
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
                  background_x, background_y, player_one)

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
        if pauseMenu:
            runPauseMenu()
            pauseMenu = False
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
            background_x = -500
        if background_y >= 0:
            background_y = -500

        running = hit_logic(player_one)

        draw.draw_useful_information(screen, font, score, wave, money, player_one)

        pygame.display.update()
        FramesPerSecond.tick(FPS)

    ###############################################################################
    # THIS IS WHERE THE GAME OVER LOOP STARTS
    ###############################################################################

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
    while game_over:

        mouse = pygame.mouse.get_pos()

        if yes_tuple[0] < mouse[0] < yes_tuple[0] + yes_tuple[2]:
            if yes_tuple[1] < mouse[1] < yes_tuple[1] + yes_tuple[3]:
                draw.draw_game_over_screen(screen, yes_tuple, no_tuple, gameOverFont, gameOverFont2, gameOverFont3, white, grey)
        elif no_tuple[0] < mouse[0] < no_tuple[0] + no_tuple[2]:
            if no_tuple[1] < mouse[1] < no_tuple[1] + no_tuple[3]:
                draw.draw_game_over_screen(screen, yes_tuple, no_tuple, gameOverFont, gameOverFont2, gameOverFont3, grey, white)
        else:
            draw.draw_game_over_screen(screen, yes_tuple, no_tuple, gameOverFont, gameOverFont2, gameOverFont3, grey, grey)
        pygame.display.update()
        FramesPerSecond.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = False
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    if yes_tuple[0] < mouse[0] < yes_tuple[0] + yes_tuple[2]:
                        if yes_tuple[1] < mouse[1] < yes_tuple[1] + yes_tuple[3]:
                            game_over = False
                            player_one.overall_position_x = 0
                            player_one.overall_position_y = 0
                    elif no_tuple[0] < mouse[0] < no_tuple[0] + no_tuple[2]:
                        if no_tuple[1] < mouse[1] < no_tuple[1] + no_tuple[3]:
                            game_over = False
                            game_quit = True
