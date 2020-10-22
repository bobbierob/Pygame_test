import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)

catImg = pygame.image.load('cat.png')
catImgX, catImgY = catImg.get_rect().size
catx = WINDOWWIDTH / 2 - (catImgX / 2)
caty = WINDOWHEIGHT - catImgY
CATSPEED = 5

def main():
    while True: # the main game loop
        DISPLAYSURF.fill(WHITE)
        # keep cat in frame
        if catx < 0:
            catx = 0
        if catx > WINDOWWIDTH - catImgX:
            catx = WINDOWWIDTH - catImgX
        if caty < 0:
            caty = 0
        if caty > WINDOWHEIGHT - catImgY:
            caty = WINDOWHEIGHT - catImgY

        DISPLAYSURF.blit(catImg, (catx, caty))
        keystate = pygame.key.get_pressed()
        if keystate[K_UP]:
            caty -= CATSPEED
        if keystate[K_DOWN]:
            caty += CATSPEED
        if keystate[K_LEFT]:
            catx -= CATSPEED
        if keystate[K_RIGHT]:
            catx += CATSPEED

        for event in pygame.event.get():
            print(event)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

def Jump(image, height):
    pass

if __name__ == '__main__':
    main()