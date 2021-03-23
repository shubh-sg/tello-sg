import os
import pygame
from time import sleep

pygame.init()
HEIGHT, WIDTH = 400, 400
WIN = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('Tello Keyboard')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LOGO_HEIGHT, LOGO_WIDTH = 100, 100
TELLO_LOGO = pygame.image.load(os.path.join('assets', 'tello_logo.jpg'))
TELLO_LOGO = pygame.transform.scale(TELLO_LOGO, (LOGO_HEIGHT, LOGO_WIDTH))
drone_logo = pygame.Rect((HEIGHT-LOGO_HEIGHT)//2, (WIDTH-LOGO_WIDTH)//2, LOGO_HEIGHT, LOGO_WIDTH)

FPS = 60
VEL = 5

def getKey(keyName, keys_pressed):
        ans = False
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keys_pressed[myKey]:
                ans = True
        return ans

def move_drone(drone_logo, VEL, keys_pressed):
        if getKey("LEFT", keys_pressed) and drone_logo.x - VEL > 0:
                drone_logo.x -= VEL
        if getKey("RIGHT", keys_pressed) and drone_logo.x + VEL + drone_logo.width < WIDTH:
                drone_logo.x += VEL
        if getKey("UP", keys_pressed) and drone_logo.y -VEL > 0:
                drone_logo.y -= VEL
        if getKey("DOWN", keys_pressed) and drone_logo.y + VEL + drone_logo.height < HEIGHT:
                drone_logo.y += VEL


def draw_window(drone_logo) :
        WIN.fill(WHITE)
        WIN.blit(TELLO_LOGO, (drone_logo.x, drone_logo.y))
        pygame.display.update()

def main() :
        clock = pygame.time.Clock()
        run = True
        while run:
                # set fps for the screen
                clock.tick(FPS) 

                # check for exit button clicked
                for eve in pygame.event.get():
                        if eve.type == pygame.QUIT:
                                run = False

                # gives list of keys pressed
                keys_pressed = pygame.key.get_pressed()
                
                #display screen
                draw_window(drone_logo)

                #check input key
                move_drone(drone_logo, VEL, keys_pressed)
        
        pygame.quit()

if __name__ == '__main__':
        main()





