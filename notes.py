from djitellopy import Tello
from threading import Thread
from time import sleep


drone = Tello()

drone.connect()
drone.streamon()

drone.takeoff()
drone.land()

##############################
####### take imgage:
##############################

frame_read = drone.get_frame_read()
cv2.imwrite("picture.png", frame_read.frame)


##############################
####### capture video : 
##############################

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)
    video.release()

keepRecording = True
frame_read = drone.get_frame_read()
recorder = Thread(target=videoRecorder)
recorder.start()
keepRecording = False
recorder.join()


##############################
####### state fields :
##############################

# pitch, roll, yaw
# vgx, vgy, vgz
# templ, temph
# tof, h, bat, time
# baro
# agx, agy, agz

()drone.stream_on

##############################
####### state functions :
##############################

drone.


