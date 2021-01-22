import header

class menu:
    def init(self, fontProportions: int):
        FontText = pygame.font.SysFont('comicsans', fontProportions, True, True)
        FontHeadline = pygame.font.SysFont('comicsans', 2*fontProportions, True, True)
        pygame.display.update()
        FramesPerSecond.tick(FPS)
        draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, SCREEN_WIDTH, SCREEN_HEIGHT)

class pauseMenu(menu):
        def loopMenu(self, fontSize: int):
            menuRunning: bool = True
            while menuRunning == True:
                init(160)
                screen.blit(FontHeadline.render("Pause", True, (0, 0, 0)), (screen.get_width()/2-FontHeadline.size()[0], screen.get_height()/2-FontHeadline.size()[1]/2))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            menuRunning = False
                    if event.type == VIDEORESIZE:
                        player_one.position_x = screen.get_width() / 2
                        player_one.position_y = screen.get_height() / 2


class mainMenu(menu):
        def loopMenu(self):
            menuRunning: bool = True
            while menuRunning == True:
                init(160)
                screen.blit(FontText.render("Pause", True, (0, 0, 0)), (screen.get_width()/2-FontText.size()[0], screen.get_height()/2-FontText.size()[1]/2))
                for event in pygame.event.get():
                    if event.type == VIDEORESIZE:
                        player_one.position_x = screen.get_width() / 2
                        player_one.position_y = screen.get_height() / 2
                pygame.draw.rect(screen.get_width()/2, screen.get_height()/2, 200, 20)

