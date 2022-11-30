import pygame

def MainGame(curscreen, scenesList, player1, screen, clock, item, visibleSprites):#main game scene
    while curscreen == scenesList[0]:#main gameloop
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
                    curscreen = scenesList[1]

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
        # debug(player1)
        clock.tick(500)

def MainMenu(curscreen, scenesList, colors, visibleSprites, screen):
    while curscreen==scenesList[1]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(colors["BG"])
        updateScreen(visibleSprites, screen)
        pygame.display.update()
        clock.tick(500)
