from header import *
import draw


class menu:
    FontHeadline: pygame.font
    FontText: pygame.font

    def init(self, fontProportions: int, screen, enemyList, background_x, background_y, background):
        FontText = pygame.font.SysFont('comicsans', fontProportions, True, True)
        FontHeadline = pygame.font.SysFont('comicsans', 2 * fontProportions, True, True)
        pygame.display.update()
        import main
        main.FramesPerSecond.tick(main.FPS)
        draw.draw_pause_menu(screen, enemyList, background_x, background_y, background, screen.get_width(),
                             screen.get_height())


class pauseMenu(menu):
    def loopMenu(self, screen, enemyList, background_x, background_y, background):
        menuRunning: bool = True
        while menuRunning == True:
            menu.init(160, screen, enemyList, background_x, background_y, background)
            screen.blit(menu.FontHeadline.render("Pause", True, (0, 0, 0)), (
            screen.get_width() / 2 - menu.FontHeadline.size()[0],
            screen.get_height() / 2 - menu.FontHeadline.size()[1] / 2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menuRunning = False
                if event.type == VIDEORESIZE:
                    import main
                    main.player_one.position_x = screen.get_width() / 2
                    main.player_one.position_y = screen.get_height() / 2


class mainMenu(menu):
    def loopMenu():
        menuRunning: bool = True
        while menuRunning == True:
            menu.init(160)
            screen.blit(FontText.render("Pause", True, (0, 0, 0)),
                        (screen.get_width() / 2 - FontText.size()[0], screen.get_height() / 2 - FontText.size()[1] / 2))
            for event in pygame.event.get():
                if event.type == VIDEORESIZE:
                    import main
                    main.player_one.position_x = screen.get_width() / 2
                    main.player_one.position_y = screen.get_height() / 2
            # pygame.draw.rect(screen.get_width()/2, screen.get_height()/2, 200, 20)
