import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ankit Aim Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    def draw(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x, self.y), self.size)
        pygame.draw.circle(win,self.SECOND_COLOR,(self.x, self.y), self.size*0.8)
        pygame.draw.circle(win,self.COLOR,(self.x, self.y), self.size*0.6)
        pygame.draw.circle(win,self.SECOND_COLOR,(self.x, self.y), self.size*0.4)


def main():
    run = True
    targets = []

    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)
    pygame.quit()

if __name__ == "__main__":
    main()
