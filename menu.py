import header

class menu:
    def loopMenu(fontSize: int):
        menuRunning: bool = True
        while menuRunning == True:
            fontSize = 160 #del
            Font = pygame.font.SysFont('comicsans', fontSize, True, True)
            screen.blit(pauseFont.render("Pause", True, (0, 0, 0)), (SCREEN_WIDTH/2-fontSize, SCREEN_HEIGHT/2-fontSize/2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menuRunning = False
            pygame.display.update()
            FramesPerSecond.tick(FPS)
            draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, SCREEN_WIDTH, SCREEN_HEIGHT)

class pauseMenu(menu):
    None

class mainMenu(menu):
    None

