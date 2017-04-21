import pygame

pygame.init()

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Tic Tac Toe')

#Game Board
pygame.draw.line(gameDisplay, white, (100, 200), (400,200), 2)
pygame.draw.line(gameDisplay, white, (100, 300), (400,300), 2)
pygame.draw.line(gameDisplay, white, (200, 100), (200,400), 2)
pygame.draw.line(gameDisplay, white, (300, 100), (300,400), 2)


pygame.display.update()

gameExit = False
keys = pygame.key.get_pressed()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                    pygame.draw.line(gameDisplay, white, (100, 100), (200, 200),2)
                    pygame.draw.line(gameDisplay, white, (200, 100), (100, 200), 2)
                    pygame.display.update()
            if event.key == pygame.K_2:
                pygame.draw.line(gameDisplay, white, (200, 100), (300, 200),2)
                pygame.draw.line(gameDisplay, white, (300, 100), (200, 200), 2)
                pygame.display.update()
            if event.key == pygame.K_3:
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
            if event.key == pygame.K_7:
                pygame.draw.line(gameDisplay, white, (100, 300), (200, 400),2)
                pygame.draw.line(gameDisplay, white, (200, 300), (100, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_8:
                pygame.draw.line(gameDisplay, white, (200, 300), (300, 400),2)
                pygame.draw.line(gameDisplay, white, (300, 300), (200, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_9:
                pygame.draw.line(gameDisplay, white, (300, 300), (400, 400),2)
                pygame.draw.line(gameDisplay, white, (400, 300), (300, 400), 2)
                pygame.display.update()



pygame.display.update()

pygame.quit()
quit()


#try to find a way to run a function with only specific codes so yu can
#assign each number with its own square

#https://www.pygame.org/docs/ref/event.html
