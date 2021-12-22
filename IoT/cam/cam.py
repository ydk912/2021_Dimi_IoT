import picamera
import time
path = '/home/pi/src'
cam = picamera.PiCamera()

try:
    cam.resolution = (640, 480)
    cam.start_preview()
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    cam.rotation = 180
    #cam.capture('%s/photo.jpg'%path)
    cam.start_recording('%s/video.h264'%path)
    input('press enter to stop')
    cam.stop_recording()
finally:
    cam.stop_preview()