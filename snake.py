import pygame as pg
import random

pg.init()
windowHeight = 500
windowWidth = 500
window = pg.display.set_mode((windowWidth, windowHeight))
pg.display.set_caption('Snake')

clock = pg.time.Clock()
snakeSpeed = 10
snakeSize = 10


def DrawSnake(snakeSize, snakeList):
    for x in snakeList:
        pg.draw.rect(window, (200, 212, 0), [x[0], x[1], snakeSize, snakeSize])


def Message(msg, size, color, x, y):
    fontStyle = pg.font.SysFont(None, size)
    text = fontStyle.render(msg, True, color)
    window.blit(text, [x, y])


def Game():
    gameOver = False
    gameClose = False

    x_start = windowWidth/2
    y_start = windowHeight/2

    x_move = 0
    y_move = 0

    snakeList = []
    snakeLength = 1

    x_food = round(random.randrange(0, windowWidth - snakeSize)/10.0)*10.0
    y_food = round(random.randrange(0, windowWidth - snakeSize)/10.0)*10.0

    while not gameOver:

        while gameClose == True:
            window.fill((0, 0, 0))
            Message("Twój wynik: " + str(snakeLength - 1), 50,
                    (255, 0, 0), windowWidth/4, windowHeight/3)
            Message("[X] - Zakończ", 30, (0, 255, 0),
                    windowWidth/4, windowHeight/3 + 60)
            Message("[SPACJA] - Nowa gra", 30, (0, 255, 0),
                    windowWidth/4, windowHeight/3 + 90)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameOver = True
                    gameClose = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_x:
                        gameOver = True
                        gameClose = False
                    if event.key == pg.K_SPACE:
                        Game()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameOver = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    x_move = 0
                    y_move = -snakeSize
                elif event.key == pg.K_DOWN:
                    x_move = 0
                    y_move = snakeSize
                elif event.key == pg.K_RIGHT:
                    x_move = snakeSize
                    y_move = 0
                elif event.key == pg.K_LEFT:
                    x_move = -snakeSize
                    y_move = 0

        if x_start >= windowWidth or x_start < 0 or y_start >= windowHeight or y_start < 0:
            gameClose = True

        x_start += x_move
        y_start += y_move
        window.fill((0, 0, 0))

        pg.draw.rect(window, (255, 0, 0), [
                     x_food, y_food, snakeSize, snakeSize])

        snakeHead = []
        snakeHead.append(x_start)
        snakeHead.append(y_start)

        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
        DrawSnake(snakeSize, snakeList)
        pg.display.update()

        if x_start == x_food and y_start == y_food:
            x_food = round(random.randrange(
                0, windowWidth - snakeSize)/10.0) * 10.0
            y_food = round(random.randrange(
                0, windowWidth - snakeSize)/10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)

    pg.quit()
    quit()


Game()
