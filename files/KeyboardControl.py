from djitellopy import tello
from threading import Thread
from time import sleep, time
import pygame 
import cv2
import os

drone = tello.Tello()
pygame.init()
HEIGHT, WIDTH = 400, 400
WIN = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('Tello Keyboard')
fps = 60

def init():
        drone.connect()
                # print('connection unsuccessful')
        drone.streamon()
        print (drone.get_battery())

def get_image():
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (360,240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)

def getKey(keyName, keyInput):
        ans = False
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keyInput[myKey]:
                ans = True
        return ans

def main():

        init()
        clock = pygame.time.Clock()

        run = True
        while run:

                clock.tick(fps)
        
                get_image()
                for eve in pygame.event.get():
                        if eve.type == pygame.QUIT:
                                run = False

                keys_pressed = pygame.key.get_pressed()

                lr, fb, ud, yv = 0, 0, 0, 0
                speed = 50

                if getKey("e", keys_pressed): 
                        if not drone.is_flying: drone.takeoff()

                if getKey("p", keys_pressed):
                        filename = os.path.join('images', '{}.jpg'.format(time))
                        cv2.imwrite(filename, img)
                        
                if drone.is_flying:

                        if getKey("q", keys_pressed): drone.land()

                        if getKey("LEFT", keys_pressed): lr = -speed
                        elif getKey("RIGHT", keys_pressed): lr = speed

                        if getKey("UP", keys_pressed): fb = speed
                        elif getKey("DOWN", keys_pressed): fb = -speed

                        if getKey("w", keys_pressed): ud = speed
                        elif getKey("s", keys_pressed): ud = -speed

                        if getKey("a", keys_pressed): yv = speed
                        elif getKey("d", keys_pressed): yv = -speed

                        drone.send_rc_control (lr, fb, ud, yv)

                pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
        main()