import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failure')
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow('vid',frame)
    if cv2.waitKey(10)==5:
        break

cap.release()
cv2.destroyAllWindows()