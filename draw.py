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


def draw(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemyList, background, xDelta, yDelta, background_x, background_y, player):
    i = background_x
    i2 = background_y
    while i <= SCREEN_WIDTH:
        while i2 <= SCREEN_HEIGHT:
            screen.blit(background, (i, i2))
            i2 += 500
        i2 = background_y
        i += 500
    draw_player(mouse, player, screen)
    draw_bullet(SCREEN_WIDTH, SCREEN_HEIGHT, screen, xDelta, yDelta)
    draw_enemy(enemyList, screen, player.position_x, player.position_y, xDelta, yDelta)
    



def draw_pause_menu(screen, enemyList, background_x, background_y, background, SCREEN_WIDTH, SCREEN_HEIGHT):
    i = background_x
    i2 = background_y
    while i <= SCREEN_WIDTH:
        while i2 <= SCREEN_HEIGHT:
            screen.blit(background, (i, i2))
            i2 += 500
        i2 = background_y
        i += 500
    #menu.loopMenu(screen, enemyList, background_x, background_y, background)
    for enemy_object in enemyList:
        enemy_object.draw_pause(screen)
    for bullet_object in bullet.bulletList:
        bullet_copy = pygame.transform.rotate(bullet_object.image, bullet_object.direction)
        screen.blit(bullet_copy, (bullet_object.locationx, bullet_object.locationy))

<<<<<<< HEAD
=======

def draw_game_over_screen(screen, yes_tuple, no_tuple, gameOverFont, gameOverFont2, gameOverFont3):
    screen.fill([255, 0, 0])
    pygame.draw.rect(screen, (125, 125, 125), yes_tuple)
    pygame.draw.rect(screen, (125, 125, 125), no_tuple)
    screen.blit(gameOverFont.render("GAME OVER NERD", True, (0, 0, 0)), (50, 100))
    screen.blit(gameOverFont2.render("YOU SUCK SHIT", True, (0, 0, 0)), (250, 220))
    screen.blit(gameOverFont3.render("Would you like to try again?", True, (0, 0, 0)), (240, 300))
    screen.blit(gameOverFont3.render("Yes", True, (0, 0, 0)), (270, 350))
    screen.blit(gameOverFont3.render("No", True, (0, 0, 0)), (500, 350))
>>>>>>> 2bcdfd3b6c90466e09b8379f97136b7d0aed835a
