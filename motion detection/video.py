import cv2
from datetime import datetime
import pandas as pd
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
check,first_frame = camera.read()
first_frame = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame,(21,21),0)
prev_status=0
status=0
time=[]
while True:
    status=0
    check,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    # picture = first_frame-gray
    delta = cv2.absdiff(first_frame,gray)
    # cv2.imshow("gray",delta)
    thresh_frame = cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=2)
    cv2.imshow("seee",thresh_frame)

    (cnts,_)=cv2.findContours(thresh_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue
        status=1
        # frame=cv2.drawContours(frame,contour,-1,(0,255,0),4)
        x,y,w,h=cv2.boundingRect(contour)
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    if prev_status != status:
        time.append(datetime.now())
        prev_status=status

    cv2.imshow("MAIN",frame)
    key=cv2.waitKey(1)
    if key == ord("q"):
        if status==1:
            time.append(datetime.now())
        break
    print(status)
camera.release()

cv2.destroyAllWindows()
# for i in time:
#     print(i)
df = pd.DataFrame(columns=["Start","End"])
for i in range(0,len(time),2):
    df = df.append({"Start":time[i],"End":time[i+1]},ignore_index=True)

df.to_csv("times.csv")