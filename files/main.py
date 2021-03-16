from DJITelloPy import tello
from time import sleep
import cv2.cv2 as cv2

drone = tello.Tello()
drone.connect()
drone.streamon()
print(drone.get_battery())

while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("image", img)
        cv2.waitKey(1)

