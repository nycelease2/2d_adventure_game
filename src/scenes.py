import pygame

def MainGame(sceneManagment, colors, player1, screen, clock, item, visibleSprites, updateScreen, itemGetCheck, debug):#main game scene
    while sceneManagment.curscreen == sceneManagment.sceneList[0]:#main gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #controls
            elif event.type == pygame.KEYDOWN:
                #X axis
                if event.key == pygame.K_a:
                    player1.xVel -= player1.movementSpeed
                elif event.key == pygame.K_d:
                    player1.xVel += player1.movementSpeed

                #Y axis
                elif event.key == pygame.K_w:
                    player1.yVel -= player1.movementSpeed
                elif event.key == pygame.K_s:
                    player1.yVel += player1.movementSpeed

                #MainMenu
                elif event.key == pygame.K_ESCAPE:
                    print("Main Menu Starting")
                    sceneManagment.gotoscene(1)

            elif event.type == pygame.KEYUP:
                #X axis
                if event.key == pygame.K_a:
                    player1.xVel = 0
                elif event.key == pygame.K_d:
                    player1.xVel = 0

                #Y axis
                elif event.key == pygame.K_w:
                    player1.yVel = 0
                elif event.key == pygame.K_s:
                    player1.yVel = 0

        screen.fill(colors["BG"])
        updateScreen(visibleSprites, screen)
        for i in item:
            itemGetCheck(i, player1)
        pygame.display.update()
        #debug(player1)
        clock.tick(500)

def MainMenu(sceneManagment, colors, visibleSprites, screen, updateScreen, clock):
    print("i ran")
    while sceneManagment.curscreen == sceneManagment.sceneList[1]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(colors["BG"])
        updateScreen(visibleSprites, screen)
        pygame.display.update()
        clock.tick(500)
