import pygame

pygame.init()

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Tic Tac Toe')

#Text
font = pygame.font.SysFont("Arial", 50, True, False)
text = font.render("1", True, white, None)

#Game Board
pygame.draw.line(gameDisplay, white, (100, 200), (400,200), 2)
pygame.draw.line(gameDisplay, white, (100, 300), (400,300), 2)
pygame.draw.line(gameDisplay, white, (200, 100), (200,400), 2)
pygame.draw.line(gameDisplay, white, (300, 100), (300,400), 2)

pygame.font.init()

myfont = pygame.font.SysFont('Arial',30)
textsurface = myfont.render('1', False, (0, 0 , 0))
gameDisplay.blit(textsurface, (0, 0))


pygame.display.update()

gameExit = False
keys = pygame.key.get_pressed()

#Game
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                    pygame.draw.line(gameDisplay, white, (100, 100), (200, 200),2)
                    pygame.draw.line(gameDisplay, white, (200, 100), (100, 200), 2)
                    pygame.display.update()
            if event.key == pygame.K_8:
                pygame.draw.line(gameDisplay, white, (200, 100), (300, 200),2)
                pygame.draw.line(gameDisplay, white, (300, 100), (200, 200), 2)
                pygame.display.update()
            if event.key == pygame.K_9:
                pygame.draw.line(gameDisplay, white, (300, 100), (400, 200),2)
                pygame.draw.line(gameDisplay, white, (400, 100), (300, 200), 2)
                pygame.display.update()
            if event.key == pygame.K_4:
                pygame.draw.line(gameDisplay, white, (100, 200), (200, 300),2)
                pygame.draw.line(gameDisplay, white, (200, 200), (100, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_5:
                pygame.draw.line(gameDisplay, white, (200, 200), (300, 300),2)
                pygame.draw.line(gameDisplay, white, (300, 200), (200, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_6:
                pygame.draw.line(gameDisplay, white, (300, 200), (400, 300),2)
                pygame.draw.line(gameDisplay, white, (400, 200), (300, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_1:
                pygame.draw.line(gameDisplay, white, (100, 300), (200, 400),2)
                pygame.draw.line(gameDisplay, white, (200, 300), (100, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_2:
                pygame.draw.line(gameDisplay, white, (200, 300), (300, 400),2)
                pygame.draw.line(gameDisplay, white, (300, 300), (200, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_3:
                pygame.draw.line(gameDisplay, white, (300, 300), (400, 400),2)
                pygame.draw.line(gameDisplay, white, (400, 300), (300, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_KP7:
                pygame.draw.circle(gameDisplay, white, (150,150), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP8:
                pygame.draw.circle(gameDisplay, white, (250,150), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP9:
                pygame.draw.circle(gameDisplay, white, (350,150), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP4:
                pygame.draw.circle(gameDisplay, white, (150,250), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP5:
                pygame.draw.circle(gameDisplay, white, (250,250), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP6:
                pygame.draw.circle(gameDisplay, white, (350,250), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP1:
                pygame.draw.circle(gameDisplay, white, (150,350), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP2:
                pygame.draw.circle(gameDisplay, white, (250,350), 50, 2)
                pygame.display.update()
            if event.key == pygame.K_KP3:
                pygame.draw.circle(gameDisplay, white, (350,350), 50, 2)
                pygame.display.update()


pygame.display.update()

pygame.quit()
quit()
