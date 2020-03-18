import pygame
import random
import time

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SNAKE_HEAD_UP = pygame.image.load('./models/head_up.png')
SNAKE_HEAD_RIGHT = pygame.image.load('./models/head_right.png')
SNAKE_HEAD_DOWN = pygame.image.load('./models/head_down.png')
SNAKE_HEAD_LEFT = pygame.image.load('./models/head_left.png')
TAIL_NORMAL = pygame.image.load('./models/tail_normal.png')
FOOD = pygame.image.load('./models/food.png')
BG = pygame.image.load('./models/bg.png')


class Snake(object):
    WIDTH = 20
    HEIGHT = 20
    SPEED = 25

    def __init__(self, window, x, y, direction):
        self.x = x
        self.y = y
        self.height = self.HEIGHT
        self.width = self.WIDTH
        self.speed = self.SPEED
        self.direction = direction
        self.window = window

    def move(self):
        if self.direction == "left" and self.x > 0 + self.width:
            self.x -= self.speed
            WINDOW.blit(SNAKE_HEAD_LEFT, (self.x, self.y))
        if self.direction == "right" and self.x < SCREEN_WIDTH - self.width - self.speed:
            self.x += self.speed
            WINDOW.blit(SNAKE_HEAD_RIGHT, (self.x, self.y))
        if self.direction == "up" and self.y > 0 + self.height:
            self.y -= self.speed
            WINDOW.blit(SNAKE_HEAD_UP, (self.x, self.y))
        if self.direction == "down" and self.y < SCREEN_HEIGHT - self.height - self.speed:
            self.y += self.speed
            WINDOW.blit(SNAKE_HEAD_DOWN, (self.x, self.y))


class Tail(object):
    WIDTH = 20
    HEIGHT = 20
    SPEED = 25

    def __init__(self, window, parent):
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.speed = self.SPEED
        self.parent = parent
        self.x = -20
        self.y = -20
        self.window = window

    def moveTail(self):
        self.x = self.parent.x
        self.y = self.parent.y
        WINDOW.blit(TAIL_NORMAL, (self.x, self.y))


class Food(object):
    WIDTH = 20
    HEIGHT = 20

    def __init__(self, window):
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.window = window
        self.x = random.randrange(0, SCREEN_WIDTH, 25)
        self.y = random.randrange(0, SCREEN_HEIGHT, 25)

    def draw(self):
        WINDOW.blit(FOOD, (self.x, self.y))


def drawGame():

    WINDOW.fill((0, 0, 0))
    if len(foods) < 1:
        foods.append(Food(WINDOW))
    foods[0].draw()
    for piece in reversed(tail):
        piece.moveTail()
    snake.move()
    pygame.display.update()


def getKeys():

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.direction = "left"
    if keys[pygame.K_RIGHT]:
        snake.direction = "right"
    if keys[pygame.K_UP]:
        snake.direction = "up"
    if keys[pygame.K_DOWN]:
        snake.direction = "down"

def eventHandler():

    if len(tail) > 1:
        for i in range(len(tail)-1):
            if tail[i].x == tail[i+1].x and tail[i].y == tail[i+1].y:
                return True
    for piece in tail:
        if piece.x == snake.x and piece.y == snake.y:
            return True
    if len(foods) >= 1:
        if foods[0].x == snake.x and foods[0].y == snake.y:
            tail.append(Tail(WINDOW, tail[-1]))
            foods.pop(0)

def main(tick_rate=10, start_time=time.time(), run=True):

    while run:
        clock.tick(tick_rate)
        if (time.time() - start_time) % 20 > 18:
            print("Speed UP")
            start_time = time.time()
            tick_rate += 1

        getKeys()
        drawGame()
        eventHandler()

        if eventHandler():
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    quit()

tail = []
foods = []
snake = Snake(WINDOW, 0, 0, "right")
tail.append(Tail(WINDOW, snake))
clock = pygame.time.Clock()
main()