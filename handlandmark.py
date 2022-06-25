import cv2
import mediapipe as mp
import time
import handtrack as ht

video = cv2.VideoCapture(0)
detctor = ht.handdetector()
ptime =0
ctime = 0
while True:
        check, img = video.read()
        #img = cv2.resize(image , (960,980))
        img = detctor.findhands(img)
        lmlist = detctor.findposition(img,draw=False)
        ctime = time.time()
        if len(lmlist) !=0:

            print(lmlist[4])
        fps = 1/(ctime - ptime)
        ptime = ctime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        cv2.imshow('Color Frame', img)
        key = cv2.waitKey(50)
        if key == ord('q'):
                break
