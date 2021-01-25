from header import*
import bullet
import enemy
import menu

def draw_player(angle, player_object, screen):
    player_object.draw_player(angle, screen)


def draw_bullet(SCREEN_WIDTH, SCREEN_HEIGHT, screen, xDelta, yDelta):
    for bullet_object in bullet.bulletList:
        bullet_object.changex -= xDelta
        bullet_object.changey -= yDelta
        if bullet_object.locationx > SCREEN_WIDTH or bullet_object.locationx < 0 or bullet_object.locationy >\
                SCREEN_HEIGHT or bullet_object.locationy < 0:
            bullet.bulletList.remove(bullet_object)
        else:
            bullet_copy = pygame.transform.rotate(bullet_object.image, bullet_object.direction)
            screen.blit(bullet_copy, (bullet_object.locationx - int(bullet_copy.get_width()/2) + bullet_object.changex,
                                      int(bullet_object.locationy - bullet_copy.get_height()/2) +
                                      bullet_object.changey))
            bullet_object.set_location(bullet_object.locationx + bullet_object.changex, bullet_object.locationy +
                                       bullet_object.changey)
        bullet_object.changex += xDelta
        bullet_object.changey += yDelta


def draw_enemy(enemyList, screen, player_x, player_y, xDelta, yDelta):
    for enemy_object in enemyList:
        enemy_object.draw(screen, player_x, player_y, xDelta, yDelta)


def draw(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemyList, background, xDelta, yDelta, background_x, background_y, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, player):
    i = background_x
    i2 = background_y
    while i <= SCREEN_WIDTH:
        while i2 <= SCREEN_HEIGHT:
            screen.blit(background, (i, i2))
            i2 += BACKGROUND_HEIGHT
        i2 = background_y
        i += BACKGROUND_WIDTH
    draw_player(mouse, player, screen)
    draw_bullet(SCREEN_WIDTH, SCREEN_HEIGHT, screen, xDelta, yDelta)
    draw_enemy(enemyList, screen, player.position_x, player.position_y, xDelta, yDelta)
    



def draw_pause_menu(screen, enemyList, background_x, background_y, background, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT):
    i = background_x
    i2 = background_y
    while i <= SCREEN_WIDTH:
        while i2 <= SCREEN_HEIGHT:
            screen.blit(background, (i, i2))
            i2 += BACKGROUND_HEIGHT
        i2 = background_y
        i += BACKGROUND_WIDTH
    #menu.loopMenu(screen, enemyList, background_x, background_y, background)
    for enemy_object in enemyList:
        enemy_object.draw_pause(screen)
    for bullet_object in bullet.bulletList:
        bullet_copy = pygame.transform.rotate(bullet_object.image, bullet_object.direction)
        screen.blit(bullet_copy, (bullet_object.locationx, bullet_object.locationy))


def draw_game_over_screen(screen, yes_tuple, no_tuple, gameOverFont, gameOverFont2, gameOverFont3, color1, color2):
    screen.fill([255, 0, 0])
    pygame.draw.rect(screen, color1, yes_tuple)
    pygame.draw.rect(screen, color2, no_tuple)
    screen.blit(gameOverFont.render("GAME OVER NERD", True, (0, 0, 0)), (50, 100))
    screen.blit(gameOverFont2.render("YOU SUCK SHIT", True, (0, 0, 0)), (250, 220))
    screen.blit(gameOverFont3.render("Would you like to try again?", True, (0, 0, 0)), (240, 300))
    screen.blit(gameOverFont3.render("Yes", True, (0, 0, 0)), (270, 350))
    screen.blit(gameOverFont3.render("No", True, (0, 0, 0)), (500, 350))


def draw_useful_information(screen, font, score, wave, money, player_one):
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    wave_text = font.render("Wave: " + str(wave), True, (0, 0, 0))
    money_text = font.render("Money: $" + str("%.2f" % money), True, (0, 0, 0))
    overall_position_text = font.render(str(player_one.overall_position_x) + ", " + str(player_one.overall_position_y),
                                        True, (0, 0, 0))
    screen.blit(score_text, (2, 2))
    screen.blit(wave_text, (screen.get_width() - 130, 2))
    screen.blit(money_text, (2, 32))
    screen.blit(overall_position_text, (screen.get_width() / 2 - 50, 2))

