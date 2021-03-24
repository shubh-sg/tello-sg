import os
import cv2
import pygame
from time import sleep, time
from djitellopy import tello

# initialize pygame
pygame.init()
HEIGHT, WIDTH = 600, 600
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('tello keyboard')
FPS = 60

# initialize drone logo
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LOGO_HEIGHT, LOGO_WIDTH = 100, 100
TELLO_LOGO = pygame.image.load(os.path.join('assets', 'tello_logo.jpg'))
TELLO_LOGO = pygame.transform.scale(TELLO_LOGO, (LOGO_HEIGHT, LOGO_WIDTH))
drone_logo = pygame.Rect((HEIGHT-LOGO_HEIGHT)//2, (WIDTH-LOGO_WIDTH)//2, LOGO_HEIGHT, LOGO_WIDTH)

# initialize tello drone
drone = tello.Tello()

def init():
        # connect the drone
        drone.connect()
        drone.streamon()
        print(drone.get_battery)

def getKey(keyName, keys_pressed):
        ans = False
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keys_pressed[myKey]:
                ans = True
        return ans

def set_drone_controls(keys_pressed):
        lr, fb, ud, yv = 0, 0, 0, 0
        speed = 50

        if getKey("LEFT", keys_pressed): lr = -speed
        elif getKey("RIGHT", keys_pressed): lr = speed

        if getKey("UP", keys_pressed): fb = speed
        elif getKey("DOWN", keys_pressed): fb = -speed

        if getKey("w", keys_pressed): ud = speed
        elif getKey("s", keys_pressed): ud = -speed

        if getKey("a", keys_pressed): yv = -speed
        elif getKey("d", keys_pressed): yv = speed

        drone.send_rc_control (lr, fb, ud, yv)

def get_image(keys_pressed):
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (360,240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        if (getKey('p', keys_pressed)):
                filename = os.path.join('images', '{}.jpg'.format(time))
                cv2.imwrite(filename, img)


def set_logo_controls(keys_pressed, VEL = 5):
        if getKey("LEFT", keys_pressed) and drone_logo.x - VEL > 0:
                drone_logo.x -= VEL
        if getKey("RIGHT", keys_pressed) and drone_logo.x + VEL + drone_logo.width < WIDTH:
                drone_logo.x += VEL
        if getKey("UP", keys_pressed) and drone_logo.y -VEL > 0:
                drone_logo.y -= VEL
        if getKey("DOWN", keys_pressed) and drone_logo.y + VEL + drone_logo.height < HEIGHT:
                drone_logo.y += VEL


def draw_window() :
        WIN.fill(WHITE)
        WIN.blit(TELLO_LOGO, (drone_logo.x, drone_logo.y))
        pygame.display.update()


def main() :
        init()
        clock = pygame.time.Clock()

        run = True
        while run:
                
                clock.tick(FPS)

                for eve in pygame.event.get():
                        if eve.type == pygame.QUIT:
                                cv2.destroyAllWindows()
                                drone.end()
                                run = False

                keys_pressed = pygame.key.get_pressed()

                get_image(keys_pressed)

                if drone.is_flying :
                        if (getKey('q', keys_pressed)):
                                drone.land()

                        set_drone_controls(keys_pressed)
                        set_logo_controls(keys_pressed)
                        
                        
                elif getKey('e', keys_pressed):
                        drone.takeoff()
                        sleep(5)

                draw_window()



if __name__ == '__main__' :
        main()