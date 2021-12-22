import picamera
import time
path = '/home/pi/src'
cam = picamera.PiCamera()

try:
    cam.resolution = (640, 480)
    cam.start_preview()
    cam.rotation = 180
    i=int(input("1 : photo\n2 : video\n9 : exit\n>"))
    while i is not 9:
        if i is 1 or i is 2:
            print("taking photo..." if i is 1 else "taking video...")
            text=input("file name >")
            text=text+time.strftime('_%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
            for t in range(3,0,-1):
                print(t)
                time.sleep(1)
            print()
            if i==1:
                cam.capture('%s/%s.jpg'%(path,text))
            elif i==2:
                cam.start_recording('%s/%s.h264'%(path,text))
                input('recording\npress enter to stop...')
                cam.stop_recording()
            print("photo taken!\n" if i is 1 else "video taken!\n")
        else:
            print("incorrect input\n")
        i=int(input("1 : photo\n2 : video\n9 : exit\n>"))
finally:
    cam.stop_preview()