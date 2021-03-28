from djitellopy import Tello
from threading import Thread
from time import sleep


drone = Tello()

drone.connect()
drone.streamon()
drone.streamoff()

drone.takeoff()
drone.land()
drone.emergency()

##############################
####### take imgage:
##############################

# background frame read
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

print(drone.is_flying)
print(drone.stream_on)

##############################
####### state functions :
##############################

drone.get_pitch()
# pitch in degree

drone.get_roll
# roll in degree

drone.get_yaw
# yaw in degree

drone.get_speed_x()
drone.get_speed_y()
drone.get_speed_z()
# get speed in int

drone.get_acceleration_x()
drone.get_acceleration_y()
drone.get_acceleration_z()
# get acceleration in int

drone.get_height()
# get height in cm

drone.get_distance_tof()
# current distance from tof in cm

drone.get_barometer()
# barometer measurement in cm

drone.get_flight_time()
# flight time in s

drone.get_battery()
# get battery percentage


##############################
####### control functions :
##############################

# drone.move_x(int dist)
# x : up, down, left, right, forawrd, back
# dist : 20-500

# drone.rotate_clockwise(int deg)
# drone.rotate_counter_clockwise(int deg)
# deg : 1-3600

# drone.flip_x()
# x : left, right, forward, back

drone.go_xyz_speed(x, y, z, speed)
# x,y,z : 20-500
# speed : 10-100
# fly to xyz relative to current position

drone.curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)
# goto x2y2z2 via x1y1z1
# radius b/w 0.5 - 10 meters
# x,y,z : -500-500
# speed : 10-60

drone.set_speed(x)
# x : 10-100

drone.send_rc_control(lr, fb, ud, yv)
# velocity : -100 - 100

































