import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('JumpingCat v0.1 Alpha')
WHITE = (255, 255, 255)

# environment constants
GRAVITY = 0.3
FRICTION = 0.1

class Sprite():
    def __init__(self, imgPath, initial_xPos = 0, initial_yPos = 0, initial_xVel = 0, initial_yVel = 0, moveSpeed = 1, jumpVel = 10):
        self.imgPath = imgPath
        self.imgObj = pygame.image.load(self.imgPath)
        self.x_pos = initial_xPos
        self.y_pos = initial_yPos
        self.x_vel = initial_xVel
        self.y_vel = initial_yVel
        self.sizeX, self.sizeY = self.imgObj.get_rect().size
        self.moveSpeed = moveSpeed
        self.jumpVel = jumpVel

    def move(self, x_dist = 0, y_dist = 0):
        self.x_pos += x_dist
        self.y_pos += y_dist

        # keep object in frame
        if self.x_pos < 0:
            self.x_pos = 0
            self.x_vel = 0
        if self.x_pos > WINDOWWIDTH - self.sizeX:
            self.x_pos = WINDOWWIDTH - self.sizeX
            self.x_vel = 0
        if self.y_pos < 0:
            self.y_pos = 0
            self.y_vel = 0
        if self.y_pos > WINDOWHEIGHT - self.sizeY:
            self.y_pos = WINDOWHEIGHT - self.sizeY
            self.y_vel = 0

    def moveTo(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def jump(self, jump_vel=0):
        if not jump_vel:
            jump_vel = self.jumpVel
        self.y_vel -= jump_vel

def main():
    #create sprite objects
    Cat = Sprite('cat.png', moveSpeed=5)
    #Cat.moveTo(WINDOWWIDTH / 2 - (Cat.sizeX / 2), WINDOWHEIGHT - Cat.sizeY)
    Cat.moveTo(WINDOWWIDTH / 2 - (Cat.sizeX / 2), 0)

    # main game loop
    while True: # the main game loop
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Cat.imgObj, (Cat.x_pos, Cat.y_pos))

        # physics
        Cat.move(x_dist=Cat.x_vel, y_dist=Cat.y_vel)

        # drop down due to gravity
        Cat.y_vel += GRAVITY

        # slow down in x direction due to friction
        if Cat.x_vel < -FRICTION:
            Cat.x_vel += FRICTION
        elif Cat.x_vel > FRICTION:
            Cat.x_vel -= FRICTION
        else:
            Cat.x_vel = 0

        # bounce up due to hitting ground
        if Cat.y_pos == WINDOWHEIGHT - Cat.sizeY:
            Cat.y_vel = -8


        # handle key states
        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT]:
            #Cat.move(x_dist=Cat.moveSpeed * -1)
            Cat.x_vel -= 0.5
        if keystate[K_RIGHT]:
            #Cat.move(x_dist=Cat.moveSpeed)
            Cat.x_vel += 0.5

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Cat.jump()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()