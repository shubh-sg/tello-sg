from FaceTrackerModule import *
from djitellopy import tello
from time import sleep
import cv2

pErrorYV, pErrorUD = 0, 0
HEIGHT, WIDTH = 360, 480

drone = tello.Tello()

def init():
        drone.connect()
        drone.streamon()
        if drone.get_battery() < 20:
                return False

        print(drone.get_battery())

        drone.takeoff()
        drone.move_up(80)

        img = get_image()
        img, face_info, hand_info = processFrame(img)

        while face_info[1] == 0:
                drone.send_rc_control(0, 0, 0, 20)
                img = get_image()
                if img is None:
                        continue
                img, face_info, hand_info = processFrame(img)
                cv2.imshow('img', img)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        return False

        drone.send_rc_control(0, 0, 0, 0)

        return True


def get_image():
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (WIDTH, HEIGHT))
        return img


def main():
        if not init():
                return

        global pErrorYV, pErrorUD
        
        run = True
        while run:

                img = get_image()
                if img is None:
                        continue

                img, face_info, hand_info = processFrame(img)
                commands, pErrorYV, pErrorUD = follow_face(face_info, pErrorYV, pErrorUD)
                displayText(img, commands, face_info, hand_info)    
                cv2.imshow('img', img)

                lr, fb, ud, yv = commands
                drone.send_rc_control(lr, fb, ud, yv)

                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        run = False

        cv2.destroyAllWindows()
        drone.land()
        drone.end()


if __name__ == '__main__':
        main()

