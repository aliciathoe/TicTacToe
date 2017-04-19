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

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.line(gameDisplay, white, (100, 200), (200, 300),2)
            pygame.draw.line(gameDisplay, white, (200, 200), (100, 300), 2)
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            pygame.draw.circle(gameDisplay, white, (200,200), 50, 2)
            pygame.display.update()

pygame.display.update()

pygame.quit()
quit()


#try to find a way to run a function with only specific codes so yu can
#assign each number with its own square

#https://www.pygame.org/docs/ref/event.html
