import cv2
import mediapipe as mp
import time
import numpy as np
import handtrack as ht

from subprocess import call
from subprocess import DEVNULL
import math
video = cv2.VideoCapture(0)
detctor = ht.handdetector()
video.set(3,720)
video.set(4,480)
vol = 0
volbar = 0
ptime =0
ctime = 0
while True:
        check, image = video.read()
        img = cv2.resize(image , (1080,680))
        img = detctor.findhands(img)
        lmlist = detctor.findposition(img,draw=False)
        ctime = time.time()
        if len(lmlist) !=0:
            #print(lmlist[4],lmlist[8])
            x1 , y1 = lmlist[4][1] , lmlist[4][2]
            x2 , y2 = lmlist[8][1] , lmlist[8][2]
            cx , cy = (x1+x2)//2 , (y1+y2)//2
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            length = math.hypot(x2-x1,y2-y1)
            #print(length)
            vol = np.interp(length,[50,300],[0,100])
            volbar = np.interp(length,[50,300],[400,150])


            #print(vol)
            call(["amixer", "-D", "pulse", "sset", "Master", str(vol)+"%"], stdout=DEVNULL,stderr= DEVNULL )
            print(vol)
            if (length <=50):
                cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)

        cv2.rectangle(img,(25,150),(60,400),(0,255,0),3)
        cv2.rectangle(img,(25,int(volbar)),(60,400),(255,0,0),cv2.FILLED)
        cv2.putText(img,str(int(vol))+"%",(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

        fps = 1/(ctime - ptime)
        ptime = ctime
        cv2.putText(img,"FPS : "+str(int(fps)),(15,25),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.imshow('Color Frame', img)
        key = cv2.waitKey(50)
        if key == ord('q'):
                break

###############################################


#######################################
