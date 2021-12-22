import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failure')
    exit()

ret, frame = cap.read()
cv2.imshow('frame',frame)
cv2.imwrite('output.jpg',frame)

cv2.waitKey()

cap.release()
cv2.destroyAllWindows()