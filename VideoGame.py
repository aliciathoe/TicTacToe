import pygame
import time


pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0 , 0)

gameDisplay = pygame.display.set_mode((500,500))
gameDisplay.fill(white)
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

#Text
font = pygame.font.SysFont("Arial", 20, True, False)
font1 = pygame.font.SysFont("Arial", 15, True, False)
font2 = pygame.font.SysFont("Arial", 30, True, False)
text1 = font.render("1", True, black, None)
text2 = font.render("2", True, black, None)
text3 = font.render("3", True, black, None)
text4 = font.render("4", True, black, None)
text5 = font.render("5", True, black, None)
text6 = font.render("6", True, black, None)
text7 = font.render("7", True, black, None)
text8 = font.render("8", True, black, None)
text9 = font.render("9", True, black, None)
Title = font2.render("TicTacToe", True, black, None)
Instructions = font1.render("First with three in a row wins!", True, black, None)
gameDisplay.blit(text1, (100,100))
gameDisplay.blit(text2, (205,100))
gameDisplay.blit(text3, (305,100))
gameDisplay.blit(text4, (105,200))
gameDisplay.blit(text5, (205,200))
gameDisplay.blit(text6, (305,200))
gameDisplay.blit(text7, (105,300))
gameDisplay.blit(text8, (205,300))
gameDisplay.blit(text9, (305,300))
gameDisplay.blit(Instructions, (10, 50))
gameDisplay.blit(Title, (5, 0))
pygame.display.update()

#Game Board
pygame.draw.line(gameDisplay, black, (100, 200), (400,200), 2)
pygame.draw.line(gameDisplay, black, (100, 300), (400,300), 2)
pygame.draw.line(gameDisplay, black, (200, 100), (200,400), 2)
pygame.draw.line(gameDisplay, black, (300, 100), (300,400), 2)

pygame.font.init()

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
                    pygame.draw.line(gameDisplay, red, (100, 300), (200, 400),2)
                    pygame.draw.line(gameDisplay, red, (200, 300), (100, 400), 2)
                    pygame.display.update()
            if event.key == pygame.K_2:
                pygame.draw.line(gameDisplay, red, (201, 101), (299, 199),2)
                pygame.draw.line(gameDisplay, red, (299, 101), (201, 199), 2)
                pygame.display.update()
            if event.key == pygame.K_3:
                pygame.draw.line(gameDisplay, red, (301, 101), (399, 199),2)
                pygame.draw.line(gameDisplay, red, (399, 101), (301, 199), 2)
                pygame.display.update()
            if event.key == pygame.K_4:
                pygame.draw.line(gameDisplay, red, (100, 200), (200, 300),2)
                pygame.draw.line(gameDisplay, red, (200, 200), (100, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_5:
                pygame.draw.line(gameDisplay, red, (200, 200), (300, 300),2)
                pygame.draw.line(gameDisplay, red, (300, 200), (200, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_6:
                pygame.draw.line(gameDisplay, red, (300, 200), (400, 300),2)
                pygame.draw.line(gameDisplay, red, (400, 200), (300, 300), 2)
                pygame.display.update()
            if event.key == pygame.K_1:
                pygame.draw.line(gameDisplay, red, (101, 101), (199, 199),2)
                pygame.draw.line(gameDisplay, red, (199, 101), (101, 199), 2)
                pygame.display.update()
            if event.key == pygame.K_8:
                pygame.draw.line(gameDisplay, red, (200, 300), (300, 400),2)
                pygame.draw.line(gameDisplay, red, (300, 300), (200, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_9:
                pygame.draw.line(gameDisplay, red, (300, 300), (400, 400),2)
                pygame.draw.line(gameDisplay, red, (400, 300), (300, 400), 2)
                pygame.display.update()
            if event.key == pygame.K_KP1:
                pygame.draw.circle(gameDisplay, blue, (151,151), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP2:
                pygame.draw.circle(gameDisplay, blue, (251,151), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP3:
                pygame.draw.circle(gameDisplay, blue, (351,151), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP4:
                pygame.draw.circle(gameDisplay, blue, (151,251), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP5:
                pygame.draw.circle(gameDisplay, blue, (251,251), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP6:
                pygame.draw.circle(gameDisplay, blue, (351,251), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP7:
                pygame.draw.circle(gameDisplay, blue, (151,351), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP8:
                pygame.draw.circle(gameDisplay, blue, (251,351), 49, 2)
                pygame.display.update()
            if event.key == pygame.K_KP9:
                pygame.draw.circle(gameDisplay, blue, (351,351), 49, 2)
                pygame.display.update()


pygame.display.update()

pygame.quit()
quit()
