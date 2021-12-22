import cv2

fc = cv2.CascadeClassifier('./xml/haarcascade_frontalface_Default.xml')
ec = cv2.CascadeClassifier('./xml/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failure')
    exit()

#text=input("img nom : ")

#img = cv2.imread(text+'.jpg')

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fac = fc.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in fac:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)

        r_gray = gray[y:y+h,x:x+w]
        r_col = frame[y:y+h,x:x+w]

        eys = ec.detectMultiScale(r_gray)

        for(ex,ey,ew,eh) in eys:
            cv2.rectangle(r_col, (ex,ey), (ex+ew,ey+eh),(0,255,0),2)
    if not ret:
        break
    cv2.imshow('vid',frame)
    if cv2.waitKey(10)==27:
        break

cv2.destroyAllWindows()