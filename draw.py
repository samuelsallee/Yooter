from header import*
import bullet
import enemy

def draw_player(angle, x, y, playerImage, screen):
    rot_radian = math.atan2((angle[1] - y), (angle[0] - x))
    dy = -1 * math.degrees(rot_radian)
    player_copy = pygame.transform.rotate(playerImage, dy)
    screen.blit(player_copy, (x-int(player_copy.get_width()/2), y-int(player_copy.get_height()/2)))


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
        if enemy_object.health < 1:
            enemyList.remove(enemy_object)
        else:
            enemy_object.draw(screen, player_x, player_y, xDelta, yDelta)


def draw(mouse, player_x, player_y, playerImage, SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemyList, background, xDelta, yDelta, background_x, background_y):
    i = background_x
    i2 = background_y
    while i <= SCREEN_WIDTH:
        while i2 <= SCREEN_HEIGHT:
            screen.blit(background, (i, i2))
            i2 += 500
        i2 = background_y
        i += 500

    draw_player(mouse, player_x, player_y, playerImage, screen)
    draw_bullet(SCREEN_WIDTH, SCREEN_HEIGHT, screen, xDelta, yDelta)
    draw_enemy(enemyList, screen, player_x, player_y, xDelta, yDelta)
