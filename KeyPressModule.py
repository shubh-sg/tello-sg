import pygame
from time import sleep

def init():
        pygame.init()
        win = pygame.display.set_mode((400, 400))

def getKey(keyName):
        ans = False
        for eve in pygame.event.get(): pass
        keyInput = pygame.key.get_pressed()
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keyInput[myKey]:
                ans = True
        pygame.display.update()

        return ans


def checkKey():
        if (getKey("q")):
                return False
        if getKey("LEFT"):
                print("left key pressed")
        if getKey("RIGHT"):
                print("right key pressed")
        if getKey("UP"):
                print("up key pressed")
        if getKey("DOWN"):
                print("down key pressed")

        return True


if __name__ == '__main__':
        init()
        while(checkKey()):
                sleep(0.1)