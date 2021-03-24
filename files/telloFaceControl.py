import FaceControlUtils as utils
from djitellopy import tello
from time import sleep
import cv2

drone = tello.Tello()
HEIGHT, WIDTH = 360, 240

def init():
        # connect the drone
        drone.connect()
        drone.streamon()
        bat = int(drone.get_battery())

        print(bat)

        if bat < 20:
                return False

        drone.takeoff()

        drone.move_up(80)

        return True


def get_image():
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (WIDTH,HEIGHT))
        cv2.imshow("Image", img)
        cv2.waitKey(1)

def main():

        if not init():
                return False

        while True:

                img = get_image()
                img, face_info = utils.processFrame(img)

                commands, pErrorYV, pErrorUD = trackFace(face_info, pErrorYV, pErrorUD)

                drone.send_rc_control(
                        commands[0], 
                        commands[1], 
                        commands[2], 
                        commands[3]
                )    

                cv2.imshow('img', img)

                k = cv2.waitKey(30) & 0xff
                if k ==27:
                        break

                sleep(0.1) 


if __name__ == '__main__':
        main()
