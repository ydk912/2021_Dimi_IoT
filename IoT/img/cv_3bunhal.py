import cv2

cap = cv2.VideoCapture(0)
#DIVX(avi) X264(h264) MP4V(mp4)
if not cap.isOpened():
    print('Failure')
    exit()

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#out=cv2.VideoWriter('output.avi',fourcc,24,(320,240))

while True:
    ret,frame=cap.read()
    if not ret:
        break
    canny = cv2.Canny(frame, 100, 150)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('vid',frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge',canny)
    #out.write(frame)
    if cv2.waitKey(10)==13:
        break

cap.release()
#out.release()
cv2.destroyAllWindows()