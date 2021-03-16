from djitellopy import tello
from time import sleep
import KeyPressModule as kp 

kp.init()
drone = tello.Tello()
drone.connect()
print (drone.get_battery())

def getKeyboardInput():
        lr, fb, ud, yv = 0, 0, 0, 0
        speed = 50

        if kp.getKey("q"): drone.land()
        if kp.getKey("e"): drone.takeoff()

        if kp.getKey("LEFT"): lr = -speed
        elif kp.getKey("RIGHT"): lr = speed

        if kp.getKey("UP"): fb = speed
        elif kp.getKey("DOWN"): fb = -speed

        if kp.getKey("w"): ud = speed
        elif kp.getKey("s"): ud = -speed

        if kp.getKey("a"): yv = speed
        elif kp.getKey("d"): yv = -speed

        return [lr, fb, ud, yv]


def main():
        while True:
                vals = getKeyboardInput()
                drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
                sleep(0.5)

if __name__ == '__main__':
        main()