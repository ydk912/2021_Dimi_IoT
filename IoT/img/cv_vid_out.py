import cv2

cap = cv2.VideoCapture(0)
#DIVX(avi) X264(h264) MP4V(mp4)
if not cap.isOpened():
    print('Failure')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out=cv2.VideoWriter('output.avi',fourcc,24,(640,480))

while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow('vid',frame)
    out.write(frame)
    if cv2.waitKey(10)==27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()